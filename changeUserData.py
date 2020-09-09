import datetime


# options for the edit menu
def displayOptions():
    print("""
            1.First Name
            2.Last Name
            3.Email
            4.Password
            5.User type
            6.End of membership
            0.Return to Menu""")


# checks the format of the date
def validateDate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return 1
    except ValueError:
        return 0


# the labels for the inputs
def labels(index):
    lables = {
        1: "New First Name: ",
        2: "New Last Name: ",
        3: "New Email: ",
        4: "New Password: ",
        5: "New User Type: ",
        6: "End of Membership: "
    }
    return lables[int(index)]


# adds the new info in the accounts.txt file
def changeUserData(username):
    accFile = open('accounts.txt', 'r')
    fileContent = accFile.readlines()
    usernameList = []
    for line in fileContent:
        usernameList.append(line.split()[0])
    if usernameList.index(username) > -1:
        row = usernameList.index(username)
        print("Select an option to change data: ")
        displayOptions()
        selectedOption = int(input())
        # checks the selected option if it is 0 returns to choose again
        if selectedOption == 0:
            return 0
        newValue = input(labels(selectedOption))
        if selectedOption == 6:
            while validateDate(newValue) == 0:
                print("Membership End should be in format: YYYY-MM-DD")
                newValue = input("End of membership: ")
        oldRow = fileContent[row].split()
        oldRow[selectedOption] = newValue
        fileContent[row] = " ".join(oldRow)
        for i in range(0, len(fileContent)):
            fileContent[i] = fileContent[i].rstrip()
        content = "\n".join(fileContent)
        with open('accounts.txt', 'w') as file:
            file.write(content)
            print("Data has been changed")
            return 1
    else:
        return 0


