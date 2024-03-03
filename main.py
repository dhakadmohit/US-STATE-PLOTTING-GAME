import pandas as pd
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "D:/Python VS CODE/day-25-us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


df = pd.read_csv("D:\Python VS CODE/day-25-us-states-game-start/50_states.csv")
all_state = df["state"].to_list()
Gussed_state = []


while len(Gussed_state) < 50:

    answer_state = screen.textinput(title= f"{len(Gussed_state)}/50 states", 
                                    prompt="What's the another state's name ? ")
    answer_state = answer_state.capitalize()

    if answer_state == "Exit":
        missing_state = []
        for state in all_state:
            if state  not in Gussed_state:
                missing_state.append(state)
        new_data = pd.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_state:
        Gussed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        data_state = df[df["state"] == answer_state]
        t.goto(int(data_state['x']),int(data_state['y']))
        t.write(answer_state)

screen.exitonclick()

