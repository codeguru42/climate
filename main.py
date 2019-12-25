import pandas

data = pandas.read_csv('1236627.csv')
temps = data[data['NAME'].str.contains('REXBURG')][['DATE', 'TMAX', 'TMIN']]
temps['DATE'] = pandas.to_datetime(temps['DATE'])
print(temps['DATE'].min().date(), 'to', temps['DATE'].max().date())


temps['YEAR'] = temps['DATE'].dt.year
temps['MONTH'] = temps['DATE'].dt.month
temps['DAY'] = temps['DATE'].dt.day
day_groups = temps.groupby(['MONTH', 'DAY'])

min_high_temps = day_groups['TMAX'].min()
print(min_high_temps)

max_low_temps = day_groups['TMIN'].max()
print(max_low_temps)
