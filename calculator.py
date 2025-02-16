import tkinter as tk


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор")
        self.root.geometry("300x400")
        self.root.configure(bg="#f0f0f0")

        self.create_widgets()

    def create_widgets(self):
        self.entry = tk.Entry(
            self.root, font=("Arial", 18), justify="right", bd=10, relief=tk.RIDGE
        )
        self.entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, pady=10)

        buttons = [
            ("7", 1, 0),
            ("8", 1, 1),
            ("9", 1, 2),
            ("/", 1, 3),
            ("4", 2, 0),
            ("5", 2, 1),
            ("6", 2, 2),
            ("*", 2, 3),
            ("1", 3, 0),
            ("2", 3, 1),
            ("3", 3, 2),
            ("-", 3, 3),
            ("0", 4, 0),
            (".", 4, 1),
            ("=", 4, 2),
            ("+", 4, 3),
        ]

        for text, row, col in buttons:
            btn = tk.Button(
                self.root,
                text=text,
                font=("Arial", 14),
                fg="black",
                bg="#e6e6e6",
                relief=tk.RAISED,
                bd=5,
                command=lambda t=text: self.on_button_click(t),
            )
            btn.grid(
                row=row, column=col, ipadx=15, ipady=15, sticky="nsew", padx=2, pady=2
            )

        for i in range(5):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == "=":
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Помилка")
        else:
            self.entry.insert(tk.END, char)


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
