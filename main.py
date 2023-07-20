from optparse import OptionParser

import matplotlib.pyplot as plt
import pandas


def main():
    parser = OptionParser()
    (_, args) = parser.parse_args()
    filename, = args

    data = pandas.read_csv(filename)
    temps = data[data['NAME'].str.contains('REXBURG')][['DATE', 'TMAX', 'TMIN']]
    temps['DATE'] = pandas.to_datetime(temps['DATE'])
    start_date = temps['DATE'].min().date()
    end_date = temps['DATE'].max().date()

    temps['YEAR'] = temps['DATE'].dt.year
    temps['MONTH'] = temps['DATE'].dt.month
    temps['DAY'] = temps['DATE'].dt.day
    day_groups = temps.groupby(['MONTH', 'DAY'])

    record_highs = day_groups['TMAX'].max()
    min_high_temps = day_groups['TMAX'].min()

    record_lows = day_groups['TMIN'].min()
    max_low_temps = day_groups['TMIN'].max()

    plt.figure(figsize=(19.2, 10.8))
    plt.title(f'Rexburg, ID Temperatures ({start_date} to {end_date})', fontsize=32)
    record_highs.plot(label='Record Highs')
    min_high_temps.plot(label='Minimum Highs')
    max_low_temps.plot(label='Maximum Lows')
    record_lows.plot(label='Record Lows')
    plt.legend(prop={'size': 16})
    plt.savefig('climate.png')


if __name__ == '__main__':
    main()
