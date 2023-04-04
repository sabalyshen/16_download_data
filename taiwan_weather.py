import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'C0F9N0-2022-01.csv'
with open(filename, 'r', encoding="utf-8") as f:
    reader = csv.reader(f)
    header_row = next(reader)
    header_row = next(reader)
    
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[4], "%Y-%m-%d %H:%M")
        dates.append(current_date)
        high = float(row[8])
        highs.append(high)
        
        low = float(row[10])
        lows.append(low)
    
    #根據數據繪製圖形
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c='r', alpha=0.5)
    plt.plot(dates, lows, c='b', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='b', alpha=0.1)
    plt.plot(dates, highs, c='r')
    plt.plot(dates, lows, c='b')
    
    #設置圖形的格式
    plt.title("Daily high temperature, January 2022, Taiwan ", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (C)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    
    plt.show()