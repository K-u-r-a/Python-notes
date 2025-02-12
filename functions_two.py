#Return value
#Returning a simple value
def formatted_name(first_name, last_name):
    """Return a full name,nearly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = formatted_name('jimi','hendrix')
print(musician)

#making an argument optional

def get_formatted_name(first_name, last_name, middle_name = " " ):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('john', 'lee' 'hooker')
print(musician)

musician = get_formatted_name('john', 'hooker')
print(musician)

#another option
def get_formatted_name(first_name, last_name, middle_name = " "):
    """Return a full name, neatly formatted."""
    if middle_name:
     full_name = f"{first_name} {middle_name} {last_name}"
    else:
       full_name = f"{first_name} {last_name}"
    return full_name.title()

musician =  get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

#Returning a dictionary
def build_person(first_name, last_name, age=None):
   """Return a dictionary of information about a person."""
   person = {'first': first_name}, {'last': last_name}
   if age:
            person['age'] = age
   return person

musician = build_person('jimi', 'hendrix')
print(musician)

#Using a function with a while loop
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
#This is an infinite loop!
while True:
    print("\nPlease tell me your name:")
    f_name = input("First name:")
    l_name = input("Last name:")

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
How to terminate the while loop otherwise it will run forever.
def get_formatted__name(first_name,last_name):
    """Return a full name, neatly formatted."""
    full_name=f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name=input("First name: ")
    if f_name=='q':
        break

    l_name=input("Last name: ")
    if l_name == 'q':
        break

    formatted_name=get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")


#Passing a list.
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

#Modifying a list in a function.
#start with some designs that need to be printed.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahe', 'dron']#designs that need to be printed.
completed_models = []#an empty list.

#simulate printing each design, until none are left.
#Move each design to completed models after printing.

while unprinted_designs:#as long as designs remain in unprinted_designs
    current_design = unprinted_designs.pop()#The last design in the list is moved to current_design.
    print(f"Printing model: {current_design}")#indicates that a certain design is currently being printed.
    completed_models.append(current_design)#The printed design is then added to the list of completed models.

    #Display all completed models.
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

#Adding functions to our code.
def print_models(unprinted_designs, completed_models):#parameters
    """Simulate printing each design, until none are left.Move each design to completed_models after printing."""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        prin(completed_model)
unprinted_designs = ['phone case', 'robot pendant', 'dodecahe dron']
completed-models = []
print_models(unprinted_designs, completed_models)#arguments
show_completed_models(completed_models)

#Preventing a function from modifying a list.
#You can send a copy of a list to a function like this:
function_name(list_name[:])

printed_models(unprinted_designs[:], completed_models)

#Passing an arbitrary number of arguments.
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)

    make_pizza('pepperoni')
    make_pizza('mushrooms','green peppers', 'extra cheese')

#Now lets add a loop.
def make_pizza(*toppings):
    """Summarize the pizza we are to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

#Mixing positional and arbitrary arguments.
def make_pizza(size,*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#Using arbitrary keyword arguments
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about  a user."""

    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', location = 'princeton', field = 'physics')





 
