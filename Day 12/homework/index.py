# # 1) შედარებითი ოპერატორები : > ; < ; == ; >= ; <= .
# # >
print(5.61 > 7.21)
print(54 > 23)
print(45.27 > 27)
a = int(input("please, write a number : "))
b = int(input("please, write a second number : "))
print(a>b)
c = int(input("please, write a number : "))
print(c > 28.95)

# # <
print(96.32 < 127.45)
print(1278 < 1235)
print(45 < 12.12)
a = int(input("please, write a number : "))
b = int(input("please, write a second number : "))
print(a<b)
c = int(input("please, write a number : "))
print(c < 57)

# # >=
print(12 >= 34)
print(45.67 >= 20)
print(56.27 >= 89.72)
a = int(input("please, write a number : "))
b = int(input("please, write a second number : "))
print(a>=b)
c = int(input("please, write a number : "))
print(c >= 107.01)

# # <=
print(89 <= 98)
print(74.56 <= 85)
print(96 <= 177)
a = int(input("please, write a number : "))
b = int(input("please, write a second number : "))
print(a<=b)
c = int(input("please, write a number : "))
print(c <= 369)

# # ==
print("mariami" == "Mariami")
print(124 == 12.7)
print(189 == 758)
print(236.51 == 78.54)
a = float(input("write a number: "))
b = float(input("write a second number: "))
print(a == b)

# # logical operators -> არის სიტყვები, რომლებიც გამოიყენება ორი ან მეტი წინადადების ერთმანეთთან დასაკავშირებლად, მათ ჩვენ ქართულ ენაში კავშირებს ვუწოდებთ, ესენია: "და" და "ან". 
# #"and" -> აუცილებელია ორივე პასუხი იყოს სიმართლე, რათა true  გამოვიდეს პასუხად. ძალიან მგრძნობიარეა false-ის მიმართ, წინადადებების გაერთიანებაში რამდენი true-ც არ უნდა იყოს ერთი false ყველაფერს აფუჭებს.
# # false and false - > false
# # false and true - > false
# # true and false - > false
# # true and true - > true
# #"or" -> არ არის აუცილებელი ორივე პასუხი იყოს სიმართლე, საკმარისია ერთი მაინც იყოს სიმართლე რათა true  გამოვიდეს პასუხად. 
# # false or false - > false
# # false or true - > true
# # true or false - > true
# # true or true - > true

# # 3) logical operators:
#and:
a = 5
b = 7
c = a > b
d = b > a
print(c and d)

a = "Mariami"
b = "Luka"
c = a == b
print(a and c)

print(True and True)

#or
a = 6
b = 10
c = a > b
d = b > a
print(c or d)

a = "Luka"
b = "Mariami"
e = "Mariami"
c = a == b
d = b == e
print(d or c)

print(False or False)

# 4) 
user_num = int(input("Please, write the number: " ))
our_num = 27
print(user_num > our_num)
user_num = int(input("Please, write the number: "))
print(user_num > 27)

# 5) 
user_name = input("Write my name(please write with CapsLK off): ")
my_name = "mariami"
print(user_name == my_name)

user_name = input("Write my name(please write with CapsLK off): ")
print(user_name == "mariami")

# 6) 
user_age = int(input("Print your age: "))
access_age = 18
print(user_age>access_age)
user_age = int(input("Print your age: "))
print(user_age>18)