from __future__ import annotations
import json, time
from pathlib import Path
import numpy as np
from statorch.data.synthetic import load_spec, generate_episode
from statorch.source.classifier import train_source_classifier
from statorch.source.reference import fit_gaussian_reference
from statorch.tools.quantification import emq
from statorch.tools.classification import prior_correct
from statorch.tools.ood import mahalanobis_score
from statorch.sensors.shift import mmd_rbf, domain_classifier_auc
from statorch.sensors.uncertainty import bootstrap_emq
from statorch.sensors.goodness_of_fit import posterior_residual, fit_score_from_residual
from statorch.metrics.prevalence import l1_error
from statorch.metrics.classification import classification_metrics
from statorch.metrics.ood import ood_metrics
from statorch.agent.router import DemoDiagnosisRouter
from statorch.agent.controller import make_certificate


def _bundle_eval(ep,name,seed=0,bootstrap=80):
    sm=ep.source_measurements[name]; tm=ep.target_measurements[name]
    model=train_source_classifier(sm,ep.source_y,seed)
    p=model.predict_proba(tm)
    beta=emq(p,model.source_prior)
    ui=bootstrap_emq(p,model.source_prior,reps=bootstrap,seed=seed)
    resid=posterior_residual(p,beta); fit=fit_score_from_residual(resid)
    # Speed: shift diagnostics on capped subsets.
    mmd=mmd_rbf(sm[:350],tm[:350]); auc=domain_classifier_auc(sm[:500],tm[:500],seed)
    pc=prior_correct(p,model.source_prior,beta); yhat=pc.argmax(1)
    cls=classification_metrics(ep.hidden_truth.target_labels,yhat)
    ref=fit_gaussian_reference(sm,ep.source_y)
    ood=mahalanobis_score(tm,ref)
    om=ood_metrics(ep.hidden_truth.unknown_mask.astype(int),ood)
    return {'bundle':name,'beta':beta,'mean_ci_width':ui['mean_width'],'max_ci_width':ui['max_width'],
            'residual':resid,'fit_score':fit,'mmd':mmd,'domain_auc':auc,'macro_f1':cls['macro_f1'],
            'accuracy':cls['accuracy'],'ood_auroc':om['auroc'],'ood_aupr':om['aupr']}


def run_demo(config_path='configs/demo.yaml',out='results/demo'):
    t0=time.time(); spec,bundles,costs=load_spec(config_path); ep=generate_episode(spec,bundles,costs)
    out=Path(out); out.mkdir(parents=True,exist_ok=True)
    results={name:_bundle_eval(ep,name,spec.seed+i,bootstrap=80) for i,name in enumerate(bundles)}
    router=DemoDiagnosisRouter()
    stats={k:{'domain_auc':v['domain_auc'],'unc_width':v['mean_ci_width'],'fit_score':v['fit_score']} for k,v in results.items()}
    selected,scores=router.choose_bundle(stats,costs)
    fixed='ALL'; chosen=results[selected]; base=results[fixed]
    truth=ep.hidden_truth.known_prevalence
    summary={
        'seed':spec.seed,'selected_bundle':selected,'fixed_bundle':fixed,'scores':scores,
        'truth_beta':truth.tolist(),
        'selected_beta':chosen['beta'].tolist(),'fixed_beta':base['beta'].tolist(),
        'selected_beta_l1':l1_error(chosen['beta'],truth),'fixed_beta_l1':l1_error(base['beta'],truth),
        'selected_macro_f1':chosen['macro_f1'],'fixed_macro_f1':base['macro_f1'],
        'selected_ood_auroc':chosen['ood_auroc'],'fixed_ood_auroc':base['ood_auroc'],
        'selected_cost':costs[selected],'fixed_cost':costs[fixed],
        'runtime_s':time.time()-t0,
        'note':'Self-contained demonstration only; not a reproduction of manuscript headline experiments.'}
    before={'uncertainty':base['mean_ci_width'],'residual':base['residual']}
    after={'uncertainty':chosen['mean_ci_width'],'residual':chosen['residual']}
    cert=make_certificate(0,{'ALL':stats['ALL'],'selected':stats[selected]},
        {'information_shortage':float(base['mean_ci_width']),'measurement_shift':float(abs(base['domain_auc']-.5)*2)},
        {'tool':'MEASUREMENT_ROUTING','bundle':selected,'cost':costs[selected]},before,after,{'uncertainty':-1,'residual':-1})
    for v in results.values(): v['beta']=v['beta'].tolist()
    (out/'bundle_results.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
    (out/'summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
    (out/'certificate.json').write_text(json.dumps(cert.to_dict(),indent=2),encoding='utf-8')
    return summary
