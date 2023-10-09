
# =========================
#         Chapter 2
# =========================
#%%
print("Hello python word!")

#%%
message = "Hello python word!"
print(message)

#%% single / double quotes 
print("This is a string")
print('This is also a string')

#%%  
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

#%% 
first_name = "shuyuan"
last_name = "lu"
full_name = f"{first_name} { last_name}"
print(full_name)
print(f"Hello, {full_name.title()}!")

#%% Adding Whitespace to Strings with Tabs or Newlines
print("LU\nShuyuan")
print("LU\tShuyuan")

#%% Stripping Whitespace
name = " ShuyuanLU "
print(name.rstrip())
print(name.lstrip())
print(name.strip())

#%% Removing Prefixes
#watch_animation = "https://t.bilibili.com/?spm_id_from=333.999.0.0"
#watch_animation.removeprefix('https://')
#print(watch_animation)
### 3.9以上才能使用

#%%
3**2
universe_age = 14_000_000_000
print(1_00)
print(100)
print(10_0)
#%% Multiple Assignment
x,y,z = 0,0,0
CONSTANT = 1 

# =========================
#         Chapter 3
# =========================
#%% list
bicycles = ['treck','cannodale','redline','specialized'] 
print(bicycles[0].title())
print(bicycles[1].upper())
print(bicycles[-1])
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

#%%
motorcycles = ['honda', 'yamaha', 'suzuki']
#Appending Elements to the End of a List
motorcycles.append('ducati')
print(motorcycles)

#%% add new elements
name = []
name.append('Amy')
name.append("Dawn")
name.append('Amber')
print(name)

#%% Inserting Elements into a List
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0,'ducati')
print(motorcycles)

#%% Removing Elements from a List
motorcycles = ['honda', 'yamaha', 'suzuki','ducati']
#specific items
del motorcycles[0]
print(motorcycles)
#delete the last one and save it
last_owned = motorcycles.pop()
print(motorcycles)
print(f"The last motorcycle I owned was {last_owned.title()}.")
#delete the specific ones and save it
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was {first_owned.title()}.")

#%%
#motorcycles = ['honda', 'yamaha', 'suzuki','ducati']
#too_expensive = "daucati"
#motorcycles.remove(too_expensive)
#print(motorcycles)
#print(f"\nA {too_expensive} is too expensive for me.")

#%%
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse() #just reverse not sort
print(cars)

cars.sort()
print(cars)

cars.sort(reverse=True) #sort+reverse
print(cars)

print(len(cars))


# =========================
#         Chapter 4
# =========================
#%% looping
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you, everyone! That was a great magic show!")

#%% range is [ , )
for value in range(1,5):
    print(value)

#%% even number
even_numbers = list(range(2,11,2))
print(even_numbers)

#%%
squares = []
for value in range (1,11):
    square = value **2
    squares.append(square)
print(squares)

squares = []
squares = [value**2 for value in range (1,11)]
print(squares)
#%%
data = list(range(1,11))  #!!!!List!!!
print(data)
print(min(data))
print(max(data))
print(sum(data))

#%% slicing a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:5])
print(players[:4])
print(players[2:])

#%% copying
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append("cannoli")
friend_foods.append("ice cream")

print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

#%% Tuples
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# no ! dimensions[0] = 250
dimensions = (400, 80)
print(dimensions[0])
print(dimensions[1])
#we could not alter a tuples, but we can reassigning it 

# =========================
#         Chapter 5
# =========================
#%%
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

#%%
age = 17
age < 21
(age>10) and (age<21)
(age<10) or (age>60)
age !=17

#%% checking a value in list
requested_toppings = ['mushrooms', 'onions', 'pineapple']
"mushrooms" in requested_toppings
"ice cream" in requested_toppings
#%%
age = 17 #19
if age >= 18:
   print("You are old enough to vote!")
   print("Have you registered to vote yet?")
else:
   print("Sorry, you are too young to vote.")
   print("Please register to vote as soon as you turn 18!")
#%%
age = 12
if age < 4:
   print("Your admission cost is $0.")
elif age < 18:
   print("Your admission cost is $25.")
else:
   print("Your admission cost is $40.")

#%%
requested_toppings = []
if requested_toppings:
   for requested_topping in requested_toppings:
       print(f"Adding {requested_topping}.")
       print("\nFinished making your pizza!")
else:
   print("Are you sure you want a plain pizza?")


# =========================
#         Chapter 6
# =========================
#%%
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"You just earned {new_points} points!")
#%%
alien_0 = {'color':'green', 'points':5}

alien_0["x_position"]=0
alien_0["y_position"]=25

print(alien_0)
#%%
alien_0 = {"color" : "green"}
print(f"The alien is {alien_0['color']}.")
alien_0 = {"color" : "yellow"}
print(f"The alien is now {alien_0['color']}.")
#!!!!In dictionary only '' is available!!!
#%%
#%%
#%%
#%%

#%%
#%%
#%%
#%%
#%%
#%%

#%%
#%%
#%%
#%%
#%%
#%%

#%%
#%%
#%%
#%%
#%%
#%%

#%%
#%%
#%%
#%%
#%%
#%%

#%%
#%%
#%%
#%%
#%%
