import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for index, column_header in enumerate(header_row):
        print(index, column_header)
    #讀取每日最高溫，最低溫及日期    
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            lows.append(low)
            highs.append(high)
        
#根據數據繪製圖形    
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='r', alpha=0.5)
plt.plot(dates, lows, c='b', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='b', alpha=0.1)
plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c='b')
#設置圖形的格式
plt.title("Daily high temperatures, July 2014", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
#設計科度標記大小
plt.tick_params(axis='both', which='major', labelsize=16, color='r')
plt.show()