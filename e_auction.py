import register
import sub_menu
import library as lib

def auction_menu():
    while True:
        try:
            print("1)Register\n2)Log In\n3)Help\n4)Exit")
            alt=lib.input_int("Enter your choice no.: ")
           
            if alt==1:
                register.register()
                continue
            elif alt==2:
                uid=register.login()
                if len(uid)==0:
                    continue
                else:
                    sub_menu.auction_sub_menu(uid)
                    break
            elif alt==3:
                lib.help_box()
            elif alt==4:
                if lib.yes_no_menu()==1:
                    break
            else:
               print("Invalid input. Enter again.\n") 
        except Exception as error:
            print("Error: ",error)
            print("Exception : Wrong Input\n")
                      
                
print("-----------------------------------------------------------------------")                
print('|                       Welcome to E-auction                          |')
print("-----------------------------------------------------------------------")                

def start():
    try:
        auction_menu()
    except Exception as error:
        print(" start Error: ",error)


start()
    
