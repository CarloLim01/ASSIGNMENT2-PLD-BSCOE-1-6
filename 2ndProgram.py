apple_Question = int(input("How many apples do you want to buy? "))
orange_Question = int(input("How many oranges do you want to buy? "))

apple_Price = 20
orange_Price = 25

apple_Total = apple_Question * apple_Price
orange_Total = orange_Question * orange_Question
total = apple_Total + orange_Total
print(f"The total amount is {total}.")