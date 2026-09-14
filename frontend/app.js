const get = async p => (await fetch(`data/${p}.json`)).json();
const fmt = (x,d=3) => Number(x).toFixed(d);
const navButtons=[...document.querySelectorAll('.nav button')];
navButtons.forEach(b=>b.onclick=()=>{navButtons.forEach(x=>x.classList.remove('active'));b.classList.add('active');document.querySelectorAll('.page').forEach(x=>x.classList.remove('active'));document.getElementById(b.dataset.section).classList.add('active')});
function metricCard(value,label,delta){return `<div class="metric"><div class="value">${value}</div><div class="label">${label}</div><div class="delta">${delta}</div></div>`}
function bars(rows,key,flip=false){const vals=rows.map(r=>Number(r[key]));const max=Math.max(...vals);return rows.map(r=>{let v=Number(r[key]);let width=100*v/max;return `<div class="bar-row"><div class="bar-label">${r.method||r.policy}</div><div class="bar-track"><div class="bar-fill" style="width:${width}%"></div></div><div class="bar-value">${fmt(v)}</div></div>`}).join('')}
(async function(){
 const [overall,abl,mods,external,trace,scope,open,routers]=await Promise.all([get('overall'),get('measurement_ablation'),get('module_routing'),get('external'),get('trajectory'),get('claim_scope'),get('matched_openworld'),get('router_artifacts')]);
 const s=overall.find(x=>x.method==='StatOrch'), n=overall.find(x=>x.method==='NearCost');
 document.getElementById('metric-cards').innerHTML=[
  metricCard(fmt(s.beta_l1),'β L1 ↓',`${((Number(n.beta_l1)-Number(s.beta_l1))/Number(n.beta_l1)*100).toFixed(1)}% vs NearCost`),
  metricCard(fmt(s.macro_f1),'Macro-F1 ↑',`+${((Number(s.macro_f1)-Number(n.macro_f1))*100).toFixed(2)} pp`),
  metricCard(fmt(s.rho_error),'unknown-mass err ↓',`${((Number(n.rho_error)-Number(s.rho_error))/Number(n.rho_error)*100).toFixed(1)}% vs NearCost`),
  metricCard(fmt(s.auroc),'OOD AUROC ↑',`+${((Number(s.auroc)-Number(n.auroc))*100).toFixed(2)} pp`),
  metricCard(fmt(s.aupr),'OOD AUPR ↑',`+${((Number(s.aupr)-Number(n.aupr))*100).toFixed(2)} pp`),
  metricCard(Number(s.cost).toFixed(0),'Mean cost ↓',`${((Number(n.cost)-Number(s.cost))/Number(n.cost)*100).toFixed(1)}% vs NearCost`)
 ].join('');
 document.getElementById('overall-chart').innerHTML='<h4>Known-prevalence L1</h4>'+bars(overall,'beta_l1');
 document.getElementById('router-artifacts').innerHTML=`<table class="data-table"><thead><tr><th>Stage</th><th>Fallback</th><th>Transparent HealthRule</th><th>Safe threshold</th></tr></thead><tbody>${Object.entries(routers).map(([k,v])=>`<tr><td>${k}</td><td>${v.fallback}</td><td>${v.health_rule}</td><td>${v.safe_threshold}</td></tr>`).join('')}</tbody></table>`;
 const splits=[...new Set(abl.map(x=>x.split))];
 document.getElementById('ablation-cards').innerHTML=splits.map(sp=>{const rs=abl.filter(x=>x.split===sp);return `<div class="ab-card"><h3>${sp}</h3>${rs.map(r=>`<div class="step"><strong>${r.policy}</strong><span>β ${fmt(r.beta_l1,4)}</span><span>F1 ${fmt(r.macro_f1,4)}</span><span>cost ${Number(r.mean_cost).toFixed(1)}</span></div>`).join('')}</div>`}).join('');
 document.getElementById('module-chart').innerHTML=mods.filter(x=>x.split==='seen').map(r=>`<div class="bar-row"><div class="bar-label">${r.stage}</div><div class="bar-track"><div class="bar-fill" style="width:${r.greedy_capture_pct}%"></div></div><div class="bar-value">${r.greedy_capture_pct}%</div></div>`).join('');
 document.getElementById('module-table').innerHTML=`<table class="data-table"><thead><tr><th>Stage</th><th>Split</th><th>Fallback</th><th>HealthRule</th><th>Greedy</th><th>Safe</th><th>Oracle</th><th>Capture</th></tr></thead><tbody>${mods.map(r=>`<tr><td>${r.stage}</td><td>${r.split}</td><td>${r.fallback}</td><td>${r.health_rule}</td><td>${r.greedy}</td><td>${r.safe}</td><td>${r.oracle}</td><td class="capture">${r.greedy_capture_pct}%</td></tr>`).join('')}</tbody></table>`;
 document.getElementById('external-cards').innerHTML=external.map(r=>`<div class="ext-card"><div class="small">${r.dataset} · ${r.policy}</div><div class="big">${fmt(r.beta_auc,4)}</div><div>β utility AUC</div><div class="small" style="margin-top:8px">F1 AUC ${fmt(r.f1_auc,4)} · ${r.rank_note}</div></div>`).join('');
 document.getElementById('trace-list').innerHTML=trace.steps.map(x=>`<div class="trace-item"><div class="trace-index">${x.step}</div><div class="trace-card"><h3>${x.action}${x.selected?` · ${x.selected}`:''}</h3><p>${x.diagnosis}</p><div class="chips">${Object.entries(x.evidence).map(([k,v])=>`<span class="chip">${k}: ${v}</span>`).join('')}<span class="chip action">action: ${x.action}</span><span class="chip ok">${x.status}</span></div></div></div>`).join('');
 document.getElementById('supported').innerHTML=scope.supported.map(x=>`<li>${x}</li>`).join('');
 document.getElementById('unsupported').innerHTML=scope.not_established.map(x=>`<li>${x}</li>`).join('');
 document.getElementById('openworld').innerHTML=`<div class="open-grid"><div class="open-stat"><div class="num">${(open.open_probability.increase_pair_fraction*100).toFixed(1)}%</div><div>matched pairs with higher open probability</div><small>mean ${open.open_probability.negative_mean} → ${open.open_probability.positive_mean}</small></div><div class="open-stat"><div class="num">${(open.rho_hat.increase_pair_fraction*100).toFixed(1)}%</div><div>matched pairs with higher ρ̂</div><small>mean ${open.rho_hat.negative_mean} → ${open.rho_hat.positive_mean}</small></div></div><p style="color:var(--muted)">${open.claim}</p>`;
})();
