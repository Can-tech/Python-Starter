import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S.  States Game")
image= r"us-states-game\blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv(r"us-states-game\50_states.csv")
all_states = data.state.to_list()

guest_states=[]

while len(guest_states) < 50:
    answer_state = screen.textinput(title=f"{len(guest_states)}/50", 
                                    prompt="State Name: ? ").title()
    if answer_state == "Exit":
        break
    if answer_state in all_states:
        guest_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
remaining_states=[]
for state in all_states:
    if state not in guest_states:
        remaining_states.append(state)
new_data=pandas.DataFrame(remaining_states)
new_data.to_csv("us-states-game/forgotten_states.csv")

# data = pandas.read_csv(r"us-states-game\50_states.csv")

# state_name_data=0
# state_left=len(data)
# while state_left>0:
#     answer_state = screen.textinput(title="Guess", prompt="State Name: ? ")
#     chosen_row = data[data['state']==(answer_state)]
#     if not chosen_row.empty:
#         print(chosen_row)
#         turtle.write(chosen_row["state"],align=(chosen_row["x"],chosen_row["y"]))
#         state_left-=1
# print(state_left)











# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
