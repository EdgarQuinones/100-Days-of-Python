import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. GAME")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data["state"]

all_states = [
    "alabama", "alaska", "arizona", "arkansas", "california", "colorado",
    "connecticut", "delaware", "florida", "georgia", "hawaii", "idaho",
    "illinois", "indiana", "iowa", "kansas", "kentucky", "louisiana",
    "maine", "maryland", "massachusetts", "michigan", "minnesota",
    "mississippi", "missouri", "montana", "nebraska", "nevada",
    "new hampshire", "new jersey", "new mexico", "new york",
    "north carolina", "north dakota", "ohio", "oklahoma", "oregon",
    "pennsylvania", "rhode island", "south carolina", "south dakota",
    "tennessee", "texas", "utah", "vermont", "virginia", "washington",
    "west virginia", "wisconsin", "wyoming"
]

guessed_states = []
states_correct = 0
game_over = False
while not game_over:
    answer_state = screen.textinput(title=f"States Correct {states_correct}/50", prompt="What's another state's name")

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("Missing_States.csv")
        game_over = True
        break

    for index in range(len(states)):
        if answer_state.lower() == states[index].lower():
            print("That state is in it")
            states_correct += 1
            state_x = data["x"][index]
            state_y = data["y"][index]
            guessed_states.append(answer_state)
            state_text = turtle.Turtle()
            state_text.hideturtle()
            state_text.penup()
            state_text.goto(state_x, state_y)
            state_text.write(states[index])

            break

screen.exitonclick()
