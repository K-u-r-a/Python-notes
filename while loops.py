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


