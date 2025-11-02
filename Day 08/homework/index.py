
#2 input -> არის ფუნქცია, რომელსაც შემოაქვს ინფორმაცია კომპიუტერში. მაგ: კლავიატურა, ჯოისტიკი, სნაკერი, ბარკოდის წამკითხველი, მაუსი და ა.შ.
# output - > არის ფუქცია, რომელსაც გამოაქვს უკვე შეტანილი ინფორმაცია. მაგ: მონიტორი, პრინტერი, დინამიკი, ყურსასმენი და ა.შ. 
#3 
fav_movie = input("print your favorite movie: ")
print(type(fav_movie))
print(fav_movie)
#4-5
#str - string
name = input("what is your name?")
surname = input("what is your surname?")
your_fav_color = input("what is your favorite color?")
your_fav_city = input("what is your favorite city?")
your_fav_car = input("what is your favorite car?")
print(type(name))
print(type(surname))
print(type(your_fav_color))
print(type(your_fav_city))
print(type(your_fav_car))
#int
English_lang = 100
georgian_lang_lit = 87
students_54school = 400
students_iliauni = 10000
students_tsu = 6000
print(type(English_lang))
print(type(georgian_lang_lit))
print(type(students_54school))
print(type(students_iliauni))
print(type(students_tsu))
#float
apple_kg = 2.800
weight = 60.780
maths_mark = 9.5
height =1.83
distance=96.80
print(type(apple_kg))
print(type(weight))
print(type(maths_mark))
print(type(height))
print(type(distance))
#6
word1 =input("write your name: ")
word2 =input("write your surname: ")
print(word1+" "+word2)
#7
your_age =int(input("write your age: "))
your_mom_age =int(input("write your mom's age: "))
your_dad_age = int(input("write your dad's age: "))
your_husband_age = int(input("write your husband's age: "))
your_brother_age =int( input("write your brother's age: "))
print((your_age+your_mom_age+your_dad_age+your_husband_age+your_brother_age)/5)

#8
name = input("print your name: ")
surname = input("print your surname: ")
age = (input("print your age: "))
height = (input("print your height: "))
weight = (input("print your weight: "))
print("My name is "+" "+name+" "+surname+"."+" "+"I'm"+" "+age+" "+"years old"+"."+" "+ "My height is"+" "+height+" "+ "and my weight is"+" "+weight+".")
