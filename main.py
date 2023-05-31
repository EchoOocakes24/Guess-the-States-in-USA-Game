# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()


# Reading a csv file using csv library
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# data_list = data["temp"].to_list()
# average = sum(data_list) / len(data_list)
# print(round(average, 2))

# print(data["temp"].max())

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp
# mond_temp_far = (monday_temp * (9 / 5) + 32)
# print(mond_temp_far)

# import pandas
#
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# gray_color = len(data[data["Primary Fur Color"] == "Gray"])
# red_color = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_color = len(data[data["Primary Fur Color"] == "Black"])
#
# new_data = {
#     "Fur Color": ["gray", "red", "black"],
#     "Count": [gray_color, red_color, black_color]
# }
#
# converted_data = pandas.DataFrame(new_data)
#
# converted_data.to_csv("fur_color.csv")


import turtle
import pandas
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer()

state_guessed_correct = 0
game_is_on = True

data_states = pandas.read_csv("50_states.csv")
states = data_states["state"]
states_list = states.to_list()
guessed_state = []


while len(guessed_state) < 50:
    user_answer = screen.textinput(title=f"{len(guessed_state)} / 50 Guess the State", prompt="Can you guess a State in U.S.?")
    capital_user_answer = user_answer.title()
    states_dict = data_states[data_states["state"] == capital_user_answer]

    if capital_user_answer == "Exit":
        missing_states = []
        # for state in states_list:
        #     if state not in guessed_state:
        #         missing_states.append(state)

        # Solving by using List Comprehension Technique

        missing_states = [state for state in states_list if state not in guessed_state]


        missing_states_dataframe = pd.DataFrame(missing_states)
        missing_states_dataframe.to_csv("states_to_learn.csv")

        break

    if capital_user_answer in states_list:
        guessed_state.append(capital_user_answer)
        new_turtle = turtle.Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        new_turtle.goto(int(states_dict.x), int(states_dict.y))
        new_turtle.write(f"{capital_user_answer}", False, "center", font=('Arial', 8, 'normal'))







