import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
import re
from math import sqrt
import sqlite3


def Change():

    upassone = passwone.get()
    upasstwo = passtwo.get()

    if upassone == '' and upasstwo == '':
        messagePass.set("Fill the empty field!!!")
    else:
        if upassone == upasstwo:
            messagePass.set("Parole samainīta")
            cur.execute("SELECT * FROM users WHERE username='%s';" % uname)
            user = cur.fetchall()
            user = user[0][0]
            user_new = upassone, user
            cur.execute("UPDATE users SET password='%s' WHERE username='%s';" %user_new)
            conn.commit()
            window_changepass.destroy()
            Start()
        else:
            messagePass.set("Paroles nav līdzigas")


def ChangePassword_window():
    global window_changepass

    window_login.destroy()
    window_changepass = tk.Tk()
    window_changepass.title("Login Form")
    window_changepass.geometry("400x250")
    window_changepass.resizable(width=False, height=False)

    window_changepass.configure(bg="#CEEDC7")

    global passwone, passtwo, messagePass

    passwone = tk.StringVar()
    passtwo = tk.StringVar()
    messagePass = tk.StringVar()

    tk.Label(window_changepass, text="Samainiet savu paroli!", background="#CEEDC7", font=('Calibri Light', 17)).grid(column=0, row=1, padx= 100.0, sticky="w")

    tk.Label(window_changepass, text="Jauna parole:", background="#CEEDC7", font=('Calibri Light', 15, 'bold')).grid(column=0, row=2, padx= 10.0, sticky="w")
    tk.Entry(window_changepass, textvariable=passwone, width=24, font=('Calibri Light', 15)).grid(column=0, row=3, padx=110.0,sticky="w")
    tk.Label(window_changepass, text="Atkartojiet paroli", background="#CEEDC7",font=('Calibri Light', 15, 'bold')).grid(column=0, row=4, padx=10.0, sticky="w")
    tk.Entry(window_changepass, textvariable=passtwo, width=24, font=('Calibri Light', 15)).grid(column=0, row=5, padx=110.0, sticky="w")

    tk.Label(window_changepass, text="dasdad",textvariable=messagePass, background="#CEEDC7", font=('Calibri Light', 14)).grid(column=0, row=6, padx=10.0, sticky="w")
    button_change = ttk.Button(window_changepass, text="Change", command=Change)
    button_change.place(height=40, width=70, x=170, y=200)

    window_changepass.mainloop()


def ChangePassword_button():

    global window_login

    button_changePass = ttk.Button(window_login, text="Change Password", command=ChangePassword_window)
    button_changePass.place(height=30, width=120, x=271, y=99)


def Login():

    global destroy, uname

    uname = username.get()
    passw = password.get()
    user_data = uname, passw

    if uname == '' or passw == '':
        message.set("Fill the empty field!!!")
    else:
        if uname != "" and passw != "":
            # message.set("Login success")
            cur.execute("SELECT * FROM users WHERE username='%s';" % uname)
            exist_username = cur.fetchall()
            exist_username = len(exist_username)
            if exist_username!=0:  # proverjaet praviljnij li password
                cur.execute("SELECT * FROM users WHERE username='%s' AND password='%s';" % user_data)
                exist_userdata = cur.fetchall()
                exist_userdata = len(exist_userdata)
                if exist_userdata != 0:
                    message.set("Login success")
                    destroy = 1
                    window_login.destroy()
                elif exist_userdata == 0:
                    message.set("Wrong password")
                    ChangePassword_button()
            else:
                message.set("Login success")
                cur.execute("INSERT INTO users VALUES(?,?);", user_data)
                conn.commit()
                destroy = 1
                window_login.destroy()


