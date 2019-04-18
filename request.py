from urllib.parse import urlencode
from urllib.request import Request, urlopen
import json

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

#print(dict([('1',i)] for i in test_data))
prep=[]
for i in range(len(test_data)):
    prep = prep+[', '.join("{!s}={!r}".format(key,val) for (key,val) in test_data[i].items())]

print(prep)
d={str(i):prep[i] for i in range(len(prep))}

d=json.dumps(d)
print(d,type(d))

"""
j=0
for i in test_data:
    req = dict([(j,json.dumps(i, separators=(',',':')))])
    j+=1

print(req,type(req))
"""

url = 'http://localhost:8080/' # URL

def test_1(test_data):
    for i in test_data:
        print(i)
        post_fields = i   # POST

        request = Request(url, urlencode(post_fields).encode())
        json = urlopen(request).read().decode()

        print(json)

def test_2(test_data):
    post_fields = test_data  # POST

    request = Request(url, urlencode(post_fields).encode())
    print(post_fields, type(post_fields))
    json = urlopen(request).read().decode()

    print(json)

test_2(d)

#test_1(test_data)