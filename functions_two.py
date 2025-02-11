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

 