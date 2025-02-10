

def greet_user(): #defining a function
    """Display a simple greeting.""" #docstring
    print("Hello!")

    greet_user() #calling the function


#Passing information to a function.

def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

    greet_user("Kura")

 # 'kura' is an argument
 # 'username' is a parameter  
 
 
def display_message():
    """Display what is being learnt in this chapter."""
    print(f"Hello everyone,you will be learning Functions in this chapter.")

    display_message()


def favorite_book(title):
    """Display favorite book title."""
    print(f"One of my favorite books is {title.title()}")
    favorite_book("Alice in Wonderland")

#Passing arguments using:
#Positional arguments,keyword arguments

#Positional arguments
def describe_pet(animal_type,pet_name):
    """Display information about a pet."""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

    describe_pet('hamster','harry')

#multiple function calls.

def describe_pet(animal_type,pet_name):
    """Display information about a pet."""
    print(f"I have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")

    describe_pet('hamster','harry')
    describe_pet('dog','willie')

#Keyword Arguments.Here you directly associate the name and the value within the argument.
def describe_pet(animal_type,pet_name):
    """Display information about a pet."""
    print(f"I have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")

    describe_pet(animal_type='hamster',pet_name='harry')

#Default values.When you use default values, any parameter with a default value needs to be listed after all the parameters that don't have default values.This allows python to continue interpreting positional arguments correctly.
def describe_pet(pet_name,animal_type='dog'):
    """Display information about a pet."""
    print(f"I have a {{animal_type}}")
    print(f"My {animal_type}'s name is {pet_name.title()}")

    describe_pet(pet_name='willie')


def make_shirt(size,message):
    """Display the different sizes of shirts and the message to be written on them."""
    print(f"My shirt's size is {size.upper()} and the message to be written on it is:{message.title()}")

    make_shirt('xl','new day ,yes it is.')
    make_shirt(size='xxl',message='i love me.')






 

