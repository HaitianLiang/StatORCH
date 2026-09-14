from sklearn.metrics import accuracy_score, f1_score, log_loss

def evaluate_source(model,x,y):
    p=model.predict_proba(x); pred=p.argmax(1)
    return {'accuracy':float(accuracy_score(y,pred)),'macro_f1':float(f1_score(y,pred,average='macro')),'nll':float(log_loss(y,p))}
