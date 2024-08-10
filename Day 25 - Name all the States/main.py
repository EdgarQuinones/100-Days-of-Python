import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. GAME")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data["state"]

states_correct = 0
game_over = False
while not game_over:
    answer_state = screen.textinput(title=f"States Correct {states_correct}/50", prompt="What's another state's name")

    for index in range(len(states)):
        if answer_state.lower() == states[index].lower():
            print("That state is in it")
            states_correct += 1
            state_x = data["x"][index]
            state_y = data["y"][index]

            state_text = turtle.Turtle()
            state_text.hideturtle()
            state_text.penup()
            state_text.goto(state_x, state_y)
            state_text.write(states[index])

            break

screen.exitonclick()
