#A while loop runs for as many times as the condition is true.
#The following while loop counts from 1 to 5
current_number=1
while current_number<=5:
    print(current_number)
    current_number+=1

#Letting the user choose when to quit.
#This while loop runs as long as the value of message is not 'quit'.The program stops running when the user enters the value 'quit'.
prompt="\nTell me something and I will repeat it back to you:"
prompt+="\nEnter 'quit' to end the program."

#when the program runs it compares the value of message to 'quit'.
message=" "
while message!='quit':

#Below,python displays the prompt to the user and waits for them to enter their input.Whatever they enter is assigned to message and printed.
    message=input(prompt)
    print(message)

#The problem with the code above is that it displays the word 'quit' as if it was an actual message.A simple if test fixes this.

prompt="\nTell me something, and I will repeat it back to you: "
prompt+="\nEnter 'quit' to end the program."

message=" "
while message!='quit':
    message=input(prompt)

    if message!='quit':
        print(message)

#Using a flag
prompt="\nTell me something, and I will repeat it back to you: "
prompt+="\nEnter 'quit' to end the program."

active=True
while active:
    message=input(prompt)

    if message=='quit':
        active=False
    else:
        print(message)

#Using break to exit a loop
prompt="\nPlease enter the name of a city you have visited: "
prompt+="\n(Enter 'quit' when you are finished)"
while True:
    city=input(prompt)
    if city=='quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")

#Using continue in a loop.
current_number=0
while current_number<10:
    current_number+=1
    if current_number%2==0:
        continue
    print(current_number)

#Using while loops with lists and dictionaries
#Using while loops with lists and dictionaries allows you to collect,store and organize lots of input to examine and report on later.
#moving items from one list to another

#start with users that need to be verified,and an empty list to hold confirmed users.
unconfirmed_users=['alice','brian','candace']
confirmed_users=[]

#verify each user until there are no more unconfirmed users.
#move each verified user into the list of confirmed users.
while confirmed_users:
    current_user= unconfirmed_users.pop()
    print(f"Verifying user:{current_user.title()}")
    confirmed_users.append(current_user)

    #Display all confirmed users.
    print("\nThe following users have been confirmed: ")
    for confirmed_user in confirmed_users:
        print(confirmed_user.title())

#Removing All instances of specific values from a list.
pets=['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
    print(pets)

#Filling a dictionary with user input.
responses={}
#set a flag to indicate that polling is active.
polling_active=True
while polling_active:
    #prompt for the person's name and response.
    name=input("\nWhat is your name?")
    response=input("which mountain would you like to climb someday?")
#store the response in the dictionary.
responses[name]=response

#Find out if anyone else is going to take the poll.
repeat=input("Would you like to let another person respond? (yes/no)")
if repeat=='no':
    polling_active=False

#Polling is complete.Show the results.
print("n---Poll Results---")

for name,response in responses.items():
    print(f"{name} would like to climb {response}.")



