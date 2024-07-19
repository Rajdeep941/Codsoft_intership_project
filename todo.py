import tkinter as tk
from tkinter import ttk, messagebox

class TodoApp:
    def __init__(self, root):
        self.tasks = []
        self.root = root
        self.root.title("To-Do List Application")
        self.style = ttk.Style()
        self.style.theme_use("clam")

        # Style configuration
        self.style.configure("TButton", padding=6, relief="flat", background="#4CAF50", foreground="white")
        self.style.configure("TFrame", background="#f0f0f0")
        self.style.configure("TLabel", background="#f0f0f0", font=("Arial", 12))
        self.style.configure("TEntry", padding=6, font=("Arial", 12))
        self.style.configure("TListbox", font=("Arial", 12))

        self.frame = ttk.Frame(root, padding="10")
        self.frame.pack(pady=10)

        self.task_listbox = tk.Listbox(self.frame, width=50, height=10, font=("Arial", 12))
        self.task_listbox.pack(side=tk.LEFT, padx=(0, 10))

        self.scrollbar = ttk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        self.entry = ttk.Entry(root, width=50, font=("Arial", 12))
        self.entry.pack(pady=10)

        self.add_button = ttk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.delete_button = ttk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.update_button = ttk.Button(root, text="Mark as Done", command=self.mark_done)
        self.update_button.pack(pady=5)

    def add_task(self):
        task = self.entry.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.update_task_list()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks.pop(selected_task_index[0])
            self.update_task_list()
        else:
            messagebox.showwarning("Warning", "You must select a task.")

    def mark_done(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks[selected_task_index[0]]["completed"] = True
            self.update_task_list()
        else:
            messagebox.showwarning("Warning", "You must select a task.")

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "Done" if task["completed"] else "Pending"
            self.task_listbox.insert(tk.END, f"{task['task']} - {status}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
