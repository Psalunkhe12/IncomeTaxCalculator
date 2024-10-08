import tkinter as tk
from tkinter import messagebox
from calendar import monthrange
from datetime import date
# Constants
OLD_REGIME_SLABS = [
    (250000, 0),
    (500000, 0.05),
    (1000000, 0.20),
    (float('inf'), 0.30)
]

NEW_REGIME_SLABS = [
    (250000, 0),
    (500000, 0.05),
    (750000, 0.10),
    (1000000, 0.15),
    (1250000, 0.20),
    (1500000, 0.25),
    (float('inf'), 0.30)
]

SALARIED_SLABS = [
    (300000, 0),
    (700000, 0.05),
    (1000000, 0.10),
    (1200000, 0.15),
    (1500000, 0.20),
    (float('inf'), 0.30)
]

BUSINESS_SLABS = [
    (250000, 0),
    (500000, 0.05),
    (750000, 0.10),
    (1000000, 0.15),
    (1250000, 0.20),
    (1500000, 0.25),
    (float('inf'), 0.30)
]

SENIOR_CITIZEN_SLABS = [
    (300000, 0),
    (1000000, 0.05),
    (float('inf'), 0.30)
]

SUPER_SENIOR_CITIZEN_SLABS = [
    (500000, 0),
    (1000000, 0.20),
    (float('inf'), 0.30)
]

def calculate_tax(income, slabs):
    tax = 0
    for i, (slab, rate) in enumerate(slabs):
        if income > slab:
            if i == 0:
                tax += slab * rate
            else:
                tax += (slab - slabs[i-1][0]) * rate
        else:
            if i == 0:
                tax += income * rate
            else:
                tax += (income - slabs[i-1][0]) * rate
            break
    return tax

def show_results():
    try:
        income = float(entry_income.get())
        occupation = occupation_var.get()
        if income < 0:
            messagebox.showwarning("Input Error", "Please enter a non-negative income amount.")
            return
        if occupation == "Salaried Employee":
            tax = calculate_tax(income, SALARIED_SLABS)
        elif occupation == "Business Owner/Professional":
            tax = calculate_tax(income, BUSINESS_SLABS)
        elif occupation == "Senior Citizen":
            tax = calculate_tax(income, SENIOR_CITIZEN_SLABS)
        elif occupation == "Super Senior Citizen":
            tax = calculate_tax(income, SUPER_SENIOR_CITIZEN_SLABS)
        else:
            tax = calculate_tax(income, NEW_REGIME_SLABS)
        result_text = f"For an annual income of ₹{income:.2f} and occupation {occupation}:\n"
        result_text += f"Your tax is: ₹{tax:.2f}\n"
        messagebox.showinfo("Tax Calculation Results", result_text)
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter a valid income amount.")

def show_tax_slabs():
    tax_slabs_text = "Tax Slabs:\n"
    tax_slabs_text += "Salaried Employees:\n"
    tax_slabs_text += "  - Up to ₹3 lakh: Nil\n"
    tax_slabs_text += "  - ₹3 lakh to ₹7 lakh: 5%\n"
    tax_slabs_text += "  - ₹7 lakh to ₹10 lakh: 10%\n"
    tax_slabs_text += "  - ₹10 lakh to ₹12 lakh: 15%\n"
    tax_slabs_text += "  - ₹12 lakh to ₹15 lakh: 20%\n"
    tax_slabs_text += "  - Above ₹15 lakh: 30%\n"
    tax_slabs_text += "\nBusiness Owners and Professionals:\n"
    tax_slabs_text += "  - Tax liability depends on business income, expenses, and deductions claimed.\n"
    tax_slabs_text += "\nSenior Citizens:\n"
    tax_slabs_text += "  - Up to ₹3 lakh: Nil\n"
    tax_slabs_text += "  - ₹3 lakh to ₹10 lakh: 5% to 20%\n"
    tax_slabs_text += "  - Above ₹10 lakh: 30%\n"
    tax_slabs_text += "\nSuper Senior Citizens:\n"
    tax_slabs_text += "  - Up to ₹5 lakh: Nil\n"
    tax_slabs_text += "  - ₹5 lakh to ₹10 lakh: 20%\n"
    tax_slabs_text += "  - Above ₹10 lakh: 30%\n"
    tax_slabs_text += "\nNRIs (Non-Resident Indians):\n"
    tax_slabs_text += "  - Tax liability depends on residential status, income sources, and double taxation agreements.\n"
    tax_slabs_text += "\nOther Occupations:\n"
    tax_slabs_text += "  - Tax rates apply similarly to other occupations, but the specific details depend on the nature of income (salary, business, capital gains, etc.)."
    messagebox.showinfo("Tax Slabs", tax_slabs_text)

