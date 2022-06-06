import admin as Ss

class user:
    Username = " "
    password = " "
    login_info = {"Username":Username, "password": password}

    def __init__(self,name,phoneno,email,address,password):
        self.name=name
        self.phoneno=phoneno
        self.email=email
        self.address=address
        self.password=password
        user.login_info["username"]=name
        user.login_info["password"]=password
        self.profile={"name":name}
        self.order_history={}
    @classmethod
    def login(slv,name,password):
        if slv.login_info["username"]== name and slv.login_info["password"]==password:
            print("loggedin successfully")
            return True
        else:
            print("invalid credentials")
            return False
    def place_order(self):
           print("what you want to order in the menu")
           print(Ss.show_menu())
           user_choice= int(input("if you want to order click 1. Yes 2. No"))
           if user_choice==l:
              o=int(input("what you want to order from the list"))
              x=0
              for i in range (o):
                  dishid=int(input("enter item id"))
                  quant=int(input("enter the quantity"))
                  quantity=int(input("enter the quantity"))
                  prize=sk.prize_cal(dishid)
                  print(prize)
           
                  if quant>quantity:
                      o = o + (price*quan/quantity)
                      print (o) 
                  else:
                       print("min value has already order")
                  if o>1000:
                      o = o - ((o*10/100))
                  confirm_order = int(input("confirm the order select 1. Yes 2. No"))
                  if confirm_order=="yes":
                          print(f'''your dish name is {Ss.menu[dishid]["dishname"]}''')
                          print(f'''your dish name is {Ss.menu[dishid]["prize"]}''')
                          print(f"the quantity{quant}")
                          print(f"the cost{o}INR in total")
                          print("you can now order")
                          self.order_history[dishname]= {
                              "dishname":Sk.menu[dishid]["diahname"],
                              "prize":Sk.menu[dishid]["prize"],
                              "quantity":quant
                          }
                          final_quantity = Ss.menu[menuid]["stock"] - quan
                          kd.menu[menuid]["quantity"]=final_quantity
                          print("your order is successfully placed")
             
                  elif confirm_order == "NO": 
                          print("this order is canecelled")
                  else:
                          print("invalid choice")
           elif user_choice == 2:
               print("you select 2 optin so we can cencelled this")
           else:
              print("enter the invalid choice")
 
    def display(self):
            print("name:",self.name)
            print("number:",self.number)
            print("email:",self.email)
            print("address:",self.address)
            print("password:",self.password)
            print("login_info:",User.login_info)


    def account_register():
      cs = user(input("name: "),int(input("enter phoneno: ")),input("email_id: "),input("enter_ adress: "),input("enter password: "))
      return cs.display()

    def account_update():
      cs = user(input("name: "),int(input("enter phoneno: ")),input("email_id: "),input("enter_ adress: "),input("enter password: "))
      return cs.display()



              
                  













             
             

            


                            
