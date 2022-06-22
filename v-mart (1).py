def vs():
    import qrcode
    import cv2
    import random as r
    link = "*********************************\n            V-Mart       \n*********************************\n*\n*\n*\n*\n*\n*\n* total biil is", total, " /- only\n*\n*\n********************************"
    img = qrcode.make(link)
    int_ran = r.randint(1, 1000)
    str_str = str(int_ran)
    path = "F:\\varad  python\code_"+str_str+".png"
    img.save(path)
    path = "F://varad  python//code_"+str_str+".png"
    ing = cv2.imread(path)
    cv2.imshow("your QR Code", ing)
    cv2.waitKey(0)


print("            *******************************************************************")
print("            *                                                                 *")
print("            *                        welcome to v-mart                        *")
print("            *                                                                 *")
print("            *******************************************************************")
print("\t\t\twhat you want?????\n choose the categorie")
print("1.Fruits\n2.Vegetables\n3.Dairy\n4.Snacks\n5.Dried Fruit")
input_categorie = input("enter the categorie => ")
# this is all fruits area
if(input_categorie == "Fruits" or "f" or "1"):
    input_fruits = input(
        "list of all fruits\n1.Apples\n2.bananas\n3.grapes\n4.oranges\n5.strawberries\n=>  ")
    if(input_fruits == "apple" or "1"):
        input_apple = int(input("enter the quantity of apple"))
        total = input_apple*210
        print("total of apple is", total)
        input_pay = input("choose payment 1.cash 2.QR Code")
        if(input_pay == "cash"):
            print("*********************************\n            V-Mart       \n*********************************")
            print("*\n*\n*\n*\n*\n*\n* total biil is ", total,
                  "/- only\n*\n*\n********************************")
        elif(input_pay == "qrcode" or "QR Code" or "QRcode"):
            print("qr code activeteds")
            vs()
    elif(input_fruits == "banana" or "2"):
        input_banana = int(input("enter the quantity of Banana"))
        total = input_banana*150
        print("total of Banana is", total)
        input_pay = input("choose payment 1.cash 2.QR Code")
        if(input_pay == "cash"):
            print("*********************************\n            V-Mart       \n*********************************")
            print("*\n*\n*\n*\n*\n*\n* total biil is ", total,
                  "/- only\n*\n*\n********************************")
        elif(input_pay == "qrcode" or "QR Code" or "QRcode"):
            print("qr code activeted")
            vs()
    elif(input_fruits == "grapes" or "3"):
        input_banana = int(input("enter the quantity of grapes"))
        total = input_banana*135
        print("total of grapes is", total)
        input_pay = input("choose payment 1.cash 2.QR Code")
        if(input_pay == "cash"):
            print("*********************************\n            V-Mart       \n*********************************")
            print("*\n*\n*\n*\n*\n*\n* total biil is ", total,
                  "/- only\n*\n*\n********************************")
        elif(input_pay == "qrcode" or "QR Code" or "QRcode"):
            print("qr code activeted")
            vs()
    elif(input_fruits == "oranges" or "4"):
        input_banana = int(input("enter the quantity of oranges"))
        total = input_banana*145
        print("total of oranges is", total)
        input_pay = input("choose payment 1.cash 2.QR Code")
        if(input_pay == "cash"):
            print("*********************************\n            V-Mart       \n*********************************")
            print("*\n*\n*\n*\n*\n*\n* total biil is ", total,
                  "/- only\n*\n*\n********************************")
        elif(input_pay == "qrcode" or "QR Code" or "QRcode"):
            print("qr code activeted")
            vs()
    elif(input_fruits == "strawberries" or "str" or "5"):
        input_banana = int(input("enter the quantity of strawberries"))
        total = input_banana*50
        print("total of strawberries is", total)
        input_pay = input("choose payment 1.cash 2.QR Code")
        if(input_pay == "cash" or "1"):
            print("*********************************\n            V-Mart       \n*********************************")
            print("*\n*\n*\n*\n*\n*\n* total biil is ", total,
                  "/- only\n*\n*\n********************************")
        elif(input_pay == "qrcode" or "QR Code" or "QRcode" or "2"):
            print("qr code activeted")
            vs()
