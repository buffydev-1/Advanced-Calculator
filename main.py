from tkinter import Tk, Button, Entry, StringVar, Label

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("315x510")
        self.root.configure(background='grey')
        
        self.operator = ""
        self.input_var = StringVar()
        
        self.create_widgets()
    
    def btn_click(self, num):
        self.operator += str(num)
        self.input_var.set(self.operator)
    
    def clear(self):
        self.operator = ""
        self.input_var.set("")
    
    def evaluate(self):
        try:
            result = str(eval(self.operator))
            self.input_var.set(result)
            self.operator = ""
        except:
            self.input_var.set("Error")
            self.operator = ""
    
    def create_widgets(self):
        Label(self.root, font=('Arial', 20, 'bold'), text='Calculator', bg='grey', fg='black').grid(columnspan=4)
        Entry(self.root, font=('Arial', 20, 'bold'), textvariable=self.input_var, insertwidth=7, bd=5, bg="white", justify='right').grid(columnspan=4)
        
        buttons = [
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('+', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('*', 4, 3),
            ('0', 5, 0), ('C', 5, 1), ('.', 5, 2), ('/', 5, 3)
        ]
        
        for (text, row, col) in buttons:
            if text == 'C':
                cmd = self.clear
            else:
                cmd = lambda t=text: self.btn_click(t)
            Button(self.root, text=text, padx=16, pady=16, bd=4, fg="black", font=('Arial', 20, 'bold'), bg="grey", command=cmd).grid(row=row, column=col)
        
        Button(self.root, text="=", padx=16, pady=16, bd=4, width=16, fg="black", font=('Arial', 20, 'bold'), bg="grey", command=self.evaluate).grid(columnspan=4)

if __name__ == "__main__":
    root = Tk()
    Calculator(root)
    root.mainloop()