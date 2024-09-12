from tkinter import *
from PIL import Image, ImageTk
import Speech_to_text
import action

root = Tk()
root.title("AI ASSISTANT")
root.geometry("450x620")
root.resizable(False, False)
root.config(bg="#6F8FAF")


# ASK Function
def ask():
    print("ask")
    user_val = Speech_to_text.speech_to_text()
    bot_val = action.action(user_val)
    text.insert(END, 'user--->' + user_val + "\n")
    if bot_val != None:
        text.insert(END, "BOT <---" + str(bot_val) + "\n")
    if bot_val == "ok sir":
        root.destroy()


def send():
    send = entry.get()
    bot = action.action(send)
    text.insert(END, 'User--->' + send + "\n")
    if bot != None:
        text.insert(END, "BOT <---" + str(bot) + "\n")
    if bot == "ok sir":
        root.destroy()


def del_text():
    text.delete("1.0", "end")


# Frame
frame = LabelFrame(root, padx=20, pady=1, height=1, width=6, borderwidth=3, relief="raised")
frame.config(bg="#6F8FAF")
frame.grid(row=0, column=1, padx=60, pady=12)

# Text Label
text_label = Label(frame, text="AI ASSISTANT", font=("comic Sans ms", 14, "bold"), bg="#356696")
text_label.grid(row=0, column=0, padx=15, pady=10)

# Image
image = ImageTk.PhotoImage(Image.open("AI_image.png"))
image_label = Label(frame, image=image)
image_label.grid(row=1, column=0, pady=15)

# Adding a text widget
text = Text(root, font='courier 10 bold', bg="#356696")
text.grid(row=2, column=0)
text.place(x=30, y=390, width=390, height=100)

# Entry Widget
entry = Entry(root, justify=CENTER)
entry.place(x=30, y=495, width=390, height=40)

# Button1
Button1 = Button(root, text="ASK", bg="#356696", pady=14, height=2, width=8, borderwidth=3, relief=SOLID, command=ask)
Button1.place(x=30, y=540)

# Button2
Button2 = Button(root, text="SEND", bg="#356696", pady=14, height=2, width=8, borderwidth=3, relief=SOLID, command=send)
Button2.place(x=340, y=540)

# Button3
Button3 = Button(root, text="DELETE", bg="#356696", pady=14, height=2, width=8, borderwidth=3, relief=SOLID,
                 command=del_text)
Button3.place(x=185, y=540)

root.mainloop()
