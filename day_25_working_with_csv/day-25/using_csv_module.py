# in this way of doing data would be a list of string where each string is a line
# with open("weather_data.csv") as file:
#     data = file.readlines()
# print(data)

# built in module that helps with csv
import csv

with open("weather_data.csv") as file:
    data = csv.reader(file)  # reads as csv
    temperatures = []
    for row in data:
        try:
            temperatures.append(int(row[1]))
        except ValueError:
            print("value error on this row")
            print(row)
    print(temperatures)