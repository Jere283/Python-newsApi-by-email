import requests
from sendEmail import send_email

api_key = "2936c0219d97405c86acb1d1bf213919"
url = "https://newsapi.org/v2/top-headlines?" \
      "category=technology&language=en&sortBy=popularity&pageSize=30" \
      "&apiKey=2936c0219d97405c86acb1d1bf213919"

requests = requests.get(url)
content = requests.json()

body = "Subject: Today's news" + "\n"
for article in content['articles'][:20]:
      if article['title'] and article["description"] is not None:
            body = body + article['title'] + "\n" + article["description"] + "\n" +\
                  article['url'] + 2*"\n"

print(body)

body = body.encode("utf-8")
send_email(body)


