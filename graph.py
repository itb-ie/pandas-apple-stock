from matplotlib import pylab as plt
import pandas as pd

# pd.plotting.register_matplotlib_converters()

df1 = pd.read_csv("AAPL.csv")
print(df1.head())
df1['Date'] = pd.to_datetime(df1.Date)

df2 = pd.read_excel("iphone-dates-2019.xlsx")
print(df2)
df2['Date'] = pd.to_datetime(df2.date)

index2 = []
for date2 in df2.Date:
    if df1.index[df1.Date == date2].values.size:
        index2.append(int(df1.index[df1.Date == date2].values[0]))
    elif df1.index[df1.Date == date2 + pd.DateOffset(1)].values.size:
        index2.append(int(df1.index[df1.Date == date2 + pd.DateOffset(1)].values[0]))
    elif df1.index[df1.Date == date2 + pd.DateOffset(2)].values.size:
        index2.append(int(df1.index[df1.Date == date2 + pd.DateOffset(2)].values[0]))

    else:
        print(f"Did not find {date2}")

print(index2, len(index2))


mean = df1["Close"].mean()


plt.figure("Apple Stock")
plt.plot(df1["Date"], df1["Close"], 'r-', linewidth=0.6, label="APPL Stock price, mean="+str(mean))
# or the same can be:
# plt.plot("Date", "Close", 'r-', linewidth=0.6, label="APPL Stock price, mean="+str(mean), data=df1)
plt.plot(df1["Date"], df1["Close"], 'o', ms=7, markevery=index2, label="Iphone launch date")
plt.xlabel("Dates")
plt.legend(loc="upper left")

plt.show()
