import mysql_connection as conn
import library as lib 
def add_item()->None:
    print("\n--------Add Items--------")
    pid=lib.input_new_pid()
    if pid=="":
        print("Exiting from add item")
        return ""
    name=lib.input_text("Enter product name: ",20)
    if name=="":
        print("Exiting from add item")
        return ""
    qty=lib.input_int("Enter the quantity: ")
    if qty==0:
        print("Exiting from add item")
        return
    comp_name=lib.input_text("Enter the company name: ",20)
    if comp_name=="":
        print("Exiting from add item")
        return ""
    date=lib.input_date("Enter the manufacturing date(YYYY-MM-DD): ")
    if date=="":
        print("Exiting from add item")
        return ""
    conn.insert_data("insert into product(Pid,Name, Qty, Company_Name, Mfg_Date) \
                        values('"+pid+"','"+name+"','"+str(qty)+"','"+comp_name+"','"+date+"')")

def display_item()->None:
    products=conn.select_data("select Pid, Name, Qty, Company_Name, Mfg_Date\
                          from product")
    print("-----------------------------------------Item List-------------------------------------------------")
    print("SNo\tProduct Id\tProduct Name\tQty\t\tCompany Name\t\tMfg_Date")
    print("---------------------------------------------------------------------------------------------------")
    i=1
    for prod in products:
        print(i,end="\t")
        i=i+1
        for col in prod:
            print(col,end="\t\t")
        print("")
    print("---------------------------------------------------------------------------------------------------")

def edit_item()->None:
    print("\n--------Edit Items--------")
    pid=lib.input_Product()
    if pid=="":
        print("Exiting from edit item")
        return ""
    oldqty=conn.select_data("Select Qty from product where Pid='"+pid+"'")
    print("Old quantity is: ",oldqty[0][0])
    qty=lib.input_int("Enter new quantity to update: ")
    if qty==0:
        print("Exiting from edit item")
        return 
    conn.update_data("update product set Qty="+str(qty)+" where Pid='"+pid+"'")
    print("")
    display_item()
    print("Updated product id ",pid," successfully.")

def delete_item()->None:
    print("\n--------Delete Items--------")
    pid=lib.input_Product()
    if pid=="":
        print("Exiting from delete item")
        return ""
    conn.delete_data("delete from product where Pid='"+pid+"'")
    print("")
    display_item()
    print("Deleted product id ",pid," successfully.")









