from user import User


def setUserData(userData):
    user = User(userData[0], userData[1], userData[2], userData[3], userData[4], userData[5], userData[6])
    return user

# adds new user to the accounts.txt file
def createNewUser(userData):
    user = setUserData(userData)
    accFile = open('accounts.txt', 'r')
    fileContent = accFile.readlines()
    usernameList = []
    for line in fileContent:
        usernameList.append(line.split()[0])  # put all usernames in a list (column 0 from the text file)
    accFile.close()
    try:
        if usernameList.index(user.username):  # check if the index of the username matches the index of the password
            return 0
    except ValueError:
        with open('accounts.txt', 'w') as file:
            fileContent.append("\n" + ' '.join([user.username, user.first, user.last, user.email, user.password, user.type, user.membership_end]))
            file.write(''.join(fileContent))
            return 1