# Create the main window
root = tk.Tk()
root.title("Income Tax Calculator")

# Create a frame for the personal information
frame_personal = tk.Frame(root, bg='#D3D3D3')  # Changed background color
frame_personal.pack(padx=10, pady=10)

# Create labels and entries for personal information
label_name = tk.Label(frame_personal, text="Name:", font=('Arial', 12), fg='#000000', bg='#D3D3D3')  # Changed text color to black
label_name.grid(row=0, column=0, padx=10, pady=10)

entry_name = tk.Entry(frame_personal, font=('Arial', 12), fg='#000000', bg='#ffffff')
entry_name.grid(row=0, column=1, padx=10, pady=10)

label_gender = tk.Label(frame_personal, text="Gender:", font=('Arial', 12), fg='#000000', bg='#D3D3D3')  # Changed text color to black
label_gender.grid(row=1, column=0, padx=10, pady=10)

gender_var = tk.StringVar()
gender_var.set("Male")

def update_gender_font():
    if gender_var.get() == "Male":
        option_male.config(font=('Arial', 12, 'bold'))
        option_female.config(font=('Arial', 12))
    else:
        option_female.config(font=('Arial', 12, 'bold'))
        option_male.config(font=('Arial', 12))

option_male = tk.Radiobutton(frame_personal, text="Male", variable=gender_var, value="Male", font=('Arial', 12), fg='#000000', bg='#D3D3D3', command=update_gender_font)  # Changed text color to black
option_male.grid(row=1, column=1, padx=10, pady=10)

option_female = tk.Radiobutton(frame_personal, text="Female", variable=gender_var, value="Female", font=('Arial', 12), fg='#000000', bg='#D3D3D3', command=update_gender_font)  # Changed text color to black
option_female.grid(row=1, column=2, padx=10, pady=10)

label_occupation = tk.Label(frame_personal, text="Occupation:", font=('Arial', 12), fg='#000000', bg='#D3D3D3')  # Changed text color to black
label_occupation.grid(row=2, column=0, padx=10, pady=10)

occupation_var = tk.StringVar()
occupation_var.set("Salaried Employee")

