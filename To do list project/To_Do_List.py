import tkinter as tk
from tkinter import messagebox


# Function to add a task
def add_task():
    new_task = entry.get()
    if new_task:
        if new_task not in to_do_list:
            to_do_list.append(new_task)
            entry.delete(0, tk.END)
            update_task_list()
        else:
            messagebox.showwarning("Warning", "Task already exists in the list!")
    else:
        messagebox.showwarning("Warning", "Please enter a task!")


# Function to update the task list
def update_task_list():
    task_list.delete(0, tk.END)
    for index, task in enumerate(to_do_list, start=1):
        task_list.insert(tk.END, f"{index}. {task}")


# Function to delete selected tasks
def delete_selected_tasks():
    selected_tasks = task_list.curselection()
    if selected_tasks:
        for index in selected_tasks[::-1]:
            del to_do_list[index]
        update_task_list()


# Function to handle "Enter" key press
def handle_enter_key(event):
    add_task()


# Create the main window
root = tk.Tk()
root.title("To-Do List Application")

# Create a label
label = tk.Label(root, text="Enter a Task:")
label.pack(pady=10)

# Create an entry widget
entry = tk.Entry(root, width=30)
entry.pack()

# Bind the "Enter" key press to the handle_enter_key function
entry.bind("<Return>", handle_enter_key)

# Create an "Add" button
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=10)

# Create a Canvas to contain the Listbox and Scrollbar
canvas = tk.Canvas(root, width=300, height=200)
canvas.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create a Listbox to display tasks with multiple selections
task_list = tk.Listbox(canvas, width=50, selectmode=tk.MULTIPLE)
task_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a vertical scrollbar
vertical_scrollbar = tk.Scrollbar(canvas, command=task_list.yview)
task_list.config(yscrollcommand=vertical_scrollbar.set)

# Pack the vertical scrollbar to the right of the Listbox
vertical_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create a "Delete Selected Tasks" button
delete_button = tk.Button(root, text="Delete Selected Tasks", command=delete_selected_tasks)
delete_button.pack(pady=10)

# Initialize the task list
to_do_list = []

# Run the Tkinter main loop
root.mainloop()
