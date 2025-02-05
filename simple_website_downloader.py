import requests

url = input("Enter URL: ")
x = requests.get(url)

print(x.text)
f = open("site.html", "w")
f.write(x.text)
