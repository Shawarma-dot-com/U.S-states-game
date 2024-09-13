import turtle
import pandas
import textwrap
screen = turtle.Screen()
screen.title("U.S States game")
image = "blank_states_img.gif"
states = pandas.read_csv("50_states.csv")
screen.addshape(image)
turtle.shape(image)
guessed_states = []


while len(guessed_states) != 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states guessed",
                                    prompt="What's another state name?").title()

    state_names = states.state.to_list()
    if answer_state == "Exit":
        break
    if answer_state in state_names:
        state_names.remove(answer_state)
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = states[states.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)

t = turtle.Turtle()
t.hideturtle()
t.penup()

if len(guessed_states) == 50:

    t.write("Well done you have completed the game!!!\n Click to close", False,
            "Center",("Courier", 30, "normal"))
else:
    t.write("Click to close", False,
            "Center", ("Courier", 30, "normal"))
    print(f"Here are the state names you missed out on {state_names}")
screen.exitonclick()


