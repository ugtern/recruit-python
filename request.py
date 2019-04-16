from urllib.parse import urlencode
from urllib.request import Request, urlopen

test_data = [
  {
    "time": 1551179712,
    "sender": "i.petrov",
    "message": "Раз-два, проверка связи"
  },
  {
    "time": 1551179749,
    "sender": "m.vasiljeva",
    "message": "Проверка пройдена, всё работает"
  },
  {
    "time": 1551179831,
    "sender": "i.petrov",
    "message": "Отлично"
  }
]

url = 'http://localhost:8080/' # URL
for i in test_data:
    print(i)
    post_fields = i   # POST

    request = Request(url, urlencode(post_fields).encode())
    json = urlopen(request).read().decode()

    print(json)