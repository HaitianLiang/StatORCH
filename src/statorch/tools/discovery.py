import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

def kmeans_discovery(x, n_clusters, seed=0):
    x=np.asarray(x,float)
    if len(x)<n_clusters: raise ValueError('Need at least n_clusters samples')
    labels=KMeans(n_clusters=n_clusters,n_init=10,random_state=seed).fit_predict(x)
    sil=float(silhouette_score(x,labels)) if n_clusters>1 and len(set(labels))>1 else float('nan')
    return {'labels':labels,'silhouette':sil}
