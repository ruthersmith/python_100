import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_Squirrel_Data.csv")
new_data = data["Primary Fur Color"].groupby(data["Primary Fur Color"]).count()

data_dict = {
    "Fur Color" : list(new_data.to_dict().keys()),
    "Count" :list(new_data.to_dict().values())
}
pandas.DataFrame(data_dict).to_csv('squirrel_count.csv')
