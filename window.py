import tkinter as tk

def popup_window():
    popup = tk.Tk()
    popup.title("Menu")
    
    menubar = tk.Menu(popup)
    popup.config(menu=menubar)
    
       
    help_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Home", menu=help_menu)
    menubar.add_cascade(label="Login", menu=help_menu)
    menubar.add_cascade(label="About", menu=help_menu)
    
    help_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="Contact us")
       
    
    label = tk.Label(popup)
    label.pack(padx=150, pady=150)
    popup.mainloop()

# Example usage:
popup_window()