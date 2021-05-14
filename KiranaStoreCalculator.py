# Kirana Store Calculator

item = []
price = []
sum = 0 
counter = 0
while(True):
    flag = input("Do u want to continue Y/ N: ")
   
    if flag == 'Y' or flag == 'y':
        counter = counter + 1
        user_item = input("Enter item name :  ")
        user_price = input("Item price : ")
        item.append(user_item)
        price.append(int(user_price))
        sum = sum + int(user_price)

    elif flag == 'n' or flag == 'N':
        break

print("Item_name  Price")
for i in range(counter) :
    
    print(f"{item[i]}  {price[i]}")
print(f"Your total bill is {sum} ")


    

    
    

