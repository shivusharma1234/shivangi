admin_keys ={"SK":"k"}
menu= {1:{'dishname':'Tandurichicken','dishid':1,'dishquantity':1,'prize':250,'discount':40,'stock':10},
            2:{'dishname':'veganburger','dishid':2,'dishquantity':1,'prize':150,'discount':20,'stock':10},
            3:{'dishname':'trufflecake','dishid':3,'dishquantity':1,'prize':190,'discount':20,'stock':12}}

#nested dict
def add_new_dish():
    dishname=input("enter the new dish:")
    dishid=int(input("enter the dish id:"))
    dishquantity=int(input("enter the dish quantity"))
    prize=int(input("enter the prize of the dish"))
    discount=int(input("offer discount"))
    stock=int(input("available stock"))
    food [dishid]={
        "dishname":dishname,
        "dishid":dishid,
        "dishquantity":dishquantity,
        "prize":prize,
        "discount":discount,
        "stock":stock
    }    
    print("the dish"+"dishname"+"is successfully added")
    return menu
def edit_from_dish():
    dishid=int(input("enter the dish which want to edit"))
    g=int(("enter thedish name"))
    s=int(input("enter the prize"))
    k=int(input("enter the dish quantity"))
    c=int(input("enter dish stock"))
    menu[dishid]["dishname"]=g
    menu[dishid]["prize"]=s
    menu[dishid]["quantuty"]=k
    menu[dishid]["stock"]=c
    print("***dish edited successfully***")
    return menu
def price_cal(dish):
    dish = int(input("Enter dishid:"))
    k= menu[dish]["price"]
    d= menu[dish]["discount"]
    n= k-(k*d/100)
    return n

def piece_dish(i):
        print("Dish Name: ",menu[i]["Dishname"])
        print("Price: ",menu[i]["Price"],"INR")
        print("Item ID: ",menu[i]["DishId"])
        print("Stock: ",menu[i]["Stock"])
        print("Discount: ",menu[i]["Discount"],"%")
        print("Quantity: ",menu[i]["Dishquantity"],"pieces")
        
def gm_dish(i):
        print("dish Name: ",menu[i]["Dishname"])
        print("Price: ",menu[i]["Price"],"INR")
        print("Item ID: ",menu[i]["DishId"])
        print("Stock: ",menu[i]["Stock"])
        print("Discount: ",menu[i]["Discount"],"%")
        print("Quantity: ",menu[i]["Dishquantity"],"gm")

def show_menu():
    C = [1,2]
    K = [3]
    print("*****HERE IS THE MENU OF TASTY BITES RESTAURANT*****")
    for i in C:
     piece_dish(i)
    for i in K:
      gm_dish(i)


def remove_dish():
    d = int(input("Enter the dish id which you want to exit"))
    menu.pop(d)
    print("Remove item successfully ")
    return menu














    
