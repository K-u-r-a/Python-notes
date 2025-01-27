cars=["bmw","subaru","ford","maserati","rolls royce","mazda"]

for car in cars:
         if car=="bmw":
           print(car.upper())
         else:
          print(car.title())


    #checking whether a value is not in a list
banned_users=['Andrew','Carolina','David']
user='marie'

if user not in banned_users:
       print(f"{user.title()}, you can post a response if you wish.")

       #Boolean Expressions.Used to keep track of certain conditions such as whether a game is running or whether a user can edit certain content on a website
       game_acive=True
       can_edit=False

       car='subaru'
       print(car=='subaru')

       print(car=='audi')


       #if statements

       #simple if statements
       age=19
       if age>=18:
          print("You are old enough to vote!")
          print("Have you registered to vote yet?")


          #if-else statements
          age=17
          if age>=18:
             print("You are old enough to vote.")
             print("Have you registered yet?")
          else:
             print("Sorry,you are too young to vote.")
             print("Please register to vote as soon as you turn 18!")


             #if-elif--else chain
             age=12
             if age<4:
                print("Your admission cost is $0.")

             elif age<18:
                print("Your admission cost is $25.")

             else:
                print("Your admission cost is $40.")

                age=12
                if age<4:
                   price=0
                elif age<18:
                   price=25
                else:
                   price=40
                   print(f"Your admission is ${price}.")


#alien shoot game
#a simple if-else statement
alien_color='green'
if alien_color=='green':
  print("You just earned 5 points!")

alien_color="blue"
if alien_color=="red":
     print("You just earned 5 points!")
else:
     print("You just earned 10 points!")

#an if-elif statement
alien_color="red"
if alien_color=="green":
   print("You just earned 5 points!")
elif alien_color=="yellow":
    print("You just earned 10 points!")
elif alien_color=="red":
    print("You just earned 15 points")

#an if-elif-else statement
age=22
if age<2:
    print("You are a baby")
elif age<4:
    print("You are a toddler")
elif age<13:
    print("You are a kid")
elif age<20:
    print("You are a teenager")
elif age<65:
    print("You are an adult")
else:
    print("You are an elder")

favorite_fruits=["mango","orange","pineapple","banana","apple"]
fruit="banana"
if fruit  in favorite_fruits:
    print("You really like bananas")


    #using if statements with lists











