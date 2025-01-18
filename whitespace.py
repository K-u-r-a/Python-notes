# \n is used to add a new line and \t is used to add whitespace.
print("Languages:\npython\nC\tJavaScript")

myname="Kura chepkemoi"
print(f'" " + {myname} +" "') #I need to do more research about this.Does python recognise "+" as python code?Can " " be used to create space?

first_name="Kura"
last_name="chepkemoi"
full_name= f"{first_name} \n{last_name}"
print(full_name)

#stripping .In the real world it is used to clean up user input before it is stored in a program.
favorite_language=" python "
favorite_language.rstrip()
print(favorite_language)

favorite_language.lstrip()
print(favorite_language)

favorite_language.strip()
print(favorite_language)