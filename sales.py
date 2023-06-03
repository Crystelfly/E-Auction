import mysql_connection as conn
import library as lib
import bid
def display_sales()->None:
    sales=conn.select_data("select Sid, Uid, Pid, Offer_Price, Expiry_Date, Security_Fees from seller")
    print("-----------------------------------------------Sales List-----------------------------------------------------")
    print("SNo\tSeller Id\t\tUser Id\t\tProduct Id\tOffer Price\tExpiry Date\tSecurity Fee")
    print("--------------------------------------------------------------------------------------------------------------")
    i=1
    for sale in sales:
        print(i,end="\t\t")
        i=i+1
        for col in sale:
            print(col,end="\t\t")
        print("")
    print("--------------------------------------------------------------------------------------------------------------")

def add_sales(uid: str)->None:
    print("\n--------Add Sales--------")
    sid=lib.input_new_sid()
    if sid==0:
        print("Exiting from add sales")
        return 
    pid=lib.input_Product()
    if pid=="":
        print("Exiting from add sales")
        return 
    elif conn.is_user_product_exist(uid,pid)>0:
        print("User id ",uid," for the Product id ",pid," already exist.")
        return
    
    offer=lib.input_int("Enter the offer price Rs: ")
    if offer==0:
        print("Existing from sales")
        return 
    date=lib.input_date()
    if date=="":
        print("Exiting from add sales")
        return 
    
    fee=lib.security_fee(offer,"Enter the security fees: ")
    if fee==0:
        print("Exiting from add sales")
        return 
    conn.insert_data("insert into seller values ('"+str(sid)+"','"+uid+"','"+pid+"','"+str(offer)+"','"+date+"',"+str(fee)+")")

def update_sales()->None:
    print("\n--------Update Sales--------")
    print("Existing sell ids are: ",conn.get_sell_ids())
    sid=lib.input_Sid()
    if sid==0:
        print("Exiting from add sales")
        return 
    oldprice=conn.select_data("select Offer_Price from seller where Sid='"+str(sid)+"'")
    OldSecPrice=conn.select_data("select Security_Fees from seller where Sid='"+str(sid)+"'")
    print("Old Offer price is Rs: ",oldprice[0][0])
    print("Old Security fee is Rs: ",OldSecPrice[0][0])
    newRec=lib.input_int("Enter the new Offer Price: ")
    if newRec==0:
        print("Exiting from update sales")
        return
    NewSecPrice=lib.security_fee(newRec,"Enter the new security fees: ")
    if NewSecPrice==0:
        print("Exiting from update sales")
        return
    if newRec==0:
        print("Exiting from update sales")
        return
    elif NewSecPrice==0:
        print("Exiting from update sales")
        return
    elif conn.is_sell_exist(sid)==0:
        print("Record does not exist")
    else:
        conn.update_data("update seller set Offer_Price="+str(newRec)+", Security_Fees="+str(NewSecPrice)+" where Sid='"+str(sid)+"'")
        print("")
        display_sales()
        print("Updated sell id ",sid," successfully.")
              
def delete_sales()->None:
    print("\n--------Delete Sales--------")
    print("Existing sell ids are: ",conn.get_sell_ids())
    sid=lib.input_Sid()
    if sid==0:
        print("Exiting from delete sales")
        return 
    elif conn.is_sell_exist(sid)==0:
        print("Record does not exist")
    else:
        conn.delete_data("delete from seller where Sid='"+str(sid)+"'")
        print("")
        display_sales()
        print("Deleted sell id ",sid," successfully.")

def finalising_bids():
    bid.bid_finalising()

def payment_confirmation():
    bid.display_processed_bids()




