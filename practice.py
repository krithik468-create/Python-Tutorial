"""name = "krithik roshan"
full_name = f"My name is {name}!"

print(full_name)"""

# mylist = ["apple", "banana", "cherry","cherry","cherry","apple"]
# ano_list = ["BMW","Benz","hyndai",'ford']
# mylist.extend(ano_list) #mutable
# print(ano_list)
# print(mylist)
# copy_list = mylist.copy()
# print(mylist)
# print("copy_list",copy_list)
# copy_list.append("ansab")
# print("copy_list after append",copy_list)
# print(mylist)
# emt_value = ""
# print(mylist.count("cherry"))  #slice method
# print(len(mylist))
# mylist.append("krithik")
# print(mylist.pop(2))
# mylist.reverse()
# print(mylist)
# name = "ansab"
# mylist.sort()
# print(mylist.count("apple"))
# mylist.insert(20,"graps")
# print(mylist)
# mylist.clear()
# print(mylist)


# Dict
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year":"",
#   "year": 1964,
  
#   "date":122
# }
# print(thisdict)

# print("Enter 1 to move next, enter 2 to move back")
# num = int(input("Next 1 or Back 2 : "))
# if num > 2 : 
#   print("Invalid input")
# else:
#   match num:
#     case 1:
#       print("Move forward ->")
#     case 2:
#       print("Move backward <-")
    
# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#   for y in fruits:
#     print(x, y)


#-------------------------Functions-------------------------------------------------


# num1 = int(input("Enter 1st number : "))
# num2 = int(input("Enter 2nd number : "))

# def add(a, b) :
#  return a + b

# def sub(a,b):
#   return a - b

# def mul(a, b):
#   return a * b

# def rem(a, b):
#   return a % b

# def quo(a, b):
#   return a / b

# print("Addition :",add(num1,num2))
# print("Subraction :",sub(num1,num2))
# print("Multiplication :",mul(num1,num2))
# print("Reminder :",rem(num1,num2))
# print("Quoitent :",add(num1,num2))

# print(f"Entered two numbers are {num1} & {num2}")

# def uppercase(str):
#   return str.upper()

# def lowercase(str):
#   return str.lower()

# variable = "KRITHIK"

# # need to send this data in API response in caps letter
# print(lowercase(variable))


# def my_function():
#   return ["cherry", "banana", "apple"]
# x = my_function()
# x.sort()
# print(x)



def my_function(*,name,address):
  print("Hello", name,address)

my_function(name = "Emil",address="ferferfr")
