import tkinter as tk
from tkinter import simpledialog, messagebox  # Import simpledialog here
import pickle


class TodoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")

        self.tasks = self.load_tasks()

        self.task_listbox = tk.Listbox(self.master, selectmode=tk.SINGLE, height=15, width=40)
        self.task_listbox.pack(pady=10)

        self.update_task_listbox()

        add_button = tk.Button(self.master, text="Add Task", command=self.add_task)
        add_button.pack(pady=5)

        done_button = tk.Button(self.master, text="Mark as Done", command=self.mark_as_done)
        done_button.pack(pady=5)

        remove_button = tk.Button(self.master, text="Remove Task", command=self.remove_task)
        remove_button.pack(pady=5)

        save_button = tk.Button(self.master, text="Save Tasks", command=self.save_tasks)
        save_button.pack(pady=5)

        self.master.protocol("WM_DELETE_WINDOW", self.on_close)

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task, done in self.tasks.items():
            status = "Done" if done else "Not Done"
            self.task_listbox.insert(tk.END, f"{task} - {status}")

    def add_task(self):
        task = simpledialog.askstring("Add Task", "Enter the task:")
        if task:
            self.tasks[task] = False
            self.update_task_listbox()

    def mark_as_done(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task = list(self.tasks.keys())[selected_index[0]]
            self.tasks[task] = True
            self.update_task_listbox()

    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task = list(self.tasks.keys())[selected_index[0]]
            del self.tasks[task]
            self.update_task_listbox()

    def save_tasks(self):
        with open("tasks.pkl", "wb") as f:
            pickle.dump(self.tasks, f)
        messagebox.showinfo("Saved", "Tasks saved successfully!")

    def load_tasks(self):
        try:
            with open("tasks.pkl", "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            return {}

    def on_close(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.save_tasks()
            self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
