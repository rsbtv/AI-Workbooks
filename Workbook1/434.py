import csv
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')


# Получение 12 средних цен акции за 2022 год
def get_opens(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        open_indx = header_row.index('Open')
        opens = []
        for row in reader:
            open_price = float(row[open_indx])
            opens.append(open_price)
    return opens


# Отображение графиков для Apple, Microsoft, Google
plt.plot(range(1, 13), get_opens('data/AAPL.csv'))
plt.grid()

fig = plt.figure(figsize=(8, 4))
plt.plot(range(1, 13), get_opens('data/MSFT.csv'))
plt.grid()

fig2 = plt.figure(figsize=(8, 4))
plt.plot(range(1, 13), get_opens('data/GOOG.csv'))
plt.grid()

plt.show()
