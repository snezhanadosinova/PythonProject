from datetime import datetime as dt


# checks if the user is allowed to login from the expiration date of user
def isAllowedToLogin(endDate):
    now = dt.now()
    end = dt.strptime(endDate, "%Y-%m-%d")
    if end >= now:
        return 1
    else:
        return 0


# login function
def loginScreen():
    print("Login\n")

    accFile = open('accounts.txt', 'r')
    fileContent = accFile.readlines()
    usernameList = []
    firstNameList = []
    passwordList = []
    userTypeList = []
    userMembershipEnd = []
    for line in fileContent:
        usernameList.append(line.split()[0])  # gets all usernames and creates a list
        firstNameList.append(line.split()[1])  # gets all first names and creates a list
        passwordList.append(line.split()[4])  # gets all passwords and creates a list
        userTypeList.append(line.split()[5])  # gets all user types and creates a list
        userMembershipEnd.append(line.split()[6])  # gets all user membership end dates
    accFile.close()

    username = input("Enter your username: ")
    pwd = input("Enter your password: ")
    # check if the index of the username matches the index of the password
    try:
        if usernameList.index(username) > -1 and passwordList[usernameList.index(username)] == pwd:
            rowOfUser = usernameList.index(username)
            end_date = userMembershipEnd[rowOfUser]
            # checks if the user type is admin or the date of expiration to the other users
            if userTypeList[usernameList.index(username)] == 'admin' or isAllowedToLogin(end_date):
                firstName = firstNameList[rowOfUser]
                userType = userTypeList[rowOfUser]
                return [rowOfUser, firstName, userType]
            else:
                print("Membership has expired")
                return loginScreen()
        else:
            print("The password is incorrect, please try again!")
            return loginScreen()
    except ValueError:
        print("Wrong username, please try again!")
    return loginScreen()
