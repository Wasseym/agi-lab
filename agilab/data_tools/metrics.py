def accuracy(preds, labels):
    return sum(int(p==l) for p,l in zip(preds,labels))/max(1,len(labels))
