import time


# Make a book list that asks for input and pushes
# it to a list which displays a list of books
def library():
    our_library = []

    def print_pause(message):
        time.sleep(1)
        print(message)

    def valid_input(prompt, values):
        choice = input(prompt)
        if choice in values:
            return choice
        else:
            print_pause('Please put in a valid choice')

    def valid_input_number(prompt):
        choice = input(prompt)
        choice = float(choice)
        if type(choice) is float:
            return choice
        else:
            print_pause('Please input correct data')
            valid_input_number(prompt)

    def user_input():
        book_name = input("What is the name of the book?: ").title()
        author = input("What is name of author?: ").title()
        rating = valid_input_number("Rating of book out of 10?: ")

        while rating > 10:
            print_pause('Please select a figure greater than 0 and less than 10')
            rating = valid_input_number("Rating of book out of 10?: ")

        add_books(book_name, author, rating)

    def add_books(name, author, rating):
        book = {"name_of_book": name,
                "name_of_author": author,
                "book_rating": rating}
        our_library.append(book)
        add_more_books()

    def print_books():
        for book in our_library:
            for key, value in book.items():
                print(f"{key} : {value} \n")

    def add_more_books():
        user_choice = valid_input("Do you want to add more books? "
                                  "choose an option[y/n]: ", ['y', 'n'])
        if user_choice == 'y':
            user_input()
        elif user_choice == 'n':
            print_pause('Thank you for using our Library')
            print_books()
        else:
            add_more_books()

    add_more_books()


library()
