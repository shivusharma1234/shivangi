
import admin as Sk
import user as us
from user import user

ka= user(str,str,str,str,str)

kara= int(input("Where you want to login select 1. Admin and 2.User and 3.Exit"))
if kara == 1:
    Username=int(input("Admin Username:"))
    Password=int(input("Admin Password:"))
    if sk.admin_keys[Username] == Password:
        print("***Logged in Successfully***")
        admin_crawler = True
        while admin_crawler:
            adm_choice = int(input("choose the admin panel 1. ADD NEW DISH 2.EDIT DISH 3. VIEW DISH 4.REMOVE DISH 5.EXIT"))
            if adm_choice==1:
                Sk.add_new_dish()
            elif adm_choice ==2:
                Sk.edit_from_dish()
            elif adm_choice==3:
                Sk.show_menu()
            elif adm_choice==4:
                Sk.remove_dish()
            elif adm_choice==5:
                print(f"You are exit to admin panel{Username}")
                admin_crawler= False
            else:
                print("Entered option is wrong please selecr properly")
    else:
         print("Entered credentials are wrong!, SORRY!!")
elif kara == 2:
    print("welcome to the user dashboard,Register yourself")
    user.account_register()
    username = input("Enter the username:")
    password = input("Enter the Password:")
    if User.login(Username, password):
        print("Logged in successfully")
    user_crawler= True
    while user_crawler:
        prsn_choice = int(input("{username},Enter the option 1.Place order 2. Order history 3. Exit"))
        if prsn_choice ==1:
            ka.place_order()
        elif prsn_choice ==2:
            print("here is your order history, Repeat order {username}")
            print("kkh.order_history")
        elif prsn_choice==3:
            user_crawler  = False
            print("Logged out")
        else:
            print("you have choosen the invalid option")
    else:
        print("wrong credentials")
else:
    exit()
