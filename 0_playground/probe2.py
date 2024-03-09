def score(cf, *scores) :
    for i in scores:
        print(cf * i)

cf = 0.2
scores = [14, 5, 4]
score(cf, scores)