import pandas

data = pandas.read_csv("weather_data.csv")
#print(type(data))
#print(type(data['temp']))

data_dict = data.to_dict()
#print(data_dict)

data_list_temp = data['temp'].to_list()
#print(data_list_temp)

#get the average
#print(data['temp'].mean())
#get the max
#print(data['temp'].max())

# get a row
# this is like select where day == Monday
#print(data[data.day == "Monday"])

# which row of data where temp was max
#print(data[data.temp == data.temp.max()])

# Monday temp in FarenHeight
#monday  = data[data.day == "Monday"]
#print(int(monday.temp) * (9/5) + 32)


