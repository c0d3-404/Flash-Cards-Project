from funcs import *
from funcs import information as info
from customtkinter import *
from CTkMessagebox import CTkMessagebox

file_name_old = 'keywords.txt'
file_name = './Text/'+file_name_old
correct = 0


def Run(tk):
    # starts the question sequence
    Qselection = randint(0, len(info)-1)
    loading_popup(tk, ArrayValue=Qselection)


def loading_popup(tk, Qnum=1, ArrayValue=0):
    msg = CTkMessagebox(title="Continue?", message="The quiz starts immediately.\n Do you want to continue?",
                        icon="question", option_1="No", option_2="Yes")
    response = msg.get()

    if response == "Yes":
        question_widow(tk, Qnum, ArrayValue)
    else:
        Menu()


def question_widow(tk=None, Qnum=1, ArrayValue=0):
    global correct
    global Quiz
    hide(tk)

    ab1 = str("Empty")
    ab2 = str("Empty")
    ab3 = str("Empty")
    value1 = randint(0, len(info)-1)
    value2 = randint(0, len(info)-1)

    match randint(1, 3):
        case 1:
            ab1 = info[ArrayValue][1]
            while info[value1][1] == info[ArrayValue][1]:
                value1 = randint(0, len(info)-1)
            while info[value2][1] == info[ArrayValue][1] or info[value2][1] == info[value1][1]:
                value2 = randint(0, len(info)-1)
            ab2 = info[value1][1]
            ab3 = info[value2][1]
        case 2:
            ab2 = info[ArrayValue][1]
            while info[value1][1] == info[ArrayValue][1]:
                value1 = randint(0, len(info)-1)
            while info[value2][1] == info[ArrayValue][1] or info[value2][1] == info[value1][1]:
                value2 = randint(0, len(info)-1)
            ab1 = info[value1][1]
            ab3 = info[value2][1]
        case 3:
            ab3 = info[ArrayValue][1]
            while info[value1][1] == info[ArrayValue][1]:
                value1 = randint(0, len(info)-1)
            while info[value2][1] == info[ArrayValue][1] or info[value2][1] == info[value1][1]:
                value2 = randint(0, len(info)-1)
            ab1 = info[value1][1]
            ab2 = info[value2][1]
    if Qnum == 1:
        # makes the question window
        Quiz = CTkToplevel()
        Quiz.geometry("500x400+750+300")
        Quiz.resizable(False, False)
        Quiz.title("F.C.Q")
        start_timer()
        correct = 0
    TimerLabel = CTkLabel(master=Quiz, text=str(
        get_timer()), font=("Arial", 10))
    if Qnum != 1:
        for widgets in Quiz.winfo_children():
            if widgets == TimerLabel:
                continue
            widgets.destroy()
    Quiz.bind("<Escape>", lambda x: sys.exit())
    Title = CTkLabel(master=Quiz, text=f"Question {Qnum}",
                     font=("Arial", 20))
    Title.place(relx=0.5, rely=0.05, anchor="center")

    TimerLabel.place(relx=0.8, rely=0.05, anchor="center")
    question = CTkLabel(master=Quiz, text=info[ArrayValue][0], font=(
        "Arial", 15)).place(relx=0.5, rely=0.15, anchor="center")
    Abutton1 = CTkButton(master=Quiz, text=ab1, command=lambda: Answer_Buttons(
        1, Abutton1, Abutton2, Abutton3, ContBtn, ArrayValue))
    Abutton1.place(relx=0.5, rely=0.3, anchor="center")

    Abutton2 = CTkButton(master=Quiz, text=ab2, command=lambda: Answer_Buttons(
        2, Abutton1, Abutton2, Abutton3, ContBtn, ArrayValue))
    Abutton2.place(relx=0.5, rely=0.4, anchor="center")

    Abutton3 = CTkButton(master=Quiz, text=ab3, command=lambda: Answer_Buttons(
        3, Abutton1, Abutton2, Abutton3, ContBtn, ArrayValue))
    Abutton3.place(relx=0.5, rely=0.5, anchor="center")

    ContBtn = CTkButton(master=Quiz, text="Continue",
                        fg_color="#555555", text_color="#000000", command=lambda: cont(Quiz, Qnum),  state="disabled")
    ContBtn.place(relx=0.5, rely=0.6, anchor="center")
    ExitBtn = CTkButton(master=Quiz, text="Exit",
                        fg_color="#550000", text_color="#000000", command=lambda: Menu(Quiz)).place(relx=0.5, rely=0.7, anchor="center")
    Quiz.after(1000, update, Quiz, TimerLabel)


def update(Quiz, TimerLabel):
    TimeLabel = get_timer()
    try:
        Quiz.after(1000, update, Quiz, TimerLabel)
        TimerLabel.configure(text=str(TimeLabel))
    except:
        pass


def cont(tk, Qnum):
    num = Qnum
    if num >= 9:
        endScreen(tk)
    else:
        num += 1
        question_widow(None, num, randint(0, len(info)-1))


def hide(tk):
    # hides window
    try:
        tk.withdraw()
    except:
        pass


def show(tk):
    # shows window
    tk.deiconify()


