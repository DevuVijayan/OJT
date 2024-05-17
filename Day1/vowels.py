# def fun(string):
#     vowels = 'aeiouAEIOU'
#     count = 0
#     for char in string:
#         if char in vowels:
#             count += 1
#     return count

# string = input("Enter a string: ")
# print("Number of vowels:", fun(string))

 




def fun(str):
    vowels="aeiouAEIOU"
    count=0
    for char in str:
        if char in vowels:
            count+=1
    return count
str=input("enter a string")
print("str: ",fun(str))