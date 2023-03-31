import csv
from matplotlib import pyplot as plt

filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for index, column_header in enumerate(header_row):
        print(index, column_header)
    #讀取每日最高溫    
    highs = []
    for row in reader:
        high = int(row[1])
        highs.append(high)
        
#根據數據繪製圖形    