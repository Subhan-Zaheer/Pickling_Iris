import pickle
import requests
import json
import unpicklingfunc
url = "https://newsapi.org/v2/top-headlines?q=cricket&from=2022-07-15&to=2022-07-15&sortBy=popularity&apiKey=a23441b217ed489b8350cf8ca4ba317f"
text1 = requests.get(url).text
print(text1)
print(type(text1))
parsedText_here = json.loads(text1)
articles = parsedText_here['articles']
file = "articles.pkl"
fileobj = open(file, "wb")
ls = []
for items in articles:
    ls.append(items)

print(ls)
pickle.dump(ls, fileobj)
fileobj.close()
articles1 = unpicklingfunc.func()
print(articles1)