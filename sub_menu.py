import item
import mysql_connection
import sales
import bid
import library as lib

def auction_bidding_menu(uid: str)->None:
    while True:
        try:
            print("\n--------Bid Menu--------")
            print("1)Display Bids\n2)Add Bid\n3)Edit Bid\n4)Delete Bid\n5)Payment\n6)Processed Bids\n7)Exit")
            ch=lib.input_int("Enter your choice number: ")
            if ch==1:
                bid.display_bid()
            elif ch==2:
                bid.add_bid(uid)
            elif ch==3:
                bid.update_bid()
            elif ch==4:
                bid.delete_bid()
            elif ch==5:
                bid.payment()
            elif ch==6: 
                bid.display_processed_bids()
            elif ch==7:
                print("Exiting from Bid Menu.\n")
                break
        except Exception as error:
            print("Error: ",error)        
            print("Exception:Wrong Input")

def auction_item_menu()->None:
    while True:
        try:
            print("\n--------Item Menu--------")
            print("1)Display Items\n2)Add Item\n3)Edit Item\n4)Delete Item\n5)Exit\n")
            ch=lib.input_int("Enter your choice no.: ")
            if ch==1:
                item.display_item()
                continue
            elif ch==2:
                item.add_item()
                continue
            elif ch==3:
                item.edit_item()
                continue
            elif ch==4:
                item.delete_item()
                continue
            elif ch==5:
                print("Exiting from Item Menu.\n")
                break
            else:
                print("Wrong input. Ener again.")
        except Exception as error:
            print("Error: ",error)
            print("Exception:Wrong Input")

def auction_seller_menu(uid: str)->None:
    while True:
        try:
            print("\n--------Sales Menu--------")
            print("1)Display Sales\n2)Add Sales\n3)Edit Sales\n4)Delete Sales\n5)Finalise bids\n6)Confirm Payment\n7)Exit")
            ch=lib.input_int("Enter your choice: ")
            if ch==1:
                sales.display_sales()
            elif ch==2:
                sales.add_sales(uid)
            elif ch==3:
                sales.update_sales()
            elif ch==4:
                sales.delete_sales()
            elif ch==5:
                sales.finalising_bids()
            elif ch==6:
                sales.payment_confirmation()
            elif ch==7:
                print("Exiting from Sales Menu.\n")
                break
        except Exception as error:
            print("auction_seller_menu Error: ",error)
            print("Wrong Input")

def auction_sub_menu(uid: str)->None:
    user_name=mysql_connection.get_user_name(uid)
    print("Welcome [",uid,"][",user_name,"]\n")
    while True:
        try:
            print("--------Main Menu--------")
            print("1)Items\n2)Sales\n3)Bid\n4)Log Out\n")
            op=lib.input_int("Enter your choice: ")
            if op==1:
                auction_item_menu()
            elif op==2:
                auction_seller_menu(uid)
            elif op==3:
                auction_bidding_menu(uid)
            elif op==4:
                print("Do you want to exit from E-Auction?")
                ch=lib.yes_no_menu()
                if ch==1:
                    break
            else:
                print("Wrong Input")
        except Exception as error:
            print("Error: ",error)
            

