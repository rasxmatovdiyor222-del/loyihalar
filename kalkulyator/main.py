import tkinter as tk


class Calculyator:
    def __init__(self, root):
        self.root = root
        self.root.title("Kalkulyator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        self.expression = ""
        self.input_text = tk.StringVar()

        self.create_screen()

        self.create_buttions()

    def create_screen(self):
        screen_frame = tk.Frame(self.root, width=300, height=50, bd=0, highlightbackground="black",
                                highlightcolor="black", highlightthickness=1)
        screen_frame.pack(side=tk.TOP)

        screen = tk.Entry(screen_frame, font=('Arial',20 , 'bold'), textvariable=self.input_text, width=50, bg="#eee",
                          bd=0, justify=tk.RIGHT)
        screen.grid(row=0, column=0)
        screen.pack(ipady=10)

    def create_buttions(self):
        btns_frame = tk.Frame(self.root, width=300, height=350, bg="grey")
        btns_frame.pack()

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0)
        ]

        for (text, row, col) in buttons:
            btn = tk.Button(btns_frame, text=text, fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                            command=lambda txt=text: self.on_button_click(txt))
            btn.grid(row=row, column=col, padx=1, pady=1)

    def on_button_click(self, char):
        if char == '=':
            try:
                result = str(eval(self.expression))
                self.input_text.set(result)
            except Exception as e:
                self.input_text.set("xatolik")
                self.expression = ""
        elif char == 'C':
            self.expression = ""
            self.input_text.set("")
        else:
            self.expression += str(char)
            self.input_text.set(self.expression)


if __name__ == '__main__':
    root = tk.Tk()
    calc = Calculyator(root)
    root.mainloop()