# this is all Vegetables  area
if(input_categorie == "Vegetables" or "v" or "2"):
    input_Vegetables = input(
        "list of all Vegetables\n1.Potatoes\n2.onions\n3.carrots\n4.tomatoes\n5.cucumbers\n=>  ")
    if(input_Vegetables == "Potatoes" or "1" or "p"):
        input_Potatoe = int(input("enter the quantity of Potatoes "))
        total = input_Potatoe*15
        print("total of Potatoe is", total)
        input_pay = input("choose payment 1.cash 2.QR Code")
        if(input_pay == "cash"):
            print("*********************************\n            V-Mart       \n*********************************")
            print("*\n*\n*\n*\n*\n*\n* total biil is ", total,
                  "/- only\n*\n*\n********************************")
        elif(input_pay == "qrcode" or "QR Code" or "QRcode"):
            print("qr code activeteds")
            vs()
    elif(input_Vegetables == "onions" or "2" or "o"):
        input_onions = int(input("enter the quantity of onions "))
        total = input_onions*50
        print("total of onions is", total)
        input_pay = input("choose payment 1.cash 2.QR Code")
        if(input_pay == "cash" or "1"):
            print("*********************************\n            V-Mart       \n*********************************")
            print("*\n*\n*\n*\n*\n*\n* total biil is ", total,
                  "/- only\n*\n*\n********************************")
        elif(input_pay == "2" or "qrcode" or "QR Code" or "QRcode"):
            print("qr code activeteds")
            vs()
    elif(input_Vegetables == "carrots" or "3" or "c"):
        input_carrots = int(input("enter the quantity of carrots "))
        total = input_carrots*20
        print("total of carrots is", total)
        input_pay = input("choose payment 1.cash 2.QR Code")
        if(input_pay == "cash"):
            print("*********************************\n            V-Mart       \n*********************************")
            print("*\n*\n*\n*\n*\n*\n* total biil is ", total,
                  "/- only\n*\n*\n********************************")
        elif(input_pay == "qrcode" or "QR Code" or "QRcode"):
            print("qr code activeteds")
            vs()
    elif(input_Vegetables == "tomatoes" or "4" or "t"):
        input_tomatoes = int(input("enter the quantity of tomatoes "))
        total = input_tomatoes*15
        print("total of tomatoes is", total)
        input_pay = input("choose payment 1.cash 2.QR Code")
        if(input_pay == "cash"):
            print("*********************************\n            V-Mart       \n*********************************")
            print("*\n*\n*\n*\n*\n*\n* total biil is ", total,
                  "/- only\n*\n*\n********************************")
        elif(input_pay == "qrcode" or "QR Code" or "QRcode"):
            print("qr code activeteds")
            vs()
    elif(input_Vegetables == "cucumbers" or "5" or "c"):
        input_cucumbers = int(input("enter the quantity of cucumbers "))
        total = input_cucumbers*15
        print("total of cucumbers is", total)
        input_pay = input("choose payment 1.cash 2.QR Code")
        if(input_pay == "cash"):
            print("*********************************\n            V-Mart       \n*********************************")
            print("*\n*\n*\n*\n*\n*\n* total biil is ", total,
                  "/- only\n*\n*\n********************************")
        elif(input_pay == "qrcode" or "QR Code" or "QRcode"):
            print("qr code activeteds")
            vs()
if(input_categorie == "Dairy" or "d" or "3"):
    input_Dairy = input(
        "list of all Dairy \n1.Butter\n2.cheese\n3.eggs\n4.milk\n5.yogurt \n=>  ")
    if(input_Dairy == "Butter" or "2" or "o"):
        input_Dairy = int(input("enter the quantity of Butter "))
        total = input_Dairy*140
        print("total of Butter is", total)
        input_pay = input("choose payment 1.cash 2.QR Code")
        if(input_pay == "cash" or "1"):
            print("*********************************\n            V-Mart       \n*********************************")
            print("*\n*\n*\n*\n*\n*\n* total biil is ", total,
                  "/- only\n*\n*\n********************************")
        elif(input_pay == "2" or "qrcode" or "QR Code" or "QRcode"):
            print("qr code activeteds")
            vs()
    if(input_Dairy == "cheese" or "2" or "o"):
        input_Dairy = int(input("enter the quantity of cheese "))
        total = input_Dairy*140
        print("total of cheese is", total)
        input_pay = input("choose payment 1.cash 2.QR Code")
        if(input_pay == "cash" or "1"):
            print("*********************************\n            V-Mart       \n*********************************")
            print("*\n*\n*\n*\n*\n*\n* total biil is ", total,
                  "/- only\n*\n*\n********************************")
        elif(input_pay == "2" or "qrcode" or "QR Code" or "QRcode"):
            print("qr code activeteds")
            vs()
    if(input_Dairy == "eggs" or "2" or "o"):
        input_Dairy = int(input("enter the quantity of eggs "))
        total = input_Dairy*140
        print("total of eggs is", total)
        input_pay = input("choose payment 1.cash 2.QR Code")
        if(input_pay == "cash" or "1"):
            print("*********************************\n            V-Mart       \n*********************************")
            print("*\n*\n*\n*\n*\n*\n* total biil is ", total,
                  "/- only\n*\n*\n********************************")
        elif(input_pay == "2" or "qrcode" or "QR Code" or "QRcode"):
            print("qr code activeteds")
            vs()