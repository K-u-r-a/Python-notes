#Dictionaries allow you to connect related pieces of information
#A simple dictionary showing information about a number of aliens.
alien_0={'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])


print(f"You just earned {alien_0['points']} points!")


alien_0['x_position']=0
alien_0['y_position']=25

print(alien_0)


#starting with an empty dicstionary
students={}
students['Sheila']='Nigeria'
students['Gloria']='Zimbabwe'
students['Esther']='Angola'
print(students)

#Modifying values in a dictionary
students['Sheila']='New York'
print(students)

#Lets track the position of an alien that can move at differen speeds.We'll store a value representing the alien's current speed and then use it to determine how far to the right the alien should move.
alien_1={'x_position':0,'y_position':25,'speed':'medium'}
print(f"original position:{alien_1['x_position']}")

#Move the alien to the right
#Determine how far to move the alien based on its current speed.
if alien_1['speed']=='slow':
    x_increment=1
elif alien_1['speed']=='medium':
    x_increment=2
else:
    #This must be a first alien.
    x_increment=3

alien_1['x_position']=alien_1['x_position']+x_increment

print(f"New position:{alien_1['x_position']}")

#removing key value pairs
alien_2={'x_position':0,'y_position':30}
del alien_2['y_position']
print(alien_2)

#a dictionary of similar objects.You can use a dictionary to store one kind of information about many people.
favorite_languages={
"Miriam":"Python",
  "Jane":"C",
"Mary":"JavaScript",
"Nark":"Rust"
}

language=favorite_languages['Jane'].title()
print(f"Jane's favorite language is {language}")

#using get() to access values
#I am using get() here where a value required has not been assigned to the dictionary of alien_3.I have set a default value since 'points' is not in the dictionary.
alien_3={'color':'green','speed':'slow'}
point_value=alien_3.get('points','No point value assigned')
print(point_value)

Mary={'first_name':'Mary','last_name':'Maina','city':'Nairobi'}
print(f"Mary's lastname is {Mary['last_name']}")
print(f"'Mary's lives in {Mary["city"]}" )


#looping through a dictionary
#looping through all key-value pairs
user_0={
    'username':'woman of steel',
    'firstname':'Kura',
    'lastname':'Chepkemoi'
}

for key,value in user_0.items():
    print(f"key:{value}")
for key,value in user_0.items():
    print(f"Kura's {key.title()} is {value.title()}")


#looping through all keys in a dictionary
favorite_languages={
    "Miriam":"Python",
  "Jane":"C",
"Mary":"JavaScript",
"Nark":"Rust"
}

for name in favorite_languages.keys():
    print(name.title())

friends=['sarah','Jane']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

if name in friends:
    language=favorite_languages[name].title()
    print(f"\t{name.title()}, I see you love{language}!")


#looping through a dictionary's keys in a particular order
favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'JavaScript'
}
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()},thank you for taking the poll.")

    #looping through all values in a dictionary.
    favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'JavaScript'
}
    
    print("The following languages have been mentioned.")
    for language in favorite_languages.values():
        print(language.title())

        #Nesting
        #a list of dictionaries
        alien_01={'color':'green','points':'5'}
        alien_02={'color':'yellow','points':10}
        alien__03={'color':'red','points':15}
        
        #a list of the three aliens
        aliens=[alien_01,alien_02,alien__03]
        #I loop thriough the list and print out each alien.
        for alien in aliens:
            print(alien)


#In this example we use range() to ceate a fleet of 30 aliens
#Make an empty list for storing aliens.
aliens=[]

#Make 30 green aliens.
for alien_number in range(30):
    new_alien={'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

    #show the first 5 aliens.
    for alien in aliens[:5]:
        print(alien)

#show how many aliens have been created.
print(f"Total number of aliens:{len(aliens)}")


#When it's time to change colors we can use a for loop and an if statement to change the color of the aliens.

#Make an empty list for storing aliens.
aliens=[]

#make 30 green aliens
for alien_bumber in range(30):
    new_alien={'color':'green','points':'5','speed':'slow'}
    aliens.append(new_alien)
    for alien in aliens[:3]:
        if alien['color']=='green':
            alien['color']=='yellow'
            alien['speed']=='medium'
            alien['points']=10

            #show the first 5 aliens.
            for alien in aliens[:5]:
                print(alien)

#adding an elif block that turns yellow aliens into red,fast_moving ones worth 15 points each.
for alien in aliens[0:3]:
    if alien['color']=='green':
        alien['color']='yellow'
        alien['speed']='medium'
        alien['points']=10

    elif alien['color']=='yellow':
        alien['color']='red'
        alien['speed']='fast'
        alien['points']=15

#A list in a Dictionary
#store information about a pizza being ordered.
pizza={
    'crust':'thick',
    'toppings':['mushrooms','extrs cheese'],
}

#summarize the 
print(f"You ordered a {pizza['crust']}-crust pizza" "with the following toppings:")
for topping in pizza['toppings']:
 print(f"\t{topping}")
