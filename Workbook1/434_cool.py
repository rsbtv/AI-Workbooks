import matplotlib
from matplotlib import pyplot as plt
import yfinance as yf

matplotlib.use('TkAgg')

# company = str(input("Введите название компании: "))
# year = str(input("Введите год: "))
# data = yf.download(company, start=f"{year}-01-01", end=f"{year}-12-31", interval="1mo")
data_aapl = yf.download("AAPL", start="2021-01-01", end="2021-12-31", interval="1mo")
data_msft = yf.download("MSFT", start="2021-01-01", end="2021-12-31", interval="1mo")
data_goog = yf.download("GOOG", start="2021-01-01", end="2021-12-31", interval="1mo")

plt.plot(range(1, 13), data_aapl['Open'])
plt.grid()

fig = plt.figure(figsize=(8, 4))
plt.plot(range(1, 13), data_msft['Open'])
plt.grid()

fig2 = plt.figure(figsize=(8, 4))
plt.plot(range(1, 13), data_goog['Open'])
# plt.plot(range(1, 13), data['Open'])
plt.grid()
plt.show()
