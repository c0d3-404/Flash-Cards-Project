from msilib.schema import Icon
from customtkinter import *
from CTkMessagebox import CTkMessagebox
from funcs import *


def Run(tk):
    # starts the question sequence
    Qselection = randint(0, len(information)-1)
    loading_window(tk, ArrayValue=Qselection)
    start_timer()


def loading_window(tk, Qnum=1, ArrayValue=0):
    msg = CTkMessagebox(title="Continue?", message="The quiz starts immediately.\n Do you want to continue?",
                        icon="question", option_1="No", option_2="Yes")
    response = msg.get()

    if response == "Yes":
        question_widow(tk, Qnum, ArrayValue)
    else:
        Menu()


def question_widow(tk, Qnum=1, ArrayValue=0):
    # makes the question window
    hide(tk)
    Quiz = CTkToplevel()
    Quiz.geometry("500x400")
    Quiz.iconbitmap("icons/icon.ico", "icons/icon.ico")
    Quiz.title(f"F.C.Q")

    Title = CTkLabel(master=Quiz, text=f"Question {Qnum}",
                     font=("Arial", 20))
    Title.place(relx=0.5, rely=0.05, anchor="center")
    question = CTkLabel(master=Quiz, text=information[ArrayValue][0],
                        font=("Arial", 15)).place(relx=0.5, rely=0.15, anchor="center")
    Abutton1 = CTkButton(master=Quiz, text="AB1", command=lambda: Answer_Buttons(
        1, Abutton1.cget("text"), Abutton2.cget("text"), Abutton3.cget("text"), ArrayValue))
    Abutton1.place(relx=0.5, rely=0.3, anchor="center")

    Abutton2 = CTkButton(master=Quiz, text="AB2", command=lambda: Answer_Buttons(
        2, Abutton1.cget("text"), Abutton2.cget("text"), Abutton3.cget("text"), ArrayValue))
    Abutton2.place(relx=0.5, rely=0.4, anchor="center")

    Abutton3 = CTkButton(master=Quiz, text="AB3", command=lambda: Answer_Buttons(
        3, Abutton1.cget("text"), Abutton2.cget("text"), Abutton3.cget("text"), ArrayValue))
    Abutton3.place(relx=0.5, rely=0.5, anchor="center")

    ExitBtn = CTkButton(master=Quiz, text="Exit",
                        fg_color="#FF0000", text_color="#000000", command=lambda: Menu(Quiz)).place(relx=0.5, rely=0.7, anchor="center")


def hide(tk):
    # hides window
    try:
        tk.withdraw()
    except:
        pass


def show(tk):
    # shows window
    tk.deiconify()


def Answer_Buttons(Buttton_Num, AB1Text, AB2Text, AB3Text, question):
    match Buttton_Num:
        case 1:
            print(AB1Text, AB2Text, AB3Text, )
        case 2:
            print(AB2Text, AB3Text, AB1Text)
        case 3:
            print(AB3Text, AB1Text, AB2Text)
        case _:
            pass


app = None


def Menu(tk=None):
    global app
    # makes app unless app is made then it reveals it.
    if app == None:
        app = CTk()
        app.geometry("500x400")
        app.iconbitmap("icon.ico", "icons/icon.ico")
        app.title("Menu")
        set_appearance_mode("dark")
        Title = CTkLabel(master=app, text="Flash Card Project",
                         font=("Arial", 40))
        PlayBtn = CTkButton(master=app, text="Start",
                            fg_color="#00FF00", text_color="#000000", command=lambda: Run(app))
        Changebtn = CTkButton(master=app, text="Change File",
                              fg_color="#AA4203", text_color="#000000", command=changeFile)
        ExitBtn = CTkButton(master=app, text="Exit",
                            fg_color="#FF0000", text_color="#000000", command=app.quit)
        Title.place(relx=0.5, rely=0.05, anchor="center")
        PlayBtn.place(relx=0.5, rely=0.4, anchor="center")
        Changebtn.place(relx=0.5, rely=0.5, anchor="center")
        ExitBtn.place(relx=0.5, rely=0.6, anchor="center")
        app.mainloop()
        exit()
    else:
        show(app)
        try:
            tk.destroy()
        except:
            pass
