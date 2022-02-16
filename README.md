Library through the console
This is a program that accepts input from a user to add information about a book, and displays them on the console.

Table of contents
Overview
The challenge
Links
My process
Built with
What I learned
Continued development
Useful resources
Author
Note: Delete this note and update the table of contents based on what sections you keep.

Overview
The challenge
Users should be able to:

Add book name, author name and rating for the book.
See books displayed in the console after adding them.


Links
Solution URL: https://github.com/N-Endy/python_library
Live Site URL: Through Console
My process
Built with
Python basics

What I learned
I learnt how to properly use functions, to make sure a function performs just one job.
Learnt how to manipulate data in a dictionary.

To see how you can add code snippets, see below:

<h1>Some codes I'm proud of</h1>
def valid_input(prompt, values):
        choice = input(prompt)
        if choice in values:
            return choice
        else:
            print_pause('Please put in a valid choice')

def add_books(name, author, rating):
        book = {"name_of_book": name,
                "name_of_author": author,
                "book_rating": rating}
        our_library.append(book)
        add_more_books()

Continued development
I'm currently learning Python for Data Science and wanted to use knowledge from what I've learnt to practice. I hope to move further into learning MySQL and other programs (Pandas)

Useful resources
Ustacky - This is my main resource for learning Data Science with Python.
Udacity - My initiate introduction to Python was from this resource. It opened me up to accepting and loving Python.

Author
Website - In progress
Twitter - @NELtheDev