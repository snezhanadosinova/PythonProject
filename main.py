from login import loginScreen  # import loginScreen function
from changePassword import changePassword  # import changePassword function
from changeUserData import changeUserData, validateDate  # import changeUser data function
from registerUser import *  # import all functions from registerUser
from addBook import *  # import all functions from addBook
from displayBooks import display_books


def main():
    # Main function
    logged_in = 0
    already_been_displayed = 0  # state flag for the different screens of the system
    endless = 1

    def sysMenus(first_name, user_type):
        if len(first_name) == 0:
            first_name = "Someone"

        if already_been_displayed == 0:
            print(f"""Hello {first_name}, welcome to our platform, please select an option from the menu""")
        else:
            print("""Please select an option from the menu:""")
        # Sub-function for the menus after the user has logged in
        if user_type == 'admin':
            print("""
                    1. Change password
                    2. Register a person
                    3. Edit personal data
                    4. Exit""")
        elif user_type == 'librarian':
            print("""
                    1. Change password
                    2. Add new book entries
                    3. Exit""")
        elif user_type == 'reader':
            print("""
                    1. Display Books
                    2. Exit""")
        else:
            print("""Your user type is undefined, contact a system administrator""")
            loginScreen()

    # registration function
    def registration_data():
        username = input("Username: ")
        first = input("First Name: ")
        last = input("Last Name: ")
        email = input("Email: ")
        passw = input("Password: ")
        type = input("User type: ")
        membership_end = input("End of membership: ")
        while validateDate(membership_end) == 0:
            print("Membership End should be in format: YYYY-MM-DD")
            membership_end = input("End of membership: ")
        user_data = [username, first, last, email, passw, type, membership_end]
        return user_data

    def book_entry_data():
        title = input("Book title: ")
        writer = input("Writer's Name: ")
        publisher = input("Publisher: ")
        year = input("Year published: ")
        genre = input("Genre: ")
        number = input("Books number: ")
        available = input("Book availability: ")
        book_data = [title, writer, publisher, year, genre, number, available]
        return book_data
    # logout function
    def logout():
        already_been_displayed = 0
        print("You've logged out")

    while endless:
        if logged_in == 0:
            user_data = loginScreen()
        user_index_found = user_data[0]
        if user_index_found > -1:
            first_name = user_data[1]
            user_type = user_data[2]
            sysMenus(first_name, user_type)
            selected_option = int(input("Select Menu option: "))
            if user_type == 'admin':
                logged_in = 1
                already_been_displayed = 1
                if selected_option == 1:
                    changePassword(user_index_found)
                elif selected_option == 2:
                    new_user_data = registration_data()
                    while createNewUser(new_user_data) == 0:
                        new_user_data = registration_data()
                        createNewUser(new_user_data)
                    else:
                        print("User has been created")
                elif selected_option == 3:
                    username = input("Provide the username of the user that will be altered: ")
                    repeat_change_user_data = changeUserData(username)
                    while repeat_change_user_data:
                        repeat_change_user_data = changeUserData(username)
                    else:
                        print("Exited Mode")
                elif selected_option == 4:
                    logged_in = 0
                    logout()
                else:
                    print("This option doesn't exist")
            elif user_type == 'librarian':
                logged_in = 1
                already_been_displayed = 1
                if selected_option == 1:
                    changePassword(user_index_found)
                elif selected_option == 2:
                    book_data = book_entry_data()
                    if addNewBook(book_data) == 0:
                        print("The book is already in the system! Please, add new book")
                        book_data = book_entry_data()
                        addNewBook(book_data)
                    else:
                        print("Book added successfully!")
                elif selected_option == 3:
                    logged_in = 0
                    logout()
                else:
                    print("This option doesn't exist")
            elif user_type == 'reader':
                logged_in = 1
                already_been_displayed = 1
                if selected_option == 1:
                    display_books()
                elif selected_option == 2:
                    logged_in = 0
                    logout()
                else:
                    print("This option doesn't exist")


main()
