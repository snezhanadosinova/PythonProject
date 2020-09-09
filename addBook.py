from book import Book


def setBookData(bookData):
    book = Book(bookData[0], bookData[1], bookData[2], bookData[3], bookData[4], bookData[5], bookData[6])
    return book


# adds the book to the allBooks.txt file
def addNewBook(bookData):
    book = setBookData(bookData)
    bookFile = open('allBooks.txt', 'r')
    fileContent = bookFile.readlines()
    bookTitleList = []
    for line in fileContent:
        bookTitleList.append(line.split(',')[0])  # put all book titles in a list
    bookFile.close()
    try:
        if bookTitleList.index(book.title):  # check if the index of the book
            return 0
    except ValueError:
        with open('allBooks.txt', 'w') as file:
            fileContent.append("\n" + '","'.join(['"' + book.title, book.writer, book.publisher, book.year, book.genre, book.number, book.available + '"']))
            file.write(''.join(fileContent))
            return 1