def Answer_Buttons(Buttton_Num, AB1, AB2, AB3, ContBtn, question):
    match Buttton_Num:
        case 1:
            global correct
            if AB1.cget("text") == info[question][1]:
                correct += 1
                AB1.configure(fg_color="#005500",
                              hover_color="#005500", text_color="#000000")
                AB2.configure(fg_color=("#550000"),
                              hover_color="#550000", text_color="#000000")
                AB3.configure(fg_color=("#550000"),
                              hover_color="#550000", text_color="#000000")
            else:
                AB1.configure(fg_color=("#550000"),
                              hover_color="#550000", text_color="#000000")
                if AB2.cget("text") == info[question][1]:
                    AB2.configure(fg_color=("#005500"),
                                  hover_color="#005500", text_color="#000000")
                    AB3.configure(fg_color=("#550000"),
                                  hover_color="#550000", text_color="#000000")
                else:
                    AB3.configure(fg_color=("#005500"),
                                  hover_color="#005500", text_color="#000000")
                    AB2.configure(fg_color=("#550000"),
                                  hover_color="#550000", text_color="#000000")

        case 2:
            if AB2.cget("text") == info[question][1]:
                correct += 1
                AB2.configure(fg_color=("#005500"),
                              hover_color="#005500", text_color="#000000")
                AB1.configure(fg_color=("#550000"),
                              hover_color="#550000", text_color="#000000")
                AB3.configure(fg_color=("#550000"),
                              hover_color="#550000", text_color="#000000")
            else:
                AB2.configure(fg_color=("#550000"),
                              hover_color="#550000", text_color="#000000")
                if AB1.cget("text") == info[question][1]:
                    AB1.configure(fg_color=("#005500"),
                                  hover_color="#005500", text_color="#000000")
                    AB3.configure(fg_color=("#550000"),
                                  hover_color="#550000", text_color="#000000")
                else:
                    AB3.configure(fg_color=("#005500"),
                                  hover_color="#005500", text_color="#000000")
                    AB1.configure(fg_color=("#550000"),
                                  hover_color="#550000", text_color="#000000")

        case 3:
            if AB3.cget("text") == info[question][1]:
                correct += 1
                AB3.configure(fg_color=("#005500"),
                              hover_color="#005500", text_color="#000000")
                AB2.configure(fg_color=("#550000"),
                              hover_color="#550000", text_color="#000000")
                AB1.configure(fg_color=("#550000"),
                              hover_color="#550000", text_color="#000000")
            else:
                AB3.configure(fg_color=("#550000"),
                              hover_color="#550000", text_color="#000000")
                if AB1.cget("text") == info[question][1]:
                    AB1.configure(fg_color=("#005500"),
                                  hover_color="#005500", text_color="#000000")
                    AB2.configure(fg_color=("#550000"),
                                  hover_color="#550000", text_color="#000000")
                else:
                    AB2.configure(fg_color=("#005500"),
                                  hover_color="#005500", text_color="#000000")
                    AB1.configure(fg_color=("#550000"),
                                  hover_color="#550000", text_color="#000000")
    AB1.configure(state="disabled")
    AB2.configure(state="disabled")
    AB3.configure(state="disabled")
    ContBtn.configure(state="normal")


def endScreen(tk=None):
    hide(tk)
    EndScreen = CTkToplevel()
    EndScreen.geometry("500x400+750+300")
    EndScreen.resizable(False, False)
    EndScreen.title("Quiz End")
    EndScreen.bind("<Escape>", lambda x: sys.exit())
    Title = CTkLabel(EndScreen, text='End screen', font=("Arial", 10))
    Title.place(relx=0.5, rely=0.05, anchor="center")
    ExitBtn = CTkButton(master=EndScreen, text="Menu",
                        fg_color="#550000", text_color="#000000", command=lambda: Menu(EndScreen)).place(relx=0.5, rely=0.7, anchor="center")


def changeFile():
    # add change file code here
    files = getFiles()
    filePicker(files)


def filePicker(files):
    hide(app)
    FilePicker = CTkToplevel()
    FilePicker.geometry("500x400+750+300")
    FilePicker.resizable(False, False)
    FilePicker.title("File Picker")
    FilePicker.bind("<Escape>", lambda x: sys.exit())
    Title = CTkLabel(
        master=FilePicker, text="Which file would you like to load?", font=("Arial", 10))
    Title.place(relx=0.5, rely=0.05, anchor="center")

    Options = CTkComboBox(FilePicker, values=files,
                          variable="Unselected", command=changeHandler)  # type: ignore
    Options.place(relx=0.5, rely=0.5, anchor="center")

    ExitBtn = CTkButton(master=FilePicker, text="Menu",
                        fg_color="#550000", text_color="#000000", command=lambda: Menu(FilePicker)).place(relx=0.5, rely=0.7, anchor="center")


def changeHandler(value):
    global file_name
    file_name = value

    return file_name


def Menu(tk=None):
    print(correct)
    global info
    info = FileHandling(file_name)
    global app
    # makes app unless app is made then it reveals it.
    if app == None:
        app = CTk()
        app.geometry("500x400+750+300")
        app.resizable(False, False)
        app.iconbitmap("./icons/icon.ico")
        app.title("Menu")
        set_appearance_mode("dark")
        # binds Esc key to close the app
        app.bind("<Escape>", lambda x: sys.exit())

        Title = CTkLabel(master=app, text="Flash Card Project",
                         font=("Arial", 40))
        PlayBtn = CTkButton(master=app, text="Start",
                            fg_color="#005500", text_color="#000000", command=lambda: Run(app))
        Changebtn = CTkButton(master=app, text="Change File",
                              fg_color="#AA4203", text_color="#000000", command=changeFile)
        ExitBtn = CTkButton(master=app, text="Exit",
                            fg_color="#550000", text_color="#000000", command=app.quit)

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
