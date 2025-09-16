"""Check if user has data saved, if yes load message, if not save data to load message next time"""
import json


try:
    with open('C:/Users/kalho/OneDrive/Documents/Portfolio/User info/username_password.json') as f:
        username_password = json.load(f)
except FileNotFoundError:
    username_password = input("Enter your username and password seperated by a space to sign up:\n")
    username_password = username_password.split()
    with open('C:/Users/kalho/OneDrive/Documents/Portfolio/User info/username_password.json', 'a') as f:
        json.dump(username_password, f)
        print("Information saved, We will remember you next time!")
else:
    user_test = input("Enter username and password seperated by space to login:\n")
    user_test = user_test.split()
    if user_test[0] != username_password[0] and user_test[1] != username_password[1]:
        print("Wrong username and password")
    elif user_test[0] != username_password[0]:
        print("Wrong Username")
    elif user_test[1] != username_password[1]:
        print("Wrong Password")
    else:
        print(f"Welcome back {username_password}!")

    
    