# 2) Boolean-> არის მეოთხე მონაცემთა ტიპი, რომელიც ვისწავლეთ. ხშირად, პროგრამირების დროს გვჭირდება, გავიგოთ ესა თუ ის გამოსახულება ჭეშმარიტია თუ მცდარი. სწორედ, ესეთი პასუხები არის boolean ტიპის მონაცემები. boolean --> true or false
# 3) binary code --> არის კოდი, რომელიც დაწერილია მხოლოდ ორი ციფრის გამოყენებით, 0 და 1-ის. 0-ებით და 1-ებით ჩაწერილია რიცხვები, სიმბოლოები და ანბანის ასოები, რომლის წაკითხვაც შეუძლია კომპიუტერს. ჩვეულებრივ 1 არის true, ხოლო 0 არის false.  
# 4) bool() --> არის ფუნქცია, რომელსაც მნიშვნელობა გადაჰყავს boolean ტიპის მონაცემში. მაგ: ნებიმიერი სტრინგი არის true გარდა ცარიელისა, ნებისმიერი ჩწერილი რიცხვი არის true, გარდა 0-ისა. მაშასადამე, ნებისმიერი მნიშვნელობა bool()-ში ჩაწერილი გამოიტანს true-ს, გარდა ცარიელი მნიშვნელობისა და ნულისა. 
# 5) 
# a = "მარიამი"
# b = "ლუკა"
# print(a == b) პასუხი არის false
a = 5
b = 10
print(a == b) # პასუხი არის false, იმ შემთხვევაში, თუ a ტოლი იქნება b-სი და იქნება ერთი და იგივე მნიშვნელობა მაშინ იქნება true.
# 6) 
c = int(input("write something:"))
d = float(input("write something too:"))
print(c > d) 
# თუ c-ს მნიშვნელობა მეტი იქნება d-ზე არის true, თუ  d-ს მნიშვნელობა მეტი იქნება c-ზე იქნება false. 
# 7) 
user_word = input("Write what are you studying?" )
prog_lang = "Python"
print(user_word == prog_lang)
# თუ მომხმარებელი ჩაწერს java, javascript ან სხვას მას გამოუგდებს false-ს, თუ ჩაწერს python-ს მაშინ true. 
user_w = input("write what you are learning?")
print(user_w == "Python")

# 8) 
user_num = int(input("write number:"))
our_num = 100
print(user_num > our_num)

user_numb = float(input("write number:"))
our_numb = 100
print(user_numb > our_numb)

user_number = int(input("write number:"))
print(user_number > 100)

# თუ მეტი იქნება 100-ზე მაშინ true, თუ ნაკლები მაშნ false.

# 9) 
user_pwd = input("write your password:")
web_pwd = "Python123"
print(user_pwd == web_pwd)

user_password = input("write your password:")
print(user_password == "Python123")


# 10) 
num1 = int(input("num1: "))
num2 = float(input("num2: "))
print(num1 > num2) # თუ მეტია true, თუ არა false
print(num1 < num2) # თუ ნაკლებია true, თუ არა false
print(num1 == num2) # თუ ტოლია true, თუ არა false

# ან მესამე პუნქტი გაგვეერთიანებინა პირველ ორთან
print(num1 >= num2) # თუ ან მეტია ან ტოლია მაშინ true, თუ არა false
print(num1 <= num2) # თუ ან ნაკლებია ან ტოლია მაშინ true, თუ არა false

# 11) 
word1 = input("word1: ")
word2 = input("word2: ")
word3 = input("word3: ")
word4 = input("word4: ")
word5 = input("word5: ")
print("User write these words:"+" "+word1+","+" "+word2+","+" "+word3+","+" "+word4+" "+"and"+" "+word5+".")

# 12) 
number1 = int(input("num1:"))
number2 = int(input("num2:"))
number3 = int(input("num3:"))
number4 = int(input("num4:"))
print((number1+number2+number3+number4)/4)

# 13)
one = 26
two = 73.546
three = "Coffee"
four = True
print(type(one))
print(type(two))
print(type(three))
print(type(four))

# 14)
str1 = "ელისო"
str2 = "გია"
print(str1 == str2)
# პასუხი არის false, რადგან ერთმანეთს არ ემთხვევა მაგრამ ორივეში "ელისო" ან ორივეშ "გია" რომ დაგვეწერა იქნებოდა true.

# 15) 
n1 = int("10")
n2 = int("150")
n3 = int("500")
n4 = int("10000")
print(n1+n2+n3+n4)

# 16)
nu1 = str(123)
nu2 = str(234)
nu3 = str(345)
print(nu1+nu2+nu3)