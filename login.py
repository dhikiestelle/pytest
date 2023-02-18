import os
import time
import getpass
from Login import Login
from SignUp import SignUp
from Encryption import Encrypt
def login():
    while True:
        os.system("cls")
        print ("[ LOGIN ]")
        username = input ("ENTER USERNAME ›> ")
        password = getpass.getpass ("ENTER PASSWORD")
        user = Login(username, password)
        if user.valid_user():
          print ("Login Successful!")
          time.sleep(1)
          break
        else:
          print ("Login Unsuccessful, try again..")
          time.sleep(1)
          continue 


def sign_up():
    while True:
      os.system("cls")
      print ("[ SIGN UP ]")
      username = input("ENTER USERNAME>>")
      if SignUp.valid_username (username):
        break
      else:
        print ("Username Taken, try again.")
        time.sleep(1)
        continue
    password = getpass.getpass ("ENTER PASSWORD »>")
    user = SignUp (username, password)
    user. save()
    os. system("cls")
    print ("Account Added")
    time.sleep(1)