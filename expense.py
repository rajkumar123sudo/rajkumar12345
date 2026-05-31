username = "admin"
password = "1234"

u = input("Enter Username: ")
p = input("Enter Password: ")

if u == username and p == password:
    print("Login Successful")

else:
    print("Invalid Login")

# i am create a matplotlib graph to show the expenses in a pie chart
import matplotlib.pyplot as plt
import csv

def plot_expenses():
            categories = []
            amounts = []

            with open("expenses.txt", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    categories.append(row[0])
                    amounts.append(int(row[1]))

            plt.pie(amounts, labels=categories, autopct='%1.1f%%')
            plt.title("Expense Distribution")
            plt.show()

plot_expenses()

def add_expense():
    item = input("Enter Expense Name: ")
    amount = input("Enter Amount: ")

    file = open("expenses.txt", "a")
    file.write(item + "," + amount + "\n")
    file.close()

    print("Expense Added Successfully")


def view_expenses():

    file = open("expenses.txt", "r")

    data = file.readlines()

    total = 0

    print("\n===== Expense List =====\n")

    for line in data:

        item, amount = line.strip().split(",")

        print("Item:", item)
        print("Amount:", amount)

        total += int(amount)

        print("----------------")

    print("Total Expense =", total)

    file.close()


while True:

    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        print("Thank You")
    break 

else:
        print("Invalid Choice")
        
       