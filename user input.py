#The input() function works by pausing your program and waits for the user to enter some text.Once python receives the user's input,it assigns that input to a variable to make it convenient for you to work with.

message=input("Tell me something, and I will repeat it back to you: ")
print(message)

#Write clear prompts
prompt="If you share your name,we can personalize the mess ages you see."
prompt+="\nwhat is your first name?"
name=input(prompt)
print(name)

print(f"/nHello, {name}!")

#using int() to accept numerical input
age=input('How old are you?')
age=int(age)



height=input("How tall are you,in inches?")
height=int(height)

if height>=48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

#The Modulo operator
You can use it to determine whether a number is even or odd
number=input("Enter a numbere,  and I will tel you whether it's even or odd:")
number=int(number)

if number%2==0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")

