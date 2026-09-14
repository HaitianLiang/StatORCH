from sklearn.metrics import roc_auc_score, average_precision_score

def ood_metrics(y_unknown, score):
    return {'auroc':float(roc_auc_score(y_unknown,score)),
            'aupr':float(average_precision_score(y_unknown,score))}
