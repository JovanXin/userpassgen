import datetime
import requests
import random

#a list of words
wordsite = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
response = requests.get(wordsite)
wordlist = response.content.splitlines()

# Generates a username
def generate_username():
  date = datetime.datetime.now() #getting current time
  year = (date.year) #getting the year
  fname = input("please type your first name : ")

  lname = input("please type your last name : ")

  age = (int(input("please type your age : ")) - 13) 
  syear = str(year - age) #schoolyear
  username = (str(syear[-1]) + fname[0:1] + lname[0:6]) #generates the username
  return username


def generate_password(wordlist):
  # pick a random password
  password = random.choice(wordlist)
  return f"{password}{random.randint(10,100)}"

def main():
  wordlist = response.content.splitlines()
  username = generate_username()
  password = generate_password(wordlist)
  print("Your password is" + password + "and your username is " + username)
  
if __name__ == "__main__":
  main()
