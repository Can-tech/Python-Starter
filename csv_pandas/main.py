import math

# with open("./csv_pandas/weather_data.csv") as file:
#     data=file.readlines()
# print(data)

# import csv

# with open("./csv_pandas/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures=[]
#     for index,row in enumerate(data):
#         if index == 0:
#             continue
#         temperatures.append(int (row[1]))
# print(temperatures)

import pandas

# # # data = pandas.read_csv("./csv_pandas/weather_data.csv")
# # # # print(type(data))
# # # # print(data["temp"])

# # # data_dict = data.to_dict()
# # # print(data_dict)

# # # temp_list = data["temp"].to_list()
# # # print(len(temp_list))

##########
#average = sum(temp_list)/len(temp_list)
#print(average)

# print(data["temp"].mean())
# print(" Max sıcaklık ",data["temp"].max())
# ##########

# ##Get Data Columns
# print(data["condition"])
# print(data.condition)

########Get Data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp==data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_f = monday_temp * 9/5+32
# print(monday_temp_f)

#########Create a dataFrame from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76,56,65]
# }
# data = pandas.DataFrame(data_dict)
####CREATE CSV CONVERT CSV
# data.to_csv("new_data.csv")

data = pandas.read_csv("csv_pandas\CenPark_Squirrel_Data.csv")
print(data)
squirrell_col=data["Primary Fur Color"]
print(squirrell_col.value_counts())#Counts the unique elements
df = pandas.DataFrame(squirrell_col.value_counts())
df.to_csv("csv_pandas\squirrel_count.csv")


