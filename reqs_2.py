import requests
import json

url = 'http://localhost:8080/'
headers = {'Content-type': 'application/json',  # Определение типа данных
           'Accept': 'text/plain',
           'Content-Encoding': 'utf-8'}
data = [
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
  },
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

answer = requests.post(url, data=json.dumps(data), headers=headers)
print(answer)