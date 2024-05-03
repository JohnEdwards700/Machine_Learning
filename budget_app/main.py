# import PySimpleGUI as sg
import helpers as func

# root = ttk.Window()

# b1 = ttk.Button(root, text="Button 1", bootstyle=SUCCESS)
# b1.pack(side=LEFT, padx=5, pady=10)

# b2 = ttk.Button(root, text="Button 2", bootstyle=(INFO, OUTLINE))
# b2.pack(side=LEFT, padx=5, pady=10)

# root.mainloop()

import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


window = ttk.Window(themename="darkly")
window.title("Loading Page")

def signup():
    pass

def login():
    #creates a new window from login to access the Dashboard
    new_window = ttk.Toplevel(window)
    
    #title of window
    new_window.title("new window")
    
    #---------creat a row and column of whole window------------
    new_window.rowconfigure(0, minsize=200, weight=1)
    new_window.columnconfigure(1, minsize=200, weight=1)
    
    #----------left---side------------
    #buttons on the left side Settings, Options, Log Out
    btn_logout = ttk.Button(new_window, text="Log Out", bootstyle="danger", command=loginpage)
    btn_open = ttk.Button(new_window, text="Options")
    btn_save = ttk.Button(new_window, text="Settings")
    
    #positioning of buttons
    btn_open.grid(row=0, column=0, sticky="n", padx=5, pady=5)
    btn_save.grid(row=1, column=0, sticky="n", padx=5)
    btn_logout.grid(row=2, column=0, pady=5)
    
# --------------right side of screen--------------------------
#frame thats going to hold graph on top and other options below
    data_interfance_main = ttk.Frame(new_window)
    data_interfance_main.grid(row=0, column=1, sticky="nsew", pady=20)
    
#----top right charts----
    chartframe = ttk.Frame(data_interfance_main)
    chartframe.grid(row=0, column=0, pady=20)
    graphlabel = ttk.Label(chartframe, text="Networth", font=("Helvetica", 12))
    graphlabel.pack()
    fig = func.net_worth_chart()
    canvas = FigureCanvasTkAgg(fig, chartframe)
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
#----bottom right tabs-----
    bottom_notebook_frame = ttk.Frame(data_interfance_main)
    bottom_notebook_frame.grid(row=1, column=0, pady=10)
    tabs = ttk.Notebook(bottom_notebook_frame, bootstyle="dark")
    tabs.pack(pady=5)
    tab1 = ttk.Frame(tabs)
    tab2 = ttk.Frame(tabs)
    tab1_label = ttk.Label(tab1, text="tab1", font=("Helvetica", 10))
    tab1_label.pack(pady=5)
    text1= ttk.Text(tab1, width=40, height=10)
    text1.pack(pady=10, padx=10)
    tab1_butt=ttk.Button(tab1, text="click here", bootstyle="success outline")
    tab1_butt.pack()
    
    tabs.add(tab1, text="Tab One")
    
    
    new_window.mainloop()

#-------main--loginpage-------
def loginpage(): 
    frame1 = ttk.Frame(window)#, bootstyle="dark"
    frame1.pack(pady=50, expand=True)
    
    label1 = ttk.Label(frame1, text="Budget Bucks Login", font=("Helvetica", 18))
    label1.grid(row=0, column=0, columnspan=3, pady=10)

    label1 = ttk.Label(frame1, text="Username:", font=("Helvetica", 12))
    label1.grid(row=1, column=0, columnspan=1, padx=10, pady=40)

    userentry = ttk.Entry(frame1, font=("Helvetica",20))
    userentry.grid(row=1, column=1, columnspan=2, pady=40, padx=20)

    label2 = ttk.Label(frame1, text="Password:", font=("Helvetica", 12))
    label2.grid(row=2, column=0, columnspan=1, padx=10 ,pady=10)

    passentry = ttk.Entry(frame1, font=("Helvetica",20), show="*")
    passentry.grid(row=2, column=1, columnspan=2,pady=40, padx=20)

    logButton = ttk.Button(frame1, text="LOG IN", bootstyle="success", command=login)
    logButton.grid(row=3, column=0, columnspan=2, pady=20, padx=30)
    
    SignUpButton = ttk.Button(frame1, text="SIGN UP", bootstyle="danger", command=signup)
    SignUpButton.grid(row=3, column=1, columnspan=2, pady=20, padx=40)
        
if __name__ == "__main__":
    loginpage()




# window.rowconfigure(0, minsize=800, weight=1)
# window.columnconfigure(1, minsize=800, weight=1)

# txt_edit = ttk.Text(window)
# # # frm_buttons = ttk.Frame(window, bd=2)
# btn_open = ttk.Button(window, text="Open")
# btn_save = ttk.Button(window, text="Save As...")

# btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
# btn_save.grid(row=1, column=0, sticky="ew", padx=5)

# # frm_buttons.grid(row=0, column=0, sticky="ns")
# txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()

# ...

# while True:
#     user_input = input("YOU: ")
#     response = func.respond(user_input)
#     print("Budget_Bot: ", response)
#     if user_input == "break":
#         break
    
#.....
# layout = [  [sg.Text('Some text on Row 1', size = 300)],
#             [sg.Text('Enter something on Row 2'), sg.InputText()],
#             [sg.Button('Ok'), sg.Button('Cancel')] ]

# # Create the Window
# window = sg.Window('Window Title', layout)

# # Event Loop to process "events" and get the "values" of the inputs
# while True:
#     event, values = window.read()
#     if event == sg.WIN_CLOSED or event == 'Cancel':	# if user closes window or clicks cancel
#         break
#     print('You entered ', values[0])

# window.close()