def Start():

    global window_login

    window_login = tk.Tk()
    window_login.title("Login Form")
    window_login.geometry("400x250")
    window_login.resizable(width=False, height=False)

    window_login.configure(bg="#CEEDC7")
    style_login = ttk.Style()
    style_login.theme_create("loggy", parent="alt", settings={
        "TButton": {
            "configure": {"font": ("Calibri Light", 10, "bold"), "foreground": "black", "background": "#86C8BC"},
            "map": {"background": [("disabled", "black"), ("pressed", "#CBAF87"), ("active", "#E7DEC8")],
                    "relief": [("pressed", "sunken"), ("!pressed", "raised")]}}})
    style_login.theme_use("loggy")

    global message, username, password

    message = tk.StringVar()
    username = tk.StringVar()
    password = tk.StringVar()

    tk.Label(window_login, text="Labdien, lietotājs!", background="#CEEDC7", font=('Calibri Light', 17)).grid(column=0, row=1, padx= 120.0, sticky="w")
    tk.Label(window_login, text="Lūdzu pielogojies", background="#CEEDC7", font=('Calibri Light', 17)).grid(column=0, row=2, padx=120.0, sticky="w")

    tk.Label(window_login, text="Username", background="#CEEDC7", font=('Calibri Light', 15, 'bold')).grid(column=0, row=3, padx= 10.0, sticky="w")
    tk.Entry(window_login, textvariable=username, width=24, font=('Calibri Light', 15)).grid(column=0, row=3, padx=110.0,sticky="w")
    tk.Label(window_login, text="Password", background="#CEEDC7",font=('Calibri Light', 15, 'bold')).grid(column=0, row=4, padx=10.0, sticky="w")
    tk.Entry(window_login, textvariable=password, show="*", width=15, font=('Calibri Light', 15)).grid(column=0, row=4, padx=110.0, sticky="w")

    tk.Label(window_login, text="", textvariable=message,  background="#CEEDC7", font=('Calibri Light', 14)).grid(column=0, row=5, padx=100.0, sticky="w")
    button_login = ttk.Button(window_login, text="Login", command=Login)
    button_login.place(height=40, width=70, x=170, y=200)


    window_login.mainloop()


def Draw_Cartesian_Coordinate(parametr):

    xmin, xmax, ymin, ymax = -3-parametr, 3+abs(parametr), -3-parametr, 5+abs(parametr)
    ticks_frequency = 1

    fig, ax = plt.subplots(figsize=(8, 8))

    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')

    ax.set(xlim=(xmin - 1, xmax + 1), ylim=(ymin - 1, ymax + 1), aspect='equal')

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    ax.set_xlabel('x', size=14, labelpad=-24, x=1.03)
    ax.set_ylabel('y', size=14, labelpad=-5, y=0.97, rotation=0)

    x_ticks = np.arange(xmin, xmax + 1, ticks_frequency)
    y_ticks = np.arange(ymin, ymax + 1, ticks_frequency)
    ax.set_xticks(x_ticks[x_ticks != 0])
    ax.set_yticks(y_ticks[y_ticks != 0])

    ax.set_xticks(np.arange(xmin, xmax + 1), minor=True)
    ax.set_yticks(np.arange(ymin, ymax + 1), minor=True)

    ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)

    arrow_fmt = dict(markersize=4, color='black', clip_on=False)
    ax.plot((1), (0), marker='>', transform=ax.get_yaxis_transform(), **arrow_fmt)
    ax.plot((0), (1), marker='^', transform=ax.get_xaxis_transform(), **arrow_fmt)

def Kvadrat_koef():

    global function_kvadrat

    a = 0
    b = 0
    c = 0

    inp = function_kvadrat

    delimiters = "+", "-"
    regex_pattern = '|'.join(map(re.escape, delimiters))
    # inp = inp.replace("*x", "x")
    # inp = inp.replace("**", "^")
    elements = re.split(regex_pattern, inp)

    if elements[0] == "":  # case -a
        a = -(float(elements[1][:elements[1].find("x")]))
        indexb = 2
        indexc = 3
    else:
        a = (float(elements[0][:elements[0].find("x")]))  # +a
        indexb = 1
        indexc = 2

    if ((inp.find("-") < inp.find("x", inp.find("^"))) and (inp.find("-") != -1)):  # -b
        b = -float(elements[indexb][:elements[indexb].find("x")])
    else:
        b = float(elements[indexb][:elements[indexb].find("x")])

    if (inp.find("-", inp.find("x", inp.find("x") + 1)) > inp.find("x", inp.find("^"))):
        c = -float(elements[indexc])
    else:
        c = float(elements[indexc])

    return(a, b, c)



def Draw_line_func():

    global function_line, line_bool

    if line_bool != 0:

        plus = function_line.find("+")
        if plus >= 0:
            plus = plus + 1
            m = function_line[plus:]
        else:
            plus = function_line.find("-", 1)
            m = function_line[plus:]
        plus = function_line.find("x")
        k = function_line[:plus]
        Draw_Cartesian_Coordinate(int(m))

        y = [-5.0,  0,  5.0]
        y[0] = y[0] - abs(float(m))
        y[2] = y[2] + abs(float(m))
        x = []

        for i in range(len(y)):
            z = y[i]
            x.append((z - float(m)) / float(k))

        plt.title('Graph of y='+function_line)
        plt.plot(y, x)
        plt.show()


