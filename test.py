import requests

data = {"data": ["1","3", 2, 5, 4.0, 6.0], "operator":["sum", "mean", "min", "max", "range", "variance", "stddev"]}
res = requests.post(url = "http://127.0.0.1:8080/Statistics/reduce", json = data)
print(res.text)