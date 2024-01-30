import os

# ill be damned if im commenting over this mess 
with open("secrettoken.txt", "r+") as file:
    if file.read()  == None:
        inputToken = input("Enter your private key: ")
        file.write(inputToken)
    if file.read() != None:
        question = input("Welcome to the Setup. 1 to Change Token, 2 to Change Channel id, 3 to Change Username, 4 to Exit: ")
        if question == "1":
            file.seek(0)
            file.truncate()
            inputToken = input("Enter your private key: ")
            file.write(inputToken)
            print("Setup complete. Exiting program.")
with open("discordChannel.txt", "r+") as file:
    if file.read()  == None:
        channelInput = input("Enter your channel id: ")
        file.write(channelInput)
    if question == "2":
        with open ("discordChannel.txt", "r+") as file:
            file.seek(0)
            file.truncate()
            channelInput = input("Enter your channel id: ")
            file.write(channelInput)
            print("Setup complete. Exiting program.")
with open("username.txt", "r+") as Usernamefile:
    if Usernamefile.read()  == None:
        usernameInput = input("Enter your username: ")
        file.write(usernameInput)
    if question == "3":
        with open ("username.txt", "r+") as file:
            file.seek(0)
            file.truncate()
            usernameInput = input("Enter your username: ")
            file.write(usernameInput)
            print("Setup complete. Exiting program.")
if question == "4":
    print("Exiting program.")
    exit()