def Draw_kvadrat_func():

    global function_kvadrat, kvadrat_bool

    a, b, c = Kvadrat_koef()

    if kvadrat_bool != 0:

        Draw_Cartesian_Coordinate(c)


        x = [-7.0, -3.0, -2.0, -1.0, -0.1, 0.1, 1.0, 2.0, 3.0, 7.0]
        y = []
        a, b, c = Kvadrat_koef()
        for i in range(len(x)):
            z = x[i]
            y.append(a*(z**2)+(b*z)+c)

        plt.title('Graph of y='+function_kvadrat)
        plt.plot(x, y)
        plt.show()


def Draw_apgriezta_func():

    global function_apgriezta, apgriezta_bool

    if apgriezta_bool != 0:

        Draw_Cartesian_Coordinate(3)

        x1 = [-7.0, -6.0, -5.0, -4.0, -3.0, -2.0, -1.0, -0.1]
        x2 = [7.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0, 0.1]
        y1 = []
        y2 = []
        point = function_apgriezta.find("/")
        k = function_apgriezta[:point]

        for i in range(len(x1)):
            z = x1[i]
            y1.append(float(k)/float(z))

        for i in range(len(x2)):
            z = x2[i]
            y2.append(float(k)/float(z))


        plt.title('Graph of y=' + function_apgriezta)
        plt.plot(y1, x1)
        plt.plot(y2, x2)
        plt.show()


def Print_function(func, lab, exist):

    if exist == 1:
        lab["text"] = func
    else:
        lab["text"] = "Nav pareiza funkcija"


def Print_intersection_line(x, y):

    global line_bool

    if line_bool != 0:
        label_user_lineara_intersection["text"] = (" Krustpunkti: (" + str(x) + ";0)  (0;" + str(y) + ")")


def Print_height_kvadrat(xo, yo):

    global kvadrat_bool

    if kvadrat_bool != 0:
        label_user_kvadrat_height["text"] = ("Augstuma koordinates: (" + str(xo) + ";" + str(yo) + ")")


def Print_intersection_kvadrat():

    global kvadrat_bool

    inter_quantity = Kvadrat_intersection_quantity()
    print(inter_quantity)
    if kvadrat_bool != 0:
        if inter_quantity == 1:
            x, y = Kvadrat_Intersection()
            label_user_kvadrata_intersection["text"] = (" Krustpunkti: (" + str(x) + ";" + str(y) + ")")
        elif inter_quantity == 2:
            x1, x2, y1, y2 = Kvadrat_Intersection()
            label_user_kvadrata_intersection["text"] = (" Krustpunkti: (" + str(x1) + ";" + str(y1) + ") (" + str(x2) + ";" + str(y2) + ")")


def Check_Function_Kvadrat():

    global function_kvadrat, kvadrat_bool

    kvadrat_bool = 0

    if "x^2" in function_kvadrat and "x" in function_kvadrat:
        place = function_kvadrat.find("x^2")
        if function_kvadrat[:place] == "":
            function_kvadrat = function_kvadrat.replace("x^2", "1x^2")
        if "+x" in function_kvadrat or "-x" in function_kvadrat:
            if "+x" in function_kvadrat:
                function_kvadrat = function_kvadrat.replace("+x", "+1x")
            elif "-x" in function_kvadrat:
                function_kvadrat = function_kvadrat.replace("-x", "-1x")
        kvadrat_bool = 1
        func_database = uname, function_kvadrat
        cur.execute("INSERT INTO functions VALUES(?, ?);", func_database)
        conn.commit()
        Print_function(function_kvadrat, label_user_kvadrat, kvadrat_bool)
    else:
        kvadrat_bool = 0
        Print_function(function_kvadrat, label_user_kvadrat, kvadrat_bool)


