from tkinter import *
from PIL import Image, ImageTk
import random

# main window
root = Tk()
root.title("Rock Paper Scissors")
root.configure(background="black")

# pictures
rock_image = ImageTk.PhotoImage(Image.open("rock.jpeg"))
paper_image = ImageTk.PhotoImage(Image.open("paper.jpeg"))
scissor_image = ImageTk.PhotoImage(Image.open("scissors.jpeg"))

# insert pictures
userlabel = Label(root, image=rock_image, bg="black")
userlabel.grid(row=1, column=30)

comp_label = Label(root, image=rock_image, bg="black")  # Default image for computer
comp_label.grid(row=1, column=0)

# scores
user_score = 0
computer_score = 0
playscore = Label(root, text=user_score, font=20, bg="black", fg="white")
playscore.grid(row=1, column=1)
computerscore = Label(root, text=computer_score, font=20, bg="black", fg="white")
computerscore.grid(row=1, column=3)

# INDICATORS
user_indicator = Label(root, font=('arial', 20, 'bold'), text="USER", bg="black", fg="white")
user_indicator.grid(row=0, column=3)
comp_indicator = Label(root, font=('arial', 20, 'bold'), text="COMPUTER", bg="black", fg="white")
comp_indicator.grid(row=0, column=1)

# messages
msg = Label(root, font=50, bg="black", fg="white", text=" ")
msg.grid(row=3, column=2)

# update choices
def updatechoice(x):
    global user_score, computer_score
    
    # Update user choice
    if x == "rock":
        userlabel.configure(image=rock_image)
    elif x == "paper":
        userlabel.configure(image=paper_image)
    else:
        userlabel.configure(image=scissor_image)

    # Randomly select computer's choice
    computer_choice = random.choice(["rock", "paper", "scissor"])
    if computer_choice == "rock":
        comp_label.configure(image=rock_image)
    elif computer_choice == "paper":
        comp_label.configure(image=paper_image)
    else:
        comp_label.configure(image=scissor_image)

    # Determine the winner
    if x == computer_choice:
        msg.configure(text="It's a Tie!")
    elif (x == "rock" and computer_choice == "scissor") or \
         (x == "paper" and computer_choice == "rock") or \
         (x == "scissor" and computer_choice == "paper"):
        user_score += 1
        msg.configure(text="You Win!")
    else:
        computer_score += 1
        msg.configure(text="Computer Wins!")

    # Update scores
    playscore.configure(text=user_score)
    computerscore.configure(text=computer_score)

# reset function
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    playscore.configure(text=user_score)
    computerscore.configure(text=computer_score)
    msg.configure(text=" ")
    userlabel.configure(image=rock_image)  # Reset user choice to default
    comp_label.configure(image=rock_image)  # Reset computer choice to default

# buttons
rock = Button(root, width=20, height=2, text="ROCK", bg="yellow", fg="black", command=lambda: updatechoice('rock'))
rock.grid(row=2, column=1)

paper = Button(root, width=20, height=2, text="PAPER", bg="blue", fg="black", command=lambda: updatechoice('paper'))
paper.grid(row=2, column=2)

scissor = Button(root, width=20, height=2, text="SCISSOR", bg="#0ABDE3", fg="black", command=lambda: updatechoice('scissor'))
scissor.grid(row=2, column=3)

# Reset button
reset_button = Button(root, width=20, height=2, text="RESET", bg="red", fg="black", command=reset_game)
reset_button.grid(row=2, column=4)

root.mainloop()
