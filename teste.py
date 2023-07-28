# Import tkinter using import keyword
import tkinter as tk

# set the master object in parent variable
parent = tk.Tk()

# Title for our window
parent.title("Geeksforgeeks- OptionMenu")

# Creating a Option Menu for AGE
# Set the variable for AGE and create the list
# of options by initializing the constructor
# of class OptionMenu.
Age_Variable = tk.StringVar(parent)
Age_Variable.set("Age")
Age_Option = tk.OptionMenu(parent, Age_Variable,
						"below 14", "15",
						"16", "17",
						"above 18")
Age_Option.pack()

# Creating a Option Menu for GENDER
# Set the variable for GENDER and create the list
# of options by initializing the constructor
# of class OptionMenu.
Gender_Variable = tk.StringVar(parent)
Gender_Variable.set("Gender")
Gender_Option = tk.OptionMenu(parent,
							Gender_Variable,
							"Male", "Female")
Gender_Option.pack()

# Creating a Option Menu for HOBBY
# Set the variable for HOBBY and create the list
# of options by initializing the constructor
# of class OptionMenu.
Hobby_Variable = tk.StringVar(parent)
Hobby_Variable.set("Hobby")
Hobby_Option = tk.OptionMenu(parent, Hobby_Variable,
							"Dance", "Code", "Sing",
							"Draw")
Hobby_Option.pack()

# Combining all the widgets used in the
# program before running it
parent.mainloop()