def Check_Function_Line():

    global function_line, line_bool

    line_bool = 0
    if "x+" in function_line or "x-" in function_line:
        if "x^" in function_line:
            line_bool = 0
        else:
            line_bool = 1
            place = function_line.find("x")
            if function_line[:place] == "":
                function_line = function_line.replace("x", "1x")
            func_database = uname, function_line
            cur.execute("INSERT INTO functions VALUES(?, ?);", func_database)
            conn.commit()
        Print_function(function_line, label_user_lineara, line_bool)
    else:
        line_bool = 0
        Print_function(function_line, label_user_lineara, line_bool)


def Check_Function_Apgriezta():

    global function_apgriezta, apgriezta_bool

    apgriezta_bool = 0
    if "/x" in function_apgriezta:
        apgriezta_bool = 1
        func_database = uname, function_apgriezta
        cur.execute("INSERT INTO functions VALUES(?, ?);", func_database)
        conn.commit()
        Print_function(function_apgriezta, label_user_apgriezta, apgriezta_bool)
    else:
        apgriezta_bool = 0
        Print_function(function_apgriezta, label_user_apgriezta, apgriezta_bool)


def Line_Intersection():

    global function_line

    x = function_line.find("+")
    if x >= 0:
        x = x + 1
        m = function_line[x:]
    else:
        x = function_line.find("-", 1)
        m = function_line[x:]
    x = function_line.find("x")
    k = function_line[:x]

    x_axis = float(m) / -(float(int(k)))
    y_axis = m
    Print_intersection_line(float(round(x_axis, 2)), y_axis)



def Kvadrat_height():

    a, b, c = Kvadrat_koef()

    xo = (-b)/(2*a)
    yo = a*(xo**2)+(b*xo)+c

    Print_height_kvadrat(float(round(xo, 2)), float(round(yo, 2)))


def Kvadrat_intersection_quantity():

    a, b, c = Kvadrat_koef()
    inter_quantity = 0
    D = b**2 - (4*a*c)
    if D>0:
        inter_quantity = 2
    elif D == 0:
        inter_quantity = 1
    elif D < 0:
        inter_quantity = 1
    return inter_quantity


def Kvadrat_Intersection():

    a, b, c = Kvadrat_koef()
    D = b**2 - (4*a*c)
    if D>0:
        x1 = round(((-b)+sqrt(D))/(2*a), 2)
        x2 = round(((-b)-sqrt(D))/(2*a), 2)
        y1 = 0
        y2 = 0
        return x1, x2, y1, y2
    elif D==0:
        x1 = round((-b)/(2*a), 2)
        y1 = 0
        return x1, y1
    elif D<0:
        x=0
        y=c
        return x, y


def Submit_User_Kvadrat():

    global function_kvadrat

    label_user_kvadrat_height["text"] = ""
    label_user_kvadrata_intersection["text"] = ""
    function_kvadrat = func_user.get()
    Check_Function_Kvadrat()

    func_user.set("")


def Submit_User_Line():

    global function_line

    label_user_lineara_intersection["text"] = ""
    function_line = func_user.get()
    Check_Function_Line()

    func_user.set("")


def Submit_User_Apgriezta():

    global function_apgriezta
    function_apgriezta = func_user.get()
    Check_Function_Apgriezta()
    func_user.set("")


def Update_History():

    cur.execute("SELECT function FROM functions WHERE username='%s';" % uname)

    functions = cur.fetchall()
    functions = str(functions)
    functions = functions.replace("[", "")
    functions = functions.replace("]", "")
    functions = functions.replace("[", "")
    functions = functions.replace("'", "")
    functions = functions.replace(",", "")
    functions = functions.replace(")", "),")
    user_history.set(functions)


def tab_lineara_create(tab_lineara, bg_color):

    text_tab_lineara = tk.Label(tab_lineara, text="Lineāras funkcijas aprēķinašana:", background= bg_color, font=('Calibri Light', 18, 'bold'))
    text_tab_lineara.grid(column=0, row=1, padx=padx, pady=pady, sticky="w")

    text_example = tk.Label(tab_lineara, text="Paraugs: y=kx+m", background= bg_color, font=('Calibri Light', 15))
    text_example.grid(column=0, row=2, padx=padx, sticky="w")

    text_lineara = tk.Label(tab_lineara, text="Ievadiet Jūsu funkciju:", background= bg_color, font=('Calibri Light', 15))
    text_lineara.grid(column=0, row=3, padx=padx, sticky="w")

    text = tk.Label(tab_lineara, text="y=", background= bg_color, font=('Calibri Light', 15))
    text.grid(column=0, row=6, padx=padx, sticky="w")

    Entry_lineara = tk.Entry(tab_lineara, textvariable = func_user, width=18, font=('Calibri Light', 15))
    Entry_lineara.grid(column=0, row=6,padx=35.0, sticky="w")

    button_intersection = ttk.Button(tab_lineara, text = "Krustpunkti", command=Line_Intersection)
    button_intersection.place(height=40, width=120, x=350, y=125)

    button_graph = ttk.Button(tab_lineara, text = "Grafiks", command=Draw_line_func)
    button_graph.place(height=40, width=120, x=350, y=170)

    button_enter = ttk.Button(tab_lineara, text="Ievadīt", command=Submit_User_Line)
    button_enter.place(height=30, width=70, x=227, y=115)


