def func():
    import pickle
    file = "articles.pkl"
    fileobj1 = open(file, "rb")
    articles = pickle.load(fileobj1)
    return articles
