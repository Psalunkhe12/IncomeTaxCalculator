import tkinter as tk

class TaxCalculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Tax Calculator')
        self.window.geometry('400x250')
        self.window.resizable(False, False)

        self.income_label = tk.Label(self.window, text="Income:", font=('Ariel', 15))
        self.income_label.pack()
        self.income_entry = tk.Entry(self.window)
        self.income_entry.pack(ipady=5)

        self.tax_rate_label = tk.Label(self.window, text="Tax Rate (%):", font=('Ariel', 15))
        self.tax_rate_label.pack()
        self.tax_rate_entry = tk.Entry(self.window)
        self.tax_rate_entry.pack(ipady=5)

        self.calculate_button = tk.Button(self.window, text="Calculate Tax", font=('Ariel', 15), height=1, command=self.calculate_tax)
        self.calculate_button.pack()

        self.result_label = tk.Label(self.window, text="", font=('Ariel', 10))
        self.result_label.pack()

    def calculate_tax(self):
        try:
            income = float(self.income_entry.get())
            tax_rate = float(self.tax_rate_entry.get())
            tax = income * (tax_rate / 100)
            self.result_label.config(text=f"Tax: ${tax:.2f}", font=('Ariel', 11))
        except ValueError:
            self.result_label.config(text="Invalid input", font=('Ariel', 12))

    def run(self):
        self.window.mainloop()

if __name__ == '__main__':
    obj = TaxCalculator()
    obj.run()