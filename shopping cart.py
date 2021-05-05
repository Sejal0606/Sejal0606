products = {}
cart = []
def printOpt():
    print("1. Add Product")
    print("2. View Product")
    print("3. Add To Cart")
    print("4. View Cart")
    print("5. Checkout")
    print("6. Exit")
    print()
    ch = int(input("Enter  your choice: "))
    print()
    return ch

def Add_Product():
    pid = input("Enter the id of product: ") 
    cate = input("Enter the category of product: ")
    name = input("Enter the name of product: ")
    descp = input("Enter the description of product: ") 
    qyt = int(input("Enter the quantity of product: ")) 
    price = float(input("Enter the price of product:"))
    products[pid] = [name, price, qyt, descp, cate]
    print()
    print("Product Added....")
    print()
 
def View_Product():
        print(products)
        print()

def Add_To_Cart():
    l = []
    ad = input("Enter product id to add in cart: ")
    l.append(ad)
    qt_add = int(input("Enter the quantity to be added in cart: "))
    # if qt_add <= products
    l.append(qt_add)
    cart.append(l)
    print()
    print("Product is added in cart...")
    print()

def view_Cart():
    sr = 0
    for i in cart:
        for j in products:
            if i[0] == j:
                sr += 1
                val = products[j]
                print(sr,".",val[0], "----->", val[1],"------",i[1])
    print()


def Checkout():
    total = 0
    view_Cart()
    for i in cart:
        for j in products:
            if i[0] == j:
                val = products[j]
                total += (i[1] * val[1])
                products[j][2] = val[2]-i[1]   
    print("Total Bill Amount:",total)
            
    print()
            
def startApp():
    while True:
        choice = printOpt()
        if choice == 1:
            Add_Product()
        elif choice == 2:
            View_Product()
        elif choice == 3:
            Add_To_Cart()
        elif choice == 4:
            view_Cart()
        elif choice == 5:
            Checkout()
        elif choice == 6:
            print("Thank you...!")
            break
        else:
            print("Please enter correct choice....")

startApp()
