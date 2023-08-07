import tkinter 
from tkinter import *
import json
from tkmacosx import Button

root=Tk()
root.title("To-Do-List")
root.geometry("400x650+400+100")
root.resizable(False,False)

task_list= []

def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)

    if task:
        branch = branch_var.get()
        if not branch:
            branch = "default"  # If no branch name is provided, use "default"

        new_task = {
            "taskname": task,
            "check": False
        }

        with open('tasklist.json', 'r') as f:
            data = json.load(f)
            if branch not in data:
                data[branch] = []  # Create the branch if it doesn't exist
            data[branch].append(new_task)

        with open('tasklist.json', 'w') as fw:
            json.dump(data, fw, indent=4, separators=(',', ': '))

        listbox.insert(END, task)  # Insert the task in the listbox

def onBranchSelected(event=None):
    selected_branch = branch_var.get()
    listbox.delete(0, END)
    with open('tasklist.json', 'r') as f:
        data = json.load(f)
        if selected_branch in data:
            for task_data in data[selected_branch]:
                task_status = "[√] " if task_data["check"] else "[ ] "  # Add a checkmark if task is done
                task_with_status = f"{task_status}{task_data['taskname']}"
                listbox.insert(END, task_with_status)

def load_options_from_json():
    with open("tasklist.json", 'r') as file:
        data = json.load(file)
        return data
        
        
def deleteTask():
    selected_index = listbox.curselection()
    if not selected_index:
        return

    selected_index = selected_index[0]  # The curselection() method returns a tuple; get the first item (index)

    selected_branch = branch_var.get()
    if not selected_branch:
        selected_branch = "default"  # If no branch name is provided, use "default"

    with open('tasklist.json', 'r') as f:
        data = json.load(f)
        if selected_branch in data:
            del data[selected_branch][selected_index]  # Remove the task at the selected index

    with open('tasklist.json', 'w') as fw:
        json.dump(data, fw, indent=4, separators=(',', ': '))

    onBranchSelected()  # Refresh the listbox after deleting the task

def openTaskFile():
    try:
        global task_list
        with open("tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            if task != '\n':
                task_list.append(task)
                listbox.insert(END, task)

    except:
        file = open('tasklist.txt', 'w')
        file.close()

def update_entry_with_option(event):
    selected_option = Listaprincipal.get()
    branch_var.set(selected_option)

# Create a new list function
def create_new_list():
    new_branch = branch_var.get().strip()
    if new_branch and new_branch not in OPTIONS:
        OPTIONS.append(new_branch)
        branch_var.set(new_branch)
        menu['menu'].delete(0, 'end')  # Clear the existing options in the OptionMenu
        for branch in OPTIONS:  # Update the OptionMenu with the updated list of branches
            menu['menu'].add_command(label=branch, command=lambda value=branch: Listaprincipal.set(value))

        with open('tasklist.json', 'r') as f:
            data = json.load(f)
            data[new_branch] = []  # Create a new list with an empty list as its value

        with open('tasklist.json', 'w') as fw:
            json.dump(data, fw, indent=4, separators=(',', ': '))

        onBranchSelected()

def toggle_task_status():
    selected_index = listbox.curselection()
    if not selected_index:
        return

    selected_index = selected_index[0]  # The curselection() method returns a tuple; get the first item (index)

    selected_branch = branch_var.get()
    if not selected_branch:
        selected_branch = "default"  # If no branch name is provided, use "default"

    with open('tasklist.json', 'r') as f:
        data = json.load(f)
        if selected_branch in data:
            task_data = data[selected_branch][selected_index]
            task_data["check"] = not task_data["check"]  # Toggle the "check" status

    with open('tasklist.json', 'w') as fw:
        json.dump(data, fw, indent=4, separators=(',', ': '))

    onBranchSelected()  # Refresh the listbox after updating the task status

    

#ícone
Image_Icon=PhotoImage(file="Imagens/task.png")
root.iconphoto(False, Image_Icon)

#barra do topo
TopImage=PhotoImage(file="Imagens/topbar.png")
Label(root,image=TopImage).pack()

dockImage=PhotoImage(file="Imagens/dock.png")
Label(root, image=dockImage,bg="#32405b").place(x=30, y=25)

noteImage=PhotoImage(file="Imagens/task.png")
Label(root, image=noteImage, bg="#32405b").place(x=340, y=20)

heading=Label(root,text="ALL TASKS", font="arial 20 bold", fg="white", bg="#32405b")
heading.place(x=150, y=20)

#main
frame= Frame(root,width=400,height=50,bg="white")
frame.place(x=0, y=180)

task=StringVar()
task_entry=Entry(frame,width=18,font="arial 20", bd=0)
task_entry.place(x=10, y=7)
task_entry.focus()

button=Button(frame,text="Adicionar",font="arial 12 bold",bg="#5a95ff",fg="white",bd=0, command=addTask)
button.place(x=280,y=5)     

# listbox
frame1 = Frame(root, bd=3, width=700, height=280, bg="#32405b")
frame1.pack(pady=(160, 0))

listbox = Listbox(frame1, font=('arial', 12), width=50, height=20, bg="#32405b", fg="white", cursor="hand2", selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH, padx=2)

scrollbar = Scrollbar(frame1, command=listbox.yview)
scrollbar.pack(side=RIGHT, fill=Y)

listbox.config(yscrollcommand=scrollbar.set)


#delete
Delete_icon=PhotoImage(file="Imagens/delete.png")
Button(root, image=Delete_icon, bd=0, command=deleteTask).pack(side=BOTTOM, pady=13)

# Additional branch input
branch_label = Label(root, text="Lista:", font="arial 12 bold", fg="white", bg="#32405b")
branch_label.place(x=35, y=120)

branch_var = StringVar()
branch_entry = Entry(root, textvariable=branch_var, font="arial 12", bd=0)
branch_entry.place(x=80, y=120)
branch_entry.focus()

OPTIONS = []  # List to store branch names

def load_options_from_json():
    with open("tasklist.json", 'r') as file:
        data = json.load(file)
        return list(data.keys())

OPTIONS = load_options_from_json()
Listaprincipal = StringVar(root)
menu = OptionMenu(root, Listaprincipal, *OPTIONS)
menu.place(x=35, y=145)

def update_entry_with_option(event):
    selected_option = Listaprincipal.get()
    branch_var.set(selected_option)

# Bind the update_entry_with_option function to the OptionMenu selection
menu.bind("<Button-1>", update_entry_with_option)

def show_tasks_and_update_entry():
    update_entry_with_option(None)  # Call the function to update the entry with the selected branch
    onBranchSelected()  # Call the onBranchSelected function to repopulate the list of tasks

show_tasks_button = Button(root, text="Mostrar Lista ", font="arial 12 bold", background="#5a95ff", fg="white", bd=0, command=show_tasks_and_update_entry)
show_tasks_button.place(x=250, y=120)

create_list_button = Button(root, text="Criar nova lista ", font="arial 12 bold", background="#5a95ff", fg="white", bd=0, command=create_new_list)
create_list_button.place(x=250, y=150)

# Bind the check button function to the Check Task button
check_button = Button(root, text="Check", font="arial 12 bold", bg="#5a95ff", fg="white", bd=0, command=toggle_task_status)
check_button.place(x=250, y=600)

# Bind the delete button function to the Delete Task button
delete_button = Button(root, text="Delete Task", font="arial 12 bold", bg="#5a95ff", fg="white", bd=0, command=deleteTask)
delete_button.place(x=250, y=550)

openTaskFile()

root.mainloop() 