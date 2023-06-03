import re   #re=regular expression
import mysql_connection as conn
import getpass
import sys 
def card_validation(s)->bool:
    lst:list = s.split("-")
    if len(lst)==4:
        for ch in lst:
            if len(ch)!=4:
                return False
    else:
        return False
    
    p = re.search("[456][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]",s)
    if p==None:
        return False
    else:
        return True
#5412-8750-2248-9156       

def Input_card_num()->str:
    print("Valid card number format xxxx-xxxx-xxxx-xxxx.")
    print("The first character must be either 4,5 or 6. Ex. 4xxx-xxxx-xxxx-xxxx.")
    msg="Enter the card number to pay: "
    while(1):
        num=input(msg)
        if num=='':
            return ""
        elif card_validation(num)==True:
            return num
        else:
            msg="Invalid card number. Enter again: "

def date_validation(date_string)->bool:
    import datetime
    #date_string = '2017-12-31'
    date_format = '%Y-%m-%d'
    try:
       dateObject = datetime.datetime.strptime(date_string, date_format)
       return True
    except ValueError:
       print("Incorrect data format, should be YYYY-MM-DD")

    return False


def input_date(msg=None)->str:
    if msg==None:
        msg="Enter the date(YYYY-MM-DD): "
        
    while(1):
        date=input(msg)
        if date=='':
            return ""
        elif(date_validation(date))==True:
            return date
            break

def input_text(msg: str, maxlength: int)->str:
    while True:
        name=input(msg)
        if name=="":
            return ""
        elif (len(name))>maxlength:
            print("Input data length is ",len(name),". It's length cannot more than ",maxlength)
        else:
            return name

def number_validation(numb)->bool:
    p=re.search("^\\+?[1-9][0-9]{9,11}$",numb)
    if p==None:
        return False
    else:
        return True
#91345647583

def number_input()->str:
    msg="Enter the phone number: "
    while True:
        numb=input(msg)
        if numb=="":
            return ""
        elif (number_validation(numb))==True:
            return numb
        else:
            msg="Invalid phone number. Enter again: "

def check_int(num)->bool:
    for char in num:
            if ord(char)>32 and ord(char)<48 or ord(char)>57 and ord(char)<65 or ord(char)>90 and ord(char)<97 or ord(char)>122 and ord(char)<127:
                return False
    if len(num)>9:
        return False
    else:
        p=re.search("^[0-9 \-]+$", num)
    if p==None:
        return False
    else:
        return True


def input_int(msg)->int:
    while True:
        num=input(msg)

        if num=="":
            return 0
        elif check_int(num)==True:
            if int(num)<0:
                msg="Input cannot be negative. Enter again: "
            else:
                return int(num)
        else:
            msg="Invalid input. Expected integer value. Enter again: "

def input_Sid()->int:
    while True:
        sid=input_int("Enter the sell id: ")
        if sid==0:
            return 0
        if conn.is_sell_exist(sid)>0:
            return sid
        else:
            print("Invalid Sell id. Existing Sell Ids are: ",conn.get_sell_ids())

def input_Bid()->int:
    while True:
        bid=input_int("Enter the Bid id: ")
        if bid==0:
            return 0
        if conn.is_bid_exist(bid)>0:
            return bid
        else:
            print("Invalid Bid id")

def input_user()->str:
    while True:
        uid=input_text("Enter the user id: ",20)
        if uid=="":
            return ""
        elif conn.is_user_exist(uid)>0:
            return uid
        else:
            print("Invalid Uid id. Existig User Ids are: ",conn.get_user_ids())
            
def input_Product()->str:
    while True:
        pid=input_text("Enter the Pid id: ",20)
        if pid=="":
            return ""
        elif conn.is_pid_exist(pid)>0:
            return pid
        else:
            print("Invalid Pid id. Existing Product ids are: ",conn.get_product_ids())
  
def input_new_sid()->int:
    while True:
        sid=input_int("Enter the sell id: ")
        if sid==0:
            return 0
        if conn.is_sell_exist(sid)>0:
            print("Given sell id already exist. Existing Sell Ids are: ",conn.get_sell_ids())
        else:
            return sid
