from sklearn.metrics import f1_score, accuracy_score

def classification_metrics(y_true,y_pred):
    mask=y_true>=0
    return {'accuracy':float(accuracy_score(y_true[mask],y_pred[mask])),
            'macro_f1':float(f1_score(y_true[mask],y_pred[mask],average='macro'))}
