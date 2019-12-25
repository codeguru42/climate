import matplotlib.pyplot as plt
import pandas

data = pandas.read_csv('1983182.csv')
temps = data[data['NAME'].str.contains('REXBURG')][['DATE', 'TMAX', 'TMIN']]
temps['DATE'] = pandas.to_datetime(temps['DATE'])
print(temps['DATE'].min().date(), 'to', temps['DATE'].max().date())


temps['YEAR'] = temps['DATE'].dt.year
temps['MONTH'] = temps['DATE'].dt.month
temps['DAY'] = temps['DATE'].dt.day
day_groups = temps.groupby(['MONTH', 'DAY'])

record_highs = day_groups['TMAX'].max()
min_high_temps = day_groups['TMAX'].min()
print(min_high_temps)

record_lows = day_groups['TMIN'].min()
max_low_temps = day_groups['TMIN'].max()
print(max_low_temps)

plt.figure(figsize=(19.2, 10.8))
record_highs.plot(label='Record Highs')
min_high_temps.plot(label='Minimum Highs')
max_low_temps.plot(label='Maximum Lows')
record_lows.plot(label='Record Lows')
plt.legend()
plt.savefig('climate.png')
