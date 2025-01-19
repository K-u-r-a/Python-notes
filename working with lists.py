#When you want to perform an action on every item on the list.You can use for loop

magicians=["Alice","Grace","Eldad","Elijah","Victor","Gideon"]
for magician in magicians:
    print(f"{magician},that was a great trick!")
    print("I can't wait to see your next trick\n")


#Making Numerical lists
#Using the range() function
for value in range(1,5):
 print(value)

#Using range() to make a list of numbers
numbers=list(range(1,6))
print(numbers)


even_numbers=list(range(2,11,2))
print(even_numbers)


squares=[]
for value in range(1,11):
 square =value**2
squares.append(square)
print(squares)

squares =[]
for value in range(1,11):
 squares.append(value**2)
print(squares)


digits=[1,2,3,4,5,6,7,8,9,0]
print(min(digits))

print(max(digits))

print(sum(digits))

#list comprehension
squares=[value**2 for value in range(1,11)]
print(squares)


#slicing a list
players=["Ronaldo","Messi","Olunga","Pogba","Merino","Wanyama","Daniella"]
print(players[0:3])

print(players[:4])

print(players[:3])

print(players[-3])

#looping through a slice.
players=["Ronaldo","Messi","Olunga","Pogba","Merino","Wanyama","Daniella"]
for player in players[:3]:
  print(player)

#copying a list
my_books=["Alchemist","Pilgrimage","Atomic Habits"]
my_friends_books=my_books[:]
print(my_friends_books)
    