def tab_kvadrat_create(tab_kvadrat, bg_color):

    text_tab = tk.Label(tab_kvadrat,text="Kvadrātfunkcijas aprēķinašana:", background= bg_color, font=('Calibri Light', 18, 'bold'))
    text_tab.grid(column=0, row=1, padx=padx, pady=pady, sticky="w")

    text_example = tk.Label(tab_kvadrat,text="Paraugs: y=ax^2+bx+c", background= bg_color, font=('Calibri Light', 15))
    text_example.grid(column=0, row=2, padx=padx, sticky="w")

    text = tk.Label(tab_kvadrat, text="Ievadiet Jūsu funkciju:", background= bg_color, font=('Calibri Light', 15))
    text.grid(column=0, row=3, padx=padx, sticky="w")

    text1 = tk.Label(tab_kvadrat, text="y=", background= bg_color, font=('Calibri Light', 15))
    text1.grid(column=0, row=5, padx=padx, sticky="w")

    Entry = tk.Entry(tab_kvadrat,  textvariable = func_user, width=18, font=('Calibri Light', 15))
    Entry.grid(column=0, row=5,padx=35.0, sticky="w")

    button_enter = ttk.Button(tab_kvadrat, text="Ievadīt", command=Submit_User_Kvadrat)
    button_enter.place(height=30, width=70, x=227, y=115)

    button_high_point = ttk.Button(tab_kvadrat, text="Virsotne", style="TButton", command=Kvadrat_height)
    button_high_point.place(height=40, width=120, x=350, y=80)

    button_intersection = ttk.Button(tab_kvadrat, text="Krustpunkti", command=Print_intersection_kvadrat)
    button_intersection.place(height=40, width=120, x=350, y=125)

    button_graph = ttk.Button(tab_kvadrat, text="Grafiks", command=Draw_kvadrat_func)
    button_graph.place(height=40, width=120, x=350, y=170)


def tab_apgriezta_create(tab_apgriezta, bg_color):

    text_tab = tk.Label(tab_apgriezta, text="Apgrieztas funkcijas aprēķinašana:", background= bg_color, font=('Calibri Light', 18, 'bold'))
    text_tab.grid(column=0, row=1, padx=padx, pady=pady, sticky="w")

    text_example = tk.Label(tab_apgriezta, text="Paraugs: y=a/x", background= bg_color, font=('Calibri Light', 15))
    text_example.grid(column=0, row=2, padx=padx, sticky="w")

    text = tk.Label(tab_apgriezta, text="Ievadiet Jūsu funkciju:", background= bg_color, font=('Calibri Light', 15))
    text.grid(column=0, row=3, padx=padx, sticky="w")

    text1 = tk.Label(tab_apgriezta, text="y=", background= bg_color, font=('Calibri Light', 15))
    text1.grid(column=0, row=5, padx=padx, sticky="w")

    Entry = tk.Entry(tab_apgriezta,  textvariable = func_user, width=18, font=('Calibri Light', 15))
    Entry.grid(column=0, row=5,padx=35.0, sticky="w")

    button_enter = ttk.Button(tab_apgriezta, text="Ievadīt", command=Submit_User_Apgriezta)
    button_enter.place(height=30, width=70, x=227, y=115)

    button_graph = ttk.Button(tab_apgriezta, text="Grafiks", command=Draw_apgriezta_func)
    button_graph.place(height=40, width=120, x=350, y=125)


