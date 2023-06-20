import matplotlib.pyplot as plt
import random
import pandas as pd

years = [2010, 2011, 2012, 2013, 2014, 2015]
countries = ['США', 'Китай', 'Россия']

for country in countries:
    data = {country: [random.randint(100, 500) for i in range(len(years))] for country in countries}
plt.figure(figsize=(10, 6))

for country in countries:
    plt.plot(years, data[country], label=country)

plt.grid(True)
plt.xlabel('Год')
plt.ylabel('Объем торговли')
plt.title('Объемы торговли стран')
plt.legend()

plt.savefig('trade_volume.png')