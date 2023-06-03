import mysql_connection as conn
import library as lib
def register():
    try:
        print("\n--------Register New User--------")
        uid=lib.input_new_user()
        if uid=="":
            return 
        name=lib.input_text("Enter your name: ",25)
        if name=="":
            return ""
        password=lib.get_new_password()
        if password=="":
            return
        type1=lib.is_buyer_seller()
        if type1=="":
            return
        phone=lib.number_input()
        if phone=="":
            return 
        add=lib.input_text("Enter your address: ",30)
        if add=="":
            return 
        
        sql="insert into user (Uid, Name, User_type, phone, address, Password) values \
                    ('"+uid+"','"+name+"','"+type1+"','"+phone+"','"+add+"','"+password+"')"
            
        if conn.insert_data(sql)==1:
            print("Registeration successful\n")
        else:
            print("Register unsuccessful\n")
    except Exception as error:
        print("Error: ",error)
        print("Register unsuccessful\n")   
        
def login()->str :
    try:
        print("\n--------Login User--------")
        uid=lib.input_user()
        if uid=="":
            return ""
        password1=lib.get_password()
        
        if password1=="":
            return ""

        return_count=conn.select_data("select count(*) from user where Uid='"+uid+"' and Password='"+password1+"'")
               
        count = return_count[0][0]
    except Exception as error :
        print("login Error: ",error)
        count=0

    if count==1:
        print("Login successful\n")
        return uid
        
    else:
        print("Invalid User id or password\n")
        return ""




