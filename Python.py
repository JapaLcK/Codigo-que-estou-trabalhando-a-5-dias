import tkinter 
from tkinter import *
import json

root=Tk()
root.title("To-Do-List")
root.geometry("400x650+400+100")
root.resizable(False,False)

task_list= []

def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)

    if task:
        branch = branch_entry.get()
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

        # Clear the listbox and then re-populate it with tasks from the selected branch
        listbox.delete(0, END)
        selected_branch = branch_var.get()
        if selected_branch in data:
            for task_data in data[selected_branch]:
                listbox.insert(END, task_data["taskname"])

def onBranchSelected(event=None):  # Make the event optional to allow manual and button-based calls
    selected_branch = branch_var.get()
    listbox.delete(0, END)
    with open('tasklist.json', 'r') as f:
        data = json.load(f)
        if selected_branch in data:
            for task_data in data[selected_branch]:
                listbox.insert(END, task_data["taskname"])

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

    # Clear the listbox and then re-populate it with tasks from the selected branch
    listbox.delete(0, END)
    if selected_branch in data:
        for task_data in data[selected_branch]:
            listbox.insert(END, task_data["taskname"])


def openTaskFile():

    try:
        global task_list
        with open("tasklist.txt","r") as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            if task !='\n':
                task_list.append(task)
                listbox.insert(END, task)

    except:
        file=open('tasklist.txt', 'w')
        file.close()
     
def update_entry_with_option(event):
    selected_option = Listaprincipal.get()
    branch_var.set(selected_option)
    
    

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

button=Button(frame,text="ADD",font="arial 12 bold",width=6,bg="#5a95ff",fg="#5a95ff",bd=0, command=addTask)
button.place(x=300,y=5) 

# listbox
frame1 = Frame(root, bd=3, width=700, height=280, bg="#32405b")
frame1.pack(pady=(160, 0))

listbox = Listbox(frame1, font=('arial', 12), width=50, height=20, bg="#32405b", fg="white", cursor="hand2", selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH, padx=2)

scrollbar = Scrollbar(frame1, command=listbox.yview)
scrollbar.pack(side=RIGHT, fill=Y)

listbox.config(yscrollcommand=scrollbar.set)


openTaskFile()

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


OPTIONS = load_options_from_json()
Listaprincipal = StringVar(root)
menu = OptionMenu(root, Listaprincipal, *OPTIONS)
menu.place(x=35, y=140)

# Bind the branch selection to onBranchSelected function
branch_var.trace("w", onBranchSelected)

branch_var = StringVar()
branch_entry = Entry(root, textvariable=branch_var, font="arial 12", bd=0)
branch_entry.place(x=80, y=120)
branch_entry.focus()

# Show Tasks button to display tasks from the selected branch
show_tasks_button = Button(root, text="Show Tasks", font="arial 12 bold", background="#5a95ff", fg="#5a95ff", bd=0, command=onBranchSelected)
show_tasks_button.place(x=250, y=120)



root.mainloop() 