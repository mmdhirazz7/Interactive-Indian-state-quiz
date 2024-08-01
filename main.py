import turtle  # Import the turtle module for graphical representation
import pandas  # Import the pandas module for handling CSV data

# Set up the screen
screen = turtle.Screen()
screen.title("Indian - states - Game")
image = "India-state.gif"
screen.addshape(image)
turtle.shape(image)

# Read the CSV file containing state data
data = pandas.read_csv("indian-states.csv")
total_states = len(data.state)
all_states = data.state.to_list()

score = 0
correct_guesses = []

# Main game loop
while score < total_states:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/29 states Correct",
                                    prompt="What's another state's name?").title()
    
    if answer_state in correct_guesses:
        continue
    if answer_state == "Exit":
        break
    if answer_state in all_states:
        state_data = data[data.state == answer_state]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_data.x), int(state_data.y))
        t.pendown()
        t.write(f"{state_data.state.item()}", align="center", font=("Arial", 8, "normal"))
        correct_guesses.append(answer_state)
        score += 1

# Remove correctly guessed states from the list of all states
for state in correct_guesses:
    all_states.remove(state)

# Create a new DataFrame with the states to learn and save to CSV
data_dict = {"states": all_states}
new_data = pandas.DataFrame(data_dict)
new_data.to_csv("states_to_learn.csv")

# Uncomment the following code to get the coordinates of a particular point on the screen
# def mouse_on_click(x, y):
#     print(x, y)
# turtle.onscreenclick(mouse_on_click)
# turtle.mainloop()

screen.exitonclick()
