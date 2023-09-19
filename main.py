from tkinter import *
from PIL import Image, ImageTk
import pandas
is_on = True

#Window
root = Tk()
root.title("Guess the Country")
root.minsize(width=700, height=700)
image = Image.open("Africa.png")
resized_image = image.resize((700, 700))
bg = ImageTk.PhotoImage(resized_image)
label_1 = Label(root, image=bg)
label_1.place(x=0, y=0)

#Pandas
data = pandas.read_csv("african_countries.csv")
all_countries = data.country.to_list()
guessed_countries = []
countries_to_learn = []
df = pandas.DataFrame(data)

def check_answer():
    global info
    answer = answer_country.get().title()
    if answer in all_countries and answer not in guessed_countries:
        guessed_countries.append(answer)
        info.config(text=f"Correct! {len(guessed_countries)}/52 Countries Correct")
        country_data = data[data.country == answer]
        country_label = Label(text=f"{answer}", font=("TkDefaultFont",6))
        country_label.place(x=int(country_data.x), y=int(country_data.y))
    elif answer in guessed_countries:
        info.config(text=f"You have already guessed this. {len(guessed_countries)}/52")
    elif answer not in all_countries:
        info.config(text=f"Wrong. Try again. {len(guessed_countries)}/52 Correct")
    answer_country.delete(0, END)

#Canvas surround
canvas_1 = Canvas(root, width=240, height=150)
canvas_1.place(x=90, y=430)

#Guess label
guess = Label(text="Guess a country:")
guess.place(x=140, y=465)

#Info label
info = Label(text="0/52 Countries Correct")
info.place(x=130, y=440)

#Guess button
guess_button = Button(text="Guess", command=check_answer)
guess_button.place(x=150, y=520)

#Quit button
quit_button = Button(text="Quit", command=root.destroy)
quit_button.place(x=200, y=520)

answer_country = Entry()
answer_country.place(x=130, y=490)

if len(guessed_countries) == 52:
    info.config(text=f"You win!")

root.mainloop()