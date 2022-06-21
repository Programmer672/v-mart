def vs():
    import qrcode
    import cv2
    import random as r
    link="*********************************\n            V-Mart       \n*********************************\n*\n*\n*\n*\n*\n*\n* total biil is",total," /- only\n*\n*\n********************************"
    img=qrcode.make(link)
    int_ran=r.randint(1,1000)
    str_str=str(int_ran)
    path="F:\\varad  python\code_"+str_str+".png"
    img.save(path)
    path="F://varad  python//code_"+str_str+".png"
    ing=cv2.imread(path)
    cv2.imshow("your QR Code",ing)
    cv2.waitKey(0)

print("*******************************************************************")
print("*                                                                 *")
print("*                        welcome to v-mart                        *")
print("*                                                                 *")
print("*******************************************************************")
print("\t\t\twhat you want?????\n choose the categorie")
print("1.Fruits\n2.Vegetables\n3.Dairy\n4.Snacks\n5.Dried Fruit")
input_categorie=input("enter the categorie => ")
if(input_categorie=="Fruits"or"f"):
    input_fruits=input("list of all fruits\n1.Apples\n2.bananas\n3.grapes\n4.oranges\n5.strawberries\n=>  ")
    if(input_fruits!="b"):
            input_apple=int(input("enter the quantity of apple"))
            total=input_apple*210
            print("total of apple is",total)
            input_pay=input("choose payment 1.cash 2.QR Code")
            if(input_pay=="cash"):
                print("*********************************\n            V-Mart       \n*********************************")
                print("*\n*\n*\n*\n*\n*\n* total biil is ",total,"/- only\n*\n*\n********************************")
            elif(input_pay=="qrcode"or"QR Code"or"QRcode"):
                print("qr code activeteds")
                vs()
    elif(input_fruits!="apple"):
            input_banana=int(input("enter the quantity of Banana"))
            total=input_banana*150
            print("total of Banana is",total)
            input_pay=input("choose payment 1.cash 2.QR Code")
            if(input_pay=="cash"):
                print("*********************************\n            V-Mart       \n*********************************")
                print("*\n*\n*\n*\n*\n*\n* total biil is ",total,"/- only\n*\n*\n********************************")
            elif(input_pay=="qrcode"or"QR Code"or"QRcode"):
                    print("qr code activeted")
                    vs()       





















































