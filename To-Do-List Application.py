import tkinter as tk
from tkinter import messagebox

# Function to add or update a task
def add_or_update_task():
    task = task_entry.get()
    if task != "":
        if edit_mode.get():
            tasks_listbox.delete(edit_index.get())
            tasks_listbox.insert(edit_index.get(), task)
            edit_mode.set(False)
            add_task_button.config(text="Add Task")
        else:
            tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Function to delete a selected task
def delete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except:
        messagebox.showwarning("Warning", "You must select a task to delete.")

# Function to edit a selected task
def edit_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        task = tasks_listbox.get(selected_task_index)
        task_entry.delete(0, tk.END)
        task_entry.insert(tk.END, task)
        edit_index.set(selected_task_index)
        edit_mode.set(True)
        add_task_button.config(text="Update Task")
    except:
        messagebox.showwarning("Warning", "You must select a task to edit.")

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create a frame for the listbox and scrollbar
frame = tk.Frame(root)
frame.pack(pady=10)

# Create a listbox to display tasks
tasks_listbox = tk.Listbox(
    frame,
    width=50,
    height=10,
    bd=0,
    font=("Helvetica", 12),
    selectbackground="#a6a6a6"
)
tasks_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

# Create a scrollbar for the listbox
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

tasks_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=tasks_listbox.yview)

# Create an entry box to add new tasks
task_entry = tk.Entry(
    root,
    font=("Helvetica", 12)
)
task_entry.pack(pady=20)

# Create a button to add or update tasks
add_task_button = tk.Button(
    root,
    text="Add Task",
    command=add_or_update_task
)
add_task_button.pack(pady=10)

# Create a button to delete tasks
delete_task_button = tk.Button(
    root,
    text="Delete Task",
    command=delete_task
)
delete_task_button.pack(pady=10)

# Create a button to edit tasks
edit_task_button = tk.Button(
    root,
    text="Edit Task",
    command=edit_task
)
edit_task_button.pack(pady=10)

# Variables to keep track of edit mode and index
edit_mode = tk.BooleanVar(value=False)
edit_index = tk.IntVar(value=-1)

# Run the application
root.mainloop()
