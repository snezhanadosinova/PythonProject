def changePassword(rowOfUser):
    accFile = open('accounts.txt', 'r')
    fileContent = accFile.readlines()
    rowList = fileContent[rowOfUser].split()
    # checks if the password is same as the old one, if its right then the new password is added in the text file instead the old one
    while 1:
        oldPassword = input("Enter your last password: ")
        if oldPassword == rowList[4]:
            newPassword = input("Enter your new password: ")
            rowList[4] = newPassword
            newRow = " ".join(rowList)
            fileContent[rowOfUser] = newRow
            for i in range(0, len(fileContent)):
                fileContent[i] = fileContent[i].rstrip()
            content = "\n".join(fileContent)
            with open('accounts.txt', 'w') as file:
                file.write(content)
                print("Password Changed successfully")
                return 1
        else:
            print("Wrong password entered")
