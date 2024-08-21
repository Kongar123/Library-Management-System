from prettytable import PrettyTable
from datetime import datetime
from pyfiglet import Figlet
import cowsay
import json
import sys
import re


books = []
members = []
transactions = []
books_table = PrettyTable()
members_table = PrettyTable()
transactions_table = PrettyTable()

def add_book(isbn, title, author, copies):
    books.append({"ISBN":isbn, "Title":title, "Author":author, "Copies":copies})
    print(f"{title}'s book is added")

def add_member(member_id, name):
    members.append({"Member ID": member_id, "Name": name, "Borrowed Books": []})
    print(f"({name}) is added")

def search_books(query):
    return [book for book in books if query == book["ISBN"] or query.lower() in book["Title"].lower() or query.lower() in book["Author"].lower()]

def issue_book(member_id, isbn):
    for book in books:
        if book["ISBN"] == isbn and book["Copies"] > 0:
            for member in members:
                if member["Member ID"] == member_id:
                    member["Borrowed Books"].append(isbn)
                    book["Copies"] -= 1
                    transactions.append({
                        "Member ID": member_id,
                        "ISBN": isbn,
                        "Returned": "No",
                        "Date": datetime.now().date().strftime('%Y-%m-%d'),
                        "Time": datetime.now().time().strftime('%H:%M:%S.%f')
                    })
                    return "Book issued successfully."
    return "Book not available."

def return_book(member_id, isbn):
    for member in members:
        if member["Member ID"] == member_id and isbn in member["Borrowed Books"]:
            member["Borrowed Books"].remove(isbn)
            for book in books:
                if book["ISBN"] == isbn:
                    book["Copies"] += 1
            transactions.append({
                "Member ID": member_id,
                "ISBN": isbn,
                "Returned": "Yes",
                "Date": datetime.now().date().strftime('%Y-%m-%d'),
                "Time": datetime.now().time().strftime('%H:%M:%S.%f')
            })
            return "Book returned successfully."
    return "Return failed. Book not borrowed or wrong Member."

def view_transactions():
    transactions_table.field_names = ["Member ID", "ISBN", "Date", "Time", "Returned"]
    for transaction in transactions:
        transactions_table.add_row([
            transaction["Member ID"], 
            transaction["ISBN"],  
            transaction["Date"], 
            transaction["Time"],
            transaction["Returned"]
        ])
    print(transactions_table)
    transactions_table.clear_rows()



def view_books():
    books_table.field_names = ["ISBN", "Title", "Author", "Copies"]
    for book in books:
        books_table.add_row([book["ISBN"], book["Title"], book["Author"], book["Copies"]])
    print(books_table)
    books_table.clear_rows()

def view_members():
    members_table.field_names = ["Member ID", "Name","Borrowed Books"]
    for member in members:
        members_table.add_row([member["Member ID"], member["Name"], member["Borrowed Books"]])
    print(members_table)
    members_table.clear_rows()

def is_valid_isbn(isbn):
    pattern = r'^978\d{10}$'
    if re.match(pattern, isbn):
        return True
    return False

def is_isbn_exist(isbn):
    for book in books:
        if isbn in book["ISBN"]:
            return True
    return False

def is_member_exist(id):
    for member in members:
        if id == member["Member ID"]:
            return True
    return False

def save_data_as_json(filename="data.json"):
    data = {
        "books": books,
        "members": members,
        "transactions": transactions
    }
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    cowsay.beavis("Data saved successfully!")

def load_data_from_json(filename="data.json"):
    global books, members, transactions
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            books = data.get("books", [])
            members = data.get("members", [])
            transactions = data.get("transactions", [])
    except FileNotFoundError:
        pass


def main():

    load_data_from_json()

    while True:
        fig = Figlet(font="twopoint")
        print(fig.renderText("Library Management System"))
        print("1. Add Book")
        print("2. Search Books")
        print("3. Add Member")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. View Transactions")
        print("7. View Books")
        print("8. View Members")
        print("9. Exit")
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                while True:
                    isbn = input("Enter ISBN: ")
                    if is_valid_isbn(isbn):
                        if is_isbn_exist(isbn):
                            print("This ISBN is used")
                            continue
                        break
                    else:
                        print("Invalid ISBN format")
                title = input("Enter Title: ")
                author = input("Enter Author: ")
                while True:
                    try:
                        copies = int(input("Enter Number of Copies: "))
                        if copies < 0:
                            raise TypeError()
                        break
                    except ValueError:
                        print("Only numbers are accepted!")
                    except TypeError as e:
                        print("Negative is not allowed!")
                add_book(isbn, title, author, copies)
            case '2':
                query = input("Enter search query (Title/Author/ISBN): ")
                results = search_books(query)
                if results != []:
                    for book in results:
                        print(book)
                else:
                    print("Book is not found!")
            case '3':
                while True:
                    try:
                        member_id = int(input("Enter Member ID: "))
                        if is_member_exist(member_id):
                            print("This id is already exist")
                            continue
                        break
                    except ValueError:
                        print("Only numbers are accepted!")
                name = input("Enter Member Name: ")
                add_member(member_id, name)
            case'4':
                if members == [] or books == []:
                    print("No members or Books have been added yet!")
                    continue
                while True:
                    try:
                        member_id = int(input("Enter Member ID: "))
                        if is_member_exist(member_id):
                            break
                        else:
                            print("Member does not exist!")
                    except ValueError:
                        print("Only numbers are accepted!")
                while True:
                    isbn = input("Enter ISBN: ")
                    if is_valid_isbn(isbn):
                        if is_isbn_exist(isbn):
                            break
                        else:
                            print("Book is not found!")
                    else:
                        print("Invalid ISBN format")
                print(issue_book(member_id, isbn))
            case '5':
                if members == [] or books == []:
                    print("No members or Books have been added yet!")
                    continue
                while True:
                    try:
                        member_id = int(input("Enter Member ID: "))
                        if is_member_exist(member_id):
                            break
                        else:
                            print("Member does not exist!")
                    except ValueError:
                        print("Only numbers are accepted!")
                while True:
                    isbn = input("Enter ISBN: ")
                    if is_valid_isbn(isbn):
                        if is_isbn_exist(isbn):
                            break
                        print("Book is not found!")
                    else:
                        print("Invalid ISBN format!")
                print(return_book(member_id, isbn))
            case '6':
                view_transactions()
            case '7':
                view_books()
            case '8':
                view_members()
            case '9':
                save_data_as_json()
                sys.exit()
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
