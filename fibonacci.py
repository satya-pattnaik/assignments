
any_number = input("Give me a number") #By default will give a string #10

#Typecast it to string
any_number = int(any_number)

another_number = float(input("Give another number")) #100


name = input("Give me your name") #satya
if type(name) != str:
    print("This is not a string, give me a string")

if any_number%2 ==0:
    print("number is even")
print(any_number)

print(name)
