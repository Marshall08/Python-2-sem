import pandas as pd
import random
import requests
import csv

length = 20
titles = ['id', 'salary', 'month', 'name']
id = [str(random.randint(0, 99999)) for _ in range(length)]
salary = [str(random.randint(100000, 999999)) for _ in range(length)]
months = [str(random.randint(1, 12)) for _ in range(length)]
url = "https://randomuser.me/api/"
params = {'results': length}
response = requests.get(url, params=params)
data = response.json()
users = list(map(lambda x: x['name']['title'] + '.' + ' ' + x['name']['first'] + ' ' + x['name']['last'], data['results']))

data = zip(id, salary, months, users)
data_users = [titles] + list(data)
with open('data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(data_users[0])
    for row in data_users[1:]:
        writer.writerow(row)

df = pd.read_csv('data.csv')
res = df['salary'].mean()
print(res)