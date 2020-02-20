import datetime
import requests
import random

#a list of words
WORD_SITE = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
response = requests.get(WORD_SITE)
possiblePasswords = response.content.splitlines()

def generator():
  global username
  date = datetime.datetime.now() #getting current time
  year = (date.year) #getting the year
  first_name = input("please type your first name : ")

  last_name = input("please type your last name : ")

  age = (int(input("please type your age : ")) - 13) 
  year = str(year - age)
  username = (str(year[-1]) + first_name[0:1] + last_name[0:6]) #generates the username

  print("Thank you, your username is " + username)

  return username


#generator()

def passgenerator():
  global password
  # pick a random password
  word = possiblePasswords[random.randint(0, len(possiblePasswords))] #gets the word
  print(word)
  number = random.randint(10,100) #gets the number
  password = (str(number) + str(word))
  print(password)
passgenerator()
