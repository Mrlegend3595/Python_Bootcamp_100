import pandas as pd

data = pd.read_csv("2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")

#my_solution
# sq_gray = data[data["Primary Fur Color"] == "Gray"]["Primary Fur Color"].count()
#
# sq_black = data[data["Primary Fur Color"] == "Black"]["Primary Fur Color"].count()
#
# sq_cinnamon = data[data["Primary Fur Color"] == "Cinnamon"]["Primary Fur Color"].count()
#
# output_dict = {
#     "Primary Fur Color": ["Gray", "Black", "Cinnamon"],
#     "Count": [sq_gray, sq_black, sq_cinnamon],
# }
#
# ouput_dataframe = pd.DataFrame(output_dict)
# ouput_dataframe.to_csv("output.csv")


#==========================================================
#Solution

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrel_count],
}


df = pd.DataFrame(data_dict)
df.to_csv("squirrels_count.csv")