def tab_history_create(tab_history, bg_color):
    text_history = tk.Label(tab_history, text="Lietotāja ievadītas funkcijas:", background = bg_color, font=('Calibri Light', 18, 'bold'))
    text_history.grid(column=0, row=1, padx=padx, pady=pady, sticky="w")

    global user_history

    user_history = tk.StringVar()

    msg = tk.Message(tab_history, textvariable=user_history, background=bg_color, width=450, font=('Calibri Light', 16))
    msg.place(x=5, y=50)

    button_update = ttk.Button(tab_history, text="Update", command=Update_History)
    button_update.place(height=35, width=75, x=200, y=220)


def DataBase():
    global conn, cur
    conn = sqlite3.connect('Users_Database.db')
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
       username type UNIQUE PRIMARY KEY,
       password TEXT);
    """)
    conn.commit()
    cur.execute("""CREATE TABLE IF NOT EXISTS functions(
       username TEXT,
       function TEXT);
    """)
    conn.commit()


global destroy
destroy = 0
DataBase()
Start()
if destroy == 1:
    window = tk.Tk()
    window.title("Funkcijas aprekinātājs")
    window.geometry("500x300")
    window.resizable(width=False, height=False)

    style = ttk.Style()

    # colors
    bg_color = "#CEEDC7"
    bg_Tab = "#FFD4B2"
    bg_Tab_selected = "#FFF6BD"

    style.theme_create( "dummy", parent="alt", settings={
            "TFrame": { "configure": {"background": bg_color}},
            "TNotebook": {"configure": {"tabmargins": [5, 5, 2, 0],
                          "background": bg_color}},
            "TButton": {
                "configure": {"font": ("Calibri Light", 14,"bold"),"foreground": "black", "background": "#86C8BC"},
                "map":  {"background": [("disabled", "black"), ("pressed","#CBAF87"), ("active", "#E7DEC8")],
                        "relief": [("pressed","sunken"), ("!pressed","raised")]}},
            "TNotebook.Tab": {
                "configure": {"padding": [9, 4], "background": bg_Tab },
                "map":       {"background": [("selected", bg_Tab_selected)],
                              "expand": [("selected", [1, 1, 1, 0])]}}})

    style.theme_use("dummy")

    tabs = ttk.Notebook(window)

    tab_lineara = ttk.Frame(tabs)
    tabs.add(tab_lineara, text = 'Lineāra')

    tab_kvadrat = ttk.Frame(tabs)
    tabs.add(tab_kvadrat, text = 'Kvadrat')

    tab_apgriezta = ttk.Frame(tabs)
    tabs.add(tab_apgriezta, text = 'Apgriezta')

    tab_history = ttk.Frame(tabs)
    tabs.add(tab_history, text= 'Vēsture')

    tabs.pack(expand=1, fill="both")

    padx = 10.0
    pady = 10.0
    func_user = tk.StringVar()

    tab_lineara_create(tab_lineara, bg_color)
    tab_kvadrat_create(tab_kvadrat, bg_color)
    tab_apgriezta_create(tab_apgriezta, bg_color)
    tab_history_create(tab_history, bg_color)
    global label_user_lineara_intersection, label_user_kvadrata_intersection, label_user_kvadrat_height

    label_user_lineara = tk.Label(tab_lineara, text="", background=bg_color, font=('Calibri Light', 15))
    label_user_lineara.grid(column=0, row=7, padx=padx, pady=pady, sticky="w")

    label_user_kvadrat = tk.Label(tab_kvadrat, text="", background=bg_color, font=('Calibri Light', 15))
    label_user_kvadrat.grid(column=0, row=7, padx=padx, pady=pady, sticky="w")

    label_user_apgriezta = tk.Label(tab_apgriezta, text="", background=bg_color, font=('Calibri Light', 15))
    label_user_apgriezta.grid(column=0, row=7, padx=padx, pady=pady, sticky="w")

    label_user_lineara_intersection = tk.Label(tab_lineara, text="", background=bg_color, font=('Calibri Light', 15))
    label_user_lineara_intersection.grid(column=0, row=8, padx=padx, pady=pady, sticky="w")

    label_user_kvadrata_intersection = tk.Label(tab_kvadrat, text="", background=bg_color, font=('Calibri Light', 15))
    label_user_kvadrata_intersection.place(x=5, y=225)

    label_user_kvadrat_height = tk.Label(tab_kvadrat, text="", background=bg_color, font=('Calibri Light', 15))
    label_user_kvadrat_height.grid(column=0, row=8, padx=padx, sticky="w")

    function = ""
    xo = 0
    yo = 0

    window.mainloop()

