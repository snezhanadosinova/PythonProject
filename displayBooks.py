# removes commas from one line of allBooks.txt file and returns the list of books
def remove_commas(book_list):
    book_list[0] = book_list[0].replace('"', '').replace('"', '')
    book_list[1] = book_list[1].replace('"', '').replace('"', '')
    book_list[2] = book_list[2].replace('"', '').replace('"', '')
    book_list[3] = book_list[3].replace('"', '').replace('"', '')
    book_list[4] = book_list[4].replace('"', '').replace('"', '')
    book_list[5] = book_list[5].replace('"', '').replace('"', '')
    book_list[6] = book_list[6].replace('"', '').replace('"', '')
    return book_list


# shows the books one by one
def display_books():
    accFile = open('allBooks.txt', 'r')
    fileContent = accFile.readlines()
    for book in fileContent:
        book_list = book.split(',')
        book_list = remove_commas(book_list)
        print(f"Name: {book_list[0]}")
        print(f"Author: {book_list[1]}")
        print(f"Publisher: {book_list[2]}")
        print(f"Genre {book_list[3]}")
        print(f"Year {book_list[4]}")
        print(f"Quantity: {book_list[5]}")
        print(f"Available: {book_list[6]}")
        print("")

