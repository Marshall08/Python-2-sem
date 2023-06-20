import pandas as pd

data = pd.read_csv('data.csv')
data['date'] = pd.to_datetime(data['date'])
data_january = data.loc[data['date'].dt.month == 1]
data_day = data_january[data_january['date'].dt.day == 1]

print ('Task 1')

non0= len(data_day[data_day['order_price'] != 0])
print("Ненулевые заказы за 1 января: ", non0)
print()

print ('Task 2')

total = len(data_day)
print("Заказы за 1 января: ", total)
zero = len(data_day[data_day['order_price'] == 0])
print("Нулевые заказы за 1 января: ", zero)
percent = zero / total * 100
print("Процент нулевых заказов за 1 января: ", round(percent, 1), "%")
print()

print ('Task 3')

zero = data.loc[data['order_price'] == 0, 'date'].dt.date.unique()
print("Дни с нулевыми заказами: ", zero)
print()

print ('Task 4')

orders = data.groupby('uid')['order_id'].count()
top = orders.nlargest(100)
print(top)
print()

print ('Task 5')

orders = data[data['cutlery'] > 0]
users = orders.groupby('uid')['cutlery'].count()
topten = users.sort_values(ascending=False).head(10)
print(topten)
print()

print ('Task 6')

orders = data[data['tips'] > 0]
user = orders.groupby('uid')['tips'].sum()
users = user.sort_values(ascending=False).head(20)
print(users)
print()

print ('Task 7')

days = data.groupby('date')['tips'].sum()
top = days.sort_values(ascending=False).head(20)
print(top)
print()

print ('Task 8')

total = data[data['cutlery'] > 0]
num = total['cutlery'].unique()
print("Количество популярных столовых приборов:", num)
print()

print ('Task 9')

num = data['uid'].nunique()
print("Количество уникальных пользователей:", num)
print()

### Task 10
### Task 11
### Task 12
