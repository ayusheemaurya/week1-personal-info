#Ayushee Maurya
#this program will take personal information from user validate it using defined parameters and then display it
#the program does not allow an empty field. if it encounters one it will terminate the program and user will restart again

#opening headline
print ('*' * 48)
print ('          PERSONAL INFORMATION MANAGER')
print ('*' * 48)

#asking user's name
#Program accepts name length from 3 to 50 and empty field in not accepted
name = input ("What is your name? ")
length_of_name = len(name)
while name == "" :
    print ("the field cannot be empty.")
    exit()
if length_of_name < 3 :
    print ("The should contain at least 3 characters.")
    exit()

elif length_of_name > 50 :
    print ("The name can have maximum 50 characters.")
    exit()
else :
    print (f"Hello {name}, please proceed further.")




#Asking other information and storing in variables
#empty field not accepted
Age = int(input("What is your age? "))
while Age == "":
    print("The field cannot by empty. please try again.")
    exit()
Age_in_months = Age * 12
City = input("where do you live? ")
while City == "" :
    print("The field cannot by empty. please try again.")
    exit()
Hobby = input("What is your hobby? ")
while Hobby == "" :
    print("The field cannot by empty. please try again.")
    exit()


#display of final information
print ('-' * 48)
print ('          PERSONAL INFORMATION MANAGER')
print ('-' * 48)

print(f"Your Name: {name}")
print(f"Your Age: {Age} ({Age_in_months} months)")
print(f"Your City: {City}")
print(f"Your Hobby: {Hobby}")

#thankyou message
print ('-' * 50)
print ('          Thankyou for using the program.')
print ('-' * 50)