import mysql_connection as conn
import library as lib
def display_bid()->None:
    print("----------------------------------------------------------Bidding List------------------------------------------------------")
    print("Bid id\t\tSeller id\tUser id\t\tProduct id\tExpiry Date\tOffer Price\tBidding Price\tBid Finalise")
    print("----------------------------------------------------------------------------------------------------------------------------")
    bids=conn.select_data("select Bid, seller.Sid, bidding.Uid, Pid, Expiry_Date, Offer_Price, Bidding_Price, Bid_Finalise\
         from seller, bidding \
         where seller.sid=bidding.sid")
    for bid in bids:
        for col in bid:
            print(col,end="\t\t")
        print("")
    print("----------------------------------------------------------------------------------------------------------------------------")

def add_bid(uid: str)->None:
    print("\n--------Add Bids--------")
    sid:int=lib.input_Sid()
    if sid==0:
        print("Exiting from Bids")
        return 
    fees=conn.fetch_security_fees(sid)
    if fees>0:
        print("This Sales require security fees Rs: ",fees)
        print("Do you want to continue? ")
        yn=lib.yes_no_menu()
        if yn==2:
            print("Exiting from Add Bid")
            return 
    sp = conn.fetch_sale_price(sid)
    print("Sale price : ",sp)
    price=lib.input_int("Enter the bid price Rs: ")
    if price==0:
        print("Exiting from Add Bid")
        return 
    if fees>0:
        print("Security money is: ",fees)
        cardnum=lib.Input_card_num()
        if cardnum=="":
            print("Exiting from Add Bid")
            return 
    conn.insert_data("insert into bidding(Sid, Uid, Bidding_Price, Bid_Finalise, Security_Fees) \
    values('"+str(sid)+"','"+uid+"','"+str(price)+"',0,"+str(fees)+")")

def update_bid()->None:
    print("\n--------Update Bids--------")
    print("Existing Bid Ids are: ",conn.get_bid_ids())
    bid=lib.input_Bid()
    if bid==0:
        return
    old_Price=conn.select_data("select Bidding_Price from bidding where Bid="+str(bid))
    print("Old Bidding price is Rs: ",old_Price[0][0])
    newrec=lib.input_int("Enter the new Bid Price: ")
    if newrec==0:
        print("Exiting from Update Bid")
        return
    elif conn.is_bid_exist(bid)==0:
        print("Record does not exist")
    else:
        conn.update_data("update bidding set Bidding_Price='"+str(newrec)+"' where Bid='"+str(bid)+"'")
        print("")
        display_bid()
        print("Updated bidding id ",bid," successfully.")
              
def delete_bid()->None:
    print("\n--------Delete Bids--------")
    print("Existing Bid Ids are: ",conn.get_bid_ids())
    bid=lib.input_Bid()
    if bid==0:
        print("Exiting from Delete Bid")
        return
    if conn.is_bid_exist(bid)==0:
        print("Record does not exist.")
    else:
        conn.delete_data("delete from bidding where Bid='"+str(bid)+"'")
        print("")
        display_bid()
        print("Deleted bidding id ",bid," successfully.")

def bid_finalising()->None:
    print("\n--------Finalise Bids--------")               #join queries
    sql="select seller.Sid, bidding.Uid, Pid, Bid, Expiry_Date, Offer_Price, Bidding_Price, Bid_Finalise\
         from seller, bidding \
         where seller.sid=bidding.sid \
         and bidding.Bid_Finalise=0"
    rec=conn.select_data(sql)
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("Seller id\tUser id\t\tProduct id\t\tBid id\t\tExpiry Date\tOffer Price\tBidding Price\tBid Finalise")
    print("-----------------------------------------------------------------------------------------------------------------------")
    for i in rec:
        for j in i:
            print(j,end="\t\t")
        print("")
    print("-----------------------------------------------------------------------------------------------------------------------")
    bid=lib.input_Bid()
    if bid==0:
        print("Exiting from Finalise Bid")
        return
    sql:str="select count(*) from bidding where Bid_Finalise=0 and Bid="+str(bid)
    is_bid_exist:bool=conn.is_record_exist(sql)
    if is_bid_exist==False:
        print("Invalid Bid Id")
        print("Exiting from finalise Bid")
        return
    print("Bid finalised successfully")
    conn.update_data("update bidding set Bid_Finalise=1 where Bid="+str(bid),0)

def payment()->None:
    print("\n--------Payment--------")
    finalised=conn.select_data("select Bid, Sid, Uid, Bidding_Price,security_fees from bidding where Bid_Finalise=1")
    if len(finalised)==0:
        print("No bids for payment")
        return         
    print("\nFinalised Bids")
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("Biddig Id\tSeller Id\tUser Id\t\tBid Price(Rs)\tSecurity money(Rs)")
    print("-----------------------------------------------------------------------------------------------------------------------")
    for row in finalised:
        for col in row:
            print(col,end="\t\t")
        print("")
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("")
    bid=lib.input_Bid()
    if bid==0:
        print("Exiting from Payment")
        return
    amount= conn.select_data("select Bidding_Price from Bidding where Bid="+str(bid))[0][0]
    final_amt=amount-conn.fetch_secuity_money_bid(bid)
    print("Payment Rupees: ",final_amt,"for Item name: ",(conn.get_product_name(bid))[0][0])
    cardnum=lib.Input_card_num()
    if cardnum=="":
        print("Exiting from Payment")
        return
    name=lib.input_text("Enter the card name: ",30)
    if name=="":
        print("Exiting from Payment")
        return
    date=lib.input_date()
    if date=="":
        print("Exiting from Payment")
        return

    choice = lib.pay_cancel_menu()
    if choice==2:
        return
    
    cardnum=cardnum.replace("-","")
    ret=conn.insert_payment("insert into payment(Card_No, Card_Name, Expiry_Date, Bid, Amount) \
    values('"+cardnum+"','"+name+"','"+date+"',"+str(bid)+","+str(final_amt)+")")
    if ret==1:
        conn.update_data("update bidding set Bid_Finalise=2 where Bid="+str(bid),0)


def display_processed_bids()->None:
    payments=conn.select_data("Select Card_No, Card_Name, Expiry_Date, Bid, Amount from payment ")
    print("\n--------Processed Bids--------")
    print("-----------------------------------------------------------------------------------------------")
    print("Card Number\t\t\tCard Name\tCard Expiry Date\tBidd Id\t\tAmount Paid")
    print("-----------------------------------------------------------------------------------------------")
    for payment in payments:
        i=1
        for col in payment:
            if i==1:
                print(lib.format_cardno(col),end="\t\t")
            else:
                print(col,end="\t\t")
                
            i=i+1       
            

        print("")
    print("-----------------------------------------------------------------------------------------------")
display_processed_bids()



