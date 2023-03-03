print("Welcome,Please enter items price and house tier")
print("Note:: It's only for guild house")

while True:

    #take item prices form user
    
    woodt1 = input("Enter T1 wood/log price: ")
    stonet1 = input("Enter T1 stone price: ")
    blockt2 = input("Enter T2 block price: ")
    blockt3 = input("Enter T3 block price: ")
    blockt4 = input("Enter T4 block price: ")
    blockt5 = input("Enter T5 block price: ")
    blockt6 = input("Enter T6 block price: ")
    blockt7 = input("Enter T7 block price: ")
    blockt8 = input("Enter T8 block price: ")
    bed =input("Enter bed price: ")
    table = input("Enter table price: ")
    labourPrice = input("Enter labour price: ")
    houseTier = input("Enter the Tier of the house you want to built: ")
    
    # changing them into integer and if can't,retype
    try:
        houseTier = int(houseTier)
        woodt1 = int(woodt1)
        stonet1 = int(stonet1)
        blockt2 = int(blockt2)
        blockt3 = int(blockt3)
        blockt4 = int(blockt4)
        blockt5 = int(blockt5)
        blockt6 = int(blockt6)
        blockt7 = int(blockt7)
        blockt8 = int(blockt8)
        bed = int(bed)
        table = int(table)
        labourPrice = int(labourPrice)
        break
    except:
        print("!!!!Please type only number!!!!")
        continue


totalCost = 0    
log = 150
stone = 15
block = 900
n = 1
t= 2
count = 0


#calculating the price of labours and funitures  
labourPrice = 15 * labourPrice
totalCost += labourPrice

bedprice = bed * 15
tableprice = table * 3
funitureprice = bedprice + tableprice
totalCost += funitureprice


while houseTier !=  1:

    count += 1
    houseTier = houseTier - 1
    log = log*n
    stone = stone*n
    n *= 2
    totalCost += stone*stonet1
    totalCost += log*woodt1


    if t == 2:
        blockCost = block * blockt2
    elif t == 3:
        blockCost = block * blockt3
    elif t == 4:
        blockCost = block * blockt4
    elif t == 5:
        blockCost = block * blockt5
    elif t == 6:
        blockCost = block * blockt6
    elif t == 7:
        blockCost = block * blockt7
    elif t ==8:
        blockCost = block * blockt8
    t += 1
    totalCost +=  blockCost
    print(totalCost)

print ("Total cost for your guild house is", totalCost)
print ("labour",labourPrice,"bedprice",bedprice, "tableprice", tableprice)

    
again = input("Do you want to check other tier guild house?(yes/no) ::")
if again.lower == "yes":
    houseTier = input("Enter the Tier of the house you want to built: ")
elif again.lower == "no":
    print("Thanks for using my programm")

    