def input_new_pid()->str:
    while True:
        pid=input_text("Enter the product id: ",20)
        if pid=="":
            return ""
        if conn.is_pid_exist(pid)>0:
            print("Given product id already exist. Existing Product Ids are: ",conn.get_product_ids())
        else:
            return pid

def is_buyer_seller()->str:
    while True:
        Utype=input_text("Enter whether you are a buyer or a seller (B/S): ",1)
        if Utype=="":
            return ""
        elif Utype=="B" or Utype=="b" or Utype=="S" or Utype=="s":
            return Utype
        else:
            print("invalid Input. Enter again.")

def input_new_user()->str:
    while True:
        uid=input_text("Enter your User Id: ",20)
        if uid=="":
            return ""
        if uid=="NUL":
            print("Invalid user id.")
        elif conn.check_user_exist(uid)==0:
            return uid

def format_cardno(cardno)->str:
    formated_cardno=""
    i=0
    for ch in cardno:
        formated_cardno += ch
        i=i+1
        if i % 4 == 0 and i<16:
            formated_cardno = formated_cardno + "-"
    return formated_cardno

def yes_no_menu()->int:
    print("1.Yes\n2.No")
    while True:
        ch=int(input_int("Enter your choice: "))
        if ch==1:
            return 1
        elif ch==2:
            return 2

def pay_cancel_menu()->int:
    print("\n1)Pay\n2)Cancel")
    while True:
        ch=int(input_int("Enter your choice: "))
        if ch==1:
            return 1
        elif ch==2:
            return 2

def security_fee(offer:int, msg:str)->int:
    while True:
        fee=input_int(msg)
        if fee==0:
            return 0
        elif fee>=offer:
            print("Security fees cannot be greater than or equal to the offer price [",offer,"]. Enter again: ")
        else:
            return fee
        
def help_box():
    print("\n---------------------------------------------------Help-----------------------------------------------------------------")
    print(" 1. During Add, Edit, Delete or Update Sales, User, Item and Bid, press key 'Enter' to exit.")
    print(" 2. If the program runs through DOS(cmd.exe) input password characters will be hidden else the password character will be shown.")
    print(" 3. This program alows to register and login user. ")
    print(" 4. User type can be as S/B where S is a seller and B is a buyer.")
    print(" 5. After login user can add edit and delete Item.")
    print(" 6. After creating item details one can sell the item by adding the records in sales.")
    print(" 7. This program also allows to add, edit and delete sale records. ")
    print(" 8. During add sale, seller can also mention security money.")
    print(" 9. Aftr adding sales the buyer can purchase an item after placing their bids.")
    print(" 10. During add bid he can enter the price at which he want to purchase it.")
    print(" 11. During add bid the buyer will have to pay if particular sale require security money. ")
    print(" 12. After adding bid, the seller can finalise the added bids for his sales.")
    print(" 13. Once the bid is finalise, the buyer can make the payment for his bids. ")
    print(" 14. Once the payment is done the item will be delivered at his address.")
    print(" 15. This program will accept the money only through debit/credit card.")
    print(" 16. Valid card number must beging with either 4,5 or 6.")
    print(" 17. Valid card format is xxxx-xxxx-xxxx-xxxx where x is the numeric value.")
    print(" 18. Valid date format is YYYY-MM-DD.")
    print(" 19. Special characters are not allowed.")
    print("\n---------------------------------------------------End------------------------------------------------------------------\n")

def get_password()->str:
    try:
        p = getpass.getpass("Password :")
        return p
    except Exception as error :
        print("get_password error :", error)
        return password

def get_new_password()->str:
    while True:
        try:
            p = getpass.getpass("Password :")
            if p=="":
                return ""
            p2 = getpass.getpass("Re Enter Password :")
            if p2=="":
                return ""
            if p==p2:
                return p
            else:
                print("Password and Re Enter password does not match. Enter again.")
                
        except Exception as error :
            password=input_text("Enter your password: ",25)
            return password




   





    
    

            
        
    




  







    