def update_occupation_font():
    if occupation_var.get() == "Salaried Employee":
        option_salaried.config(font=('Arial', 12, 'bold'))
        option_business.config(font=('Arial', 12))
        option_senior.config(font=('Arial', 12))
        option_super_senior.config(font=('Arial', 12))
        option_other.config(font=('Arial', 12))
        option_nri.config(font=('Arial', 12))
    elif occupation_var.get() == "Business Owner/Professional":
        option_business.config(font=('Arial', 12, 'bold'))
        option_salaried.config(font=('Arial', 12))
        option_senior.config(font=('Arial', 12))
        option_super_senior.config(font=('Arial', 12))
        option_other.config(font=('Arial', 12))
        option_nri.config(font=('Arial', 12))
    elif occupation_var.get() == "Senior Citizen":
        option_senior.config(font=('Arial', 12, 'bold'))
        option_salaried.config(font=('Arial', 12))
        option_business.config(font=('Arial', 12))
        option_super_senior.config(font=('Arial', 12))
        option_other.config(font=('Arial', 12))
        option_nri.config(font=('Arial', 12))
    elif occupation_var.get() == "Super Senior Citizen":
        option_super_senior.config(font=('Arial', 12, 'bold'))
        option_salaried.config(font=('Arial', 12))
        option_business.config(font=('Arial', 12))
        option_senior.config(font=('Arial', 12))
        option_other.config(font=('Arial', 12))
        option_nri.config(font=('Arial', 12))
    elif occupation_var.get() == "NRI":
        option_nri.config(font=('Arial', 12, 'bold'))
        option_salaried.config(font=('Arial', 12))
        option_business.config(font=('Arial', 12))
        option_senior.config(font=('Arial', 12))
        option_super_senior.config(font=('Arial', 12))
        option_other.config(font=('Arial', 12))
    else:
        option_other.config(font=('Arial', 12, 'bold'))
        option_salaried.config(font=('Arial', 12))
        option_business.config(font=('Arial', 12))
        option_senior.config(font=('Arial', 12))
        option_super_senior.config(font=('Arial', 12))
        option_nri.config(font=('Arial', 12))

option_salaried = tk.Radiobutton(frame_personal, text="Salaried Employee", variable=occupation_var, value="Salaried Employee", font=('Arial', 12), fg='#000000', bg='#D3D3D3', command=update_occupation_font)  # Changed text color to black
option_salaried.grid(row=2, column=1, padx=10, pady=10)

option_business = tk.Radiobutton(frame_personal, text="Business Owner/Professional", variable=occupation_var, value="Business Owner/Professional", font=('Arial', 12), fg='#000000', bg='#D3D3D3', command=update_occupation_font)  # Changed text color to black
option_business.grid(row=2, column=2, padx=10, pady=10)

option_senior = tk.Radiobutton(frame_personal, text="Senior Citizen", variable=occupation_var, value="Senior Citizen", font=('Arial', 12), fg='#000000', bg='#D3D3D3', command=update_occupation_font)  # Changed text color to black
option_senior.grid(row=3, column=1, padx=10, pady=10)

option_super_senior = tk.Radiobutton(frame_personal, text="Super Senior Citizen", variable=occupation_var, value="Super Senior Citizen", font=('Arial', 12), fg='#000000', bg='#D3D3D3', command=update_occupation_font)  # Changed text color to black
option_super_senior.grid(row=3, column=2, padx=10, pady=10)

option_nri = tk.Radiobutton(frame_personal, text="NRI", variable=occupation_var, value="NRI", font=('Arial', 12), fg='#000000', bg='#D3D3D3', command=update_occupation_font)  # Changed text color to black
option_nri.grid(row=4, column=1, padx=10, pady=10)

option_other = tk.Radiobutton(frame_personal, text="Other", variable=occupation_var, value="Other", font=('Arial', 12), fg='#000000', bg='#D3D3D3', command=update_occupation_font)  # Changed text color to black
option_other.grid(row=4, column=2, padx=10, pady=10)

label_income = tk.Label(frame_personal, text="Income:", font=('Arial', 12), fg='#000000', bg='#D3D3D3')  # Changed text color to black
label_income.grid(row=5, column=0, padx=10, pady=10)

entry_income = tk.Entry(frame_personal, font=('Arial', 12), fg='#000000', bg='#ffffff')
entry_income.grid(row=5, column=1, padx=10, pady=10)


# Create a button to calculate tax
button_calculate = tk.Button(root, text="Calculate Tax", command=show_results, font=('Arial', 12), fg='#000000', bg='#87ceeb')
button_calculate.pack(padx=10, pady=10)

# Create a button to show tax slabs
button_tax_slabs = tk.Button(root, text="Tax Slabs", command=show_tax_slabs, font=('Arial', 12), fg='#000000', bg='#87ceeb')
button_tax_slabs.pack(padx=10, pady=10)

# Start the GUI event loop
root.mainloop()