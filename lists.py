vehicles=["toyota","subaru","mercedes benz","lexus","honda","range rover","ford"]
print(vehicles)

#accessing elements in a list
print(vehicles[0])

print(vehicles[2].title())

print(f"My first car will be a {vehicles[1].title()}")

#modifying elements in a list
vehicles[0]="bmw"
vehicles[0].upper()
print(vehicles)

#Adding new elements to a list.Append() is used to add new elements to the end of a list.
vehicles.append("mark x")
print(vehicles)

#most of the time lists are created in the following way to allow users to input their own values to the list
myvehicles=[]

myvehicles.append('subaru')
myvehicles.append('range rover')
myvehicles.append('mark x')
print(myvehicles)

#inserting elements to a list
myvehicles.insert(0,'ford')
print(myvehicles)

#deleting elements from a list.This can be useful when an alien is shot down from the sky and you want to eliminate it from the active number of aliens in the sky.It can also be useful when a user decides to remove their account from your web application,you would want to remove them from the active users.
del myvehicles[2]
print(myvehicles)

#removing an item using the pop() method.You might want to know the x and y position of an alien so you can direct an explosion to that point.You can also want to remove a user from the active users to the list of inactive users.Also when an element is popped it is just brought to the surfece maybe when you want to tell more about it.Otherwise it is still present in the list

popped_myvehicles=myvehicles.pop()
print(popped_myvehicles)
print(myvehicles)

#popping elements from any position in the list
owned_vehicles=["subaru","ford","range rover","mark x"]
first_owned= owned_vehicles.pop(0)
print(f"The first vehicle I owned was a {first_owned.title()}")

#removing an item by value,remove() method removes only one occurrence of the value in the list.If there are more occurrences in the list,you will need a loop to remove the rest.Here you state the value of the element you want to get rid of,you cannot state its position in the list.
owned_vehicles.remove('mark x')
print(owned_vehicles)

#Make a list of three people you would like to invite for dinner and send each of them a message inviting them for the dinner.
invited_guests=["Mary","John","William"]

message=f"Hello {invited_guests[0]}, I will be hosting this weekends dinner.You are welcome."
print(message)
message=f"Hello {invited_guests[1]}, I will be hosting this weeknds dinner.You are welcome."
print(message)
message=f"Hello {invited_guests[2]}, I will be hosting this weekends dinner.You are invited."
print(message)

#One of your guests will not make it to dinner.
absent=invited_guests.pop(0)
print(f"{absent}, will not be able to make it to dinner.")

attendees=["William","John","Jane"]

new_message=f"{attendees[0]},I will be hosting this weekends dinner.You are welcome."
print(new_message)
new_message=f"{attendees[1]},I will be hosting this weekends dinner.You are invited."
print(new_message)
new_message=f"{attendees[2]},I will be hosting this weekends dinner.You are invited."
print(new_message)

#You found a new bigger table,invite more guests.
attendees.insert(3,"Esther")
attendees.insert(4,"Jusper")
attendees.insert(5,"Wendy")
attendees.append("Jack")
print(attendees)


message=f"Hello {attendees[0]}, I will be hosting this weekends dinner.You are invited to have a good time with us.Thank you."
print(message)
message=f"Hello {attendees[1]}, I will be hosting this weekends dinner.You are invited to have a good time with us.Thank you."
print(message)
message=f"Hello {attendees[2]}, I will be hosting this weekends dinner.You are invited to have a good rime with us.Thank you."
print(message)
message=f"Hello {attendees[3]}, I will be hosting this weekends dinner.You are invited to have a good time with us.Thank you."
print(message)
message=f"Hello {attendees[4]}, I will be hosting this weekends dinner.You are invited to have a good time with us.Thank you."
print(message)
message=f"Hello {attendees[5]}, I will be hosting this weeknds dinner.You are invited to have a good time with us.Thank you."
print(message)


#The dinner table did not arrive on time an now you can only invite two people.
print(f"Hello {attendees}, I have some bad news.The dinner table did not arrive on due time and now I can only invite two guests.I am sorry for the inconvenience.")

popped_attendee=attendees.pop(5)
print(f"Hello {popped_attendee}, sorry to break it to you but I can't invite you to dinner because of limited space on the table.")

popped_attendee=attendees.pop(4)
print(f"Hello{popped_attendee}, sorry to break it to you but I can't have you for dinner due to limited space on the table.")

popped_attendee=attendees.pop(3)
print(f"Hello {popped_attendee}, sorry to break it to you but I can't have you for dinner due to limited space on the table.")

popped_attendee=attendees.pop(2)
print(f"Hello {popped_attendee}, sorry to break it to you but I can't have you for dinner due to limited space on the table.")

unpopped_attendee=attendees.pop(1)
print(f"Hello {unpopped_attendee}, you are welcome to have dinner at my place this weeknd.")

unpopped_attendee=attendees.pop(0)
print(f"Hello {unpopped_attendee},you are welcome to have dinner at my place this weeknd. ")


del attendees[0]
print(attendees)



#Organizing a list
#organizing a list permanently using the sort() method.
cities=["Nairobi","New York","Lagos","London","Algiers","Cape Town"]
cities.sort()
print(cities)

cities.sort(reverse=True)
print(cities)


#sorted() allows you to sort the elements in the list but still maintain the original order.Inshort sorted() does not sort it permanently unlike sort() which is permanent.sorted can also take reverse=true.
cities=["Nairobi","Cape Town","Lagos","New York","London","Algiers"]
print(cities)
print(sorted(cities))
print(cities)

#printing a list in reverse order
cities=["Nairiobi","London","Lagos","Cape Town","New York"]
cities.reverse()
print(cities)

#Finding the length of a list.This is useful in determining the number of users in a website or the number of active aliens that you still have to shoot down.
length=len(cities)
print(length)

#When you want to access the last item on the list.
cities=["Lagos","London","New York","Nairobi"]
my_city=cities[-1]
print(my_city)

