#ENERGY INSIGHTS CLI 
A python CLI tool that analyzes energy prize data from a CSV file

From week1day4 folder,tun : cd week1day4

input CSV file is located at:  ../data/energy/hourly_prices.csv 

Usage - Run the CLI with command

 python week1day4/energy_insights/__main__.py --file="data/energy/hourly_prices.csv" 

 -- file - path to csv file
 --metric - number of columns to analyze
 --top - number of top price spikes to display

 SAMPLE OUPUT - python week1day4/energy_insights/__main__.py --file="data/energy/hourly_prices.csv" 

 Daily Averages:
Date:         Avg Price:
2025-09-30    $49.52

Top 10 Price Spikes:
2025-09-30T17:00:00Z $63.90
2025-09-30T07:00:00Z $61.00
2025-09-30T16:00:00Z $60.20
2025-09-30T18:00:00Z $59.70
2025-09-30T08:00:00Z $58.50
2025-09-30T15:00:00Z $57.40
2025-09-30T09:00:00Z $55.10
2025-09-30T19:00:00Z $54.00
2025-09-30T06:00:00Z $52.20
2025-09-30T14:00:00Z $50.80

Anamoly Detetction:
Anamolies detected: 2 hours
2025-09-30T14:00:00Z(95th percentile threshold): 61.0


