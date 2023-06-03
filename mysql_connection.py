import mysql.connector as pymysql
file=open("connection.txt",'r')
strhost=(file.readline()).strip()
struser=(file.readline()).strip()
strpassword=(file.readline()).strip()
strdb=(file.readline()).strip()
#strhost="localhost"
#struser="root"
#strpassword="anusha@123"
#strdb="e_auction"
file.close()

def insert_data(sql,msg=0):
    try:
        conn=pymysql.connect(host=strhost,user=struser,password=strpassword,db=strdb)
        c=conn.cursor()
        c.execute(sql)
        conn.commit()
        if msg==0:
            print("Record inserted successfully.")
        return 1
    except Exception as error:
        print("Error: ",error)
        print("Error while inserting record.sql used: ",sql)
        return 0
        
def select_data(sql):
    try:
        conn=pymysql.connect(host=strhost,user=struser,password=strpassword,db=strdb)
        c=conn.cursor()
        c.execute(sql)
        row=c.fetchall() 
        return row
    except Exception as error:
        print("select_data Error: ",error)
        print("Error while selecting record. sql used: ",sql)

def update_data(sql,dp=1):
    try:
        conn=pymysql.connect(host=strhost,user=struser,password=strpassword,db=strdb)
        c=conn.cursor()
        c.execute(sql)
        conn.commit()
        if dp==1:
            print("Record updated successfully")
    except Exception as error:
        print("Error: ",error)
        print("Error while updating record.sql used: ",sql)

def delete_data(sql,dp=1):
    try:
        conn=pymysql.connect(host=strhost,user=struser,password=strpassword,db=strdb)
        c=conn.cursor()
        c.execute(sql)
        conn.commit()
        if dp==1:
            print("Record deleted successfully")
    except Exception as error:
        print("Error: ",error)
        print("Error while deleting record.sql used: ",sql)

def is_buyer(uid):
    user_type=select_data("select user_type from user where Uid='"+uid+"'")
    if user_type==None:
        return False
    elif user_type[0]=="B" or user_type[0]=="b":
        return True
    else:
        return False

def check_user_exist(uid):
    existance=select_data("select count(*) from user where uid='"+uid+"'")
    if existance[0][0]==1:
        print("User already exist. Try another user name")
        return 1
    return 0

def is_user_exist(uid):
    existance=select_data("select count(*) from user where uid='"+uid+"'")
    return existance[0][0]

def get_user_name(uid):
    name=select_data("select name from user where uid='"+uid+"'")
    return name[0]

def drop_db():
    conn=pymysql.connect(host=strhost,user=struser,password=strpassword,db=strdb)
    c=conn.cursor()
    try:
        c.execute("drop database e_auction")
        print("Database deleted successfully")
    except Exception as error:
        print("Error: ",error)
        print("Error while deleting database")
    try:
        c.execute("create database e_auction")
        print("Database created successfully")
    except Exception as error:
        print("Error: ",error)
        print("Error while creating database")
    

def table_creation(sql):
    try:
        conn=pymysql.connect(host=strhost,user=struser,password=strpassword,db=strdb)
        c=conn.cursor()
        c.execute(sql)
        conn.commit()
        print("Table has been created successfully")
    except Exception as error:
        print("Error: ",error)
        print("Error while creating table. sql used: ",sql)

def is_bid_exist(bid:int)->int:
    existance=select_data("select count(*) from bidding where Bid="+str(bid))
    return int(existance[0][0])

def is_sell_exist(sid:int)->int:
    existance=select_data("select count(*) from seller where Sid="+str(sid))
    return int(existance[0][0])

def insert_payment(sql:str)->int:
    
    try:
        conn=pymysql.connect(host=strhost,user=struser,password=strpassword,db=strdb)
        c=conn.cursor()
        c.execute(sql)
        conn.commit()
        print("Payment done successfully.")
        print("Thank You. Your item will be deliverd at your doorstep within 10 days.")
        print("")
        return 1
    except Exception as error:
        print("Error: ",error)
        print("Error while inserting record.sql used: ",sql)
        return 0

def get_sell_ids()->str:
    sid=str(select_data("select Sid from seller "))
    sid=sid.replace("(","")
    sid=sid.replace(",)","")
    return sid

def get_user_ids()->str:
    uid=str(select_data("select Uid from User "))
    uid=uid.replace("(","")
    uid=uid.replace(",)","")
    return uid

def get_bid_ids()->str:
    bid=str(select_data("select Bid from bidding "))
    bid=bid.replace("(","")
    bid=bid.replace(",)","")
    return bid

def get_product_ids()->str:
    pid=str(select_data("select Pid from product "))
    pid=pid.replace("(","")
    pid=pid.replace(",)","")
    return pid

def is_pid_exist(pid:str)->int:
    existance=select_data("select count(*) from product where Pid='"+pid+"'")
    return existance[0][0]

def get_product_name(bid:int)->list:                                             
    name=select_data("select Name from product \
                where Pid in (select Pid from seller \
                                where Sid in (select Sid from Bidding \
                                                where bid="+str(bid)+"));")
    return name

def is_user_product_exist(uid:str,pid:str)->int:
    existance=select_data("select count(*) from seller where Uid='"+uid+"' and Pid='"+pid+"'")
    return existance[0][0]
    
def fetch_security_fees(sid:int)->int:
    fees=select_data("select Security_Fees from seller where Sid="+str(sid))
    return fees[0][0]

def fetch_sale_price(sid:int)->int:
    op=select_data("select offer_price from seller where Sid="+str(sid))
    return op[0][0]

def fetch_secuity_money_bid(bid:int)->int:
    fees=select_data("select Security_Fees from bidding where Bid="+str(bid))
    return fees[0][0]

def is_record_exist(sql:str)->bool:
    data:list=select_data(sql)
    count:int=data[0][0]
    if count>0:
        return True
    else:
        return False

    



