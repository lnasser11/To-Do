import tkinter as tk
import pickle

def add_item(event=None):
    text_inserted = text_box.get()
    if text_inserted:
        list_box.insert(tk.END, text_inserted)
        text_box.delete(0, tk.END)
        save_todo_list()

def delete_item(event=None):
    selected_index = list_box.curselection()
    if selected_index:
        list_box.delete(selected_index)
        save_todo_list()

def load_todo_list():
    try:
        with open("todo_list.pkl", "rb") as file:
            items = pickle.load(file)
            for item in items:
                list_box.insert(tk.END, item)
    except FileNotFoundError:
        pass

def save_todo_list():
    items = list_box.get(0, tk.END)
    with open("todo_list.pkl", "wb") as file:
        pickle.dump(items, file)

root = tk.Tk()
root.geometry("360x450")
root.title("To-Do List by Over-Q")

text_box = tk.Entry(root, width=30, font=("Helvetica", 12), justify=tk.CENTER, border=(2))
text_box.bind("<Return>", add_item)
text_box.pack()

add_text = tk.Button(root, text="Add Task", command=add_item)
add_text.pack()

delete_text = tk.Button(root, text="Delete Task", command=delete_item)
delete_text.pack()

separator = tk.Frame(height=2, bd=1, relief="sunken")
separator.pack(fill="x", padx=5, pady=5)

list_box = tk.Listbox(root, width=30, height=20, font=("Helvetica", 12), selectmode=tk.SINGLE)
list_box.pack()
list_box.bind("<Delete>", delete_item)
list_box.bind("<BackSpace>", delete_item)

load_todo_list()

root.mainloop()
