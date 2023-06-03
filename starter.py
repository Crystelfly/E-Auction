import mysql_connection as conn
def table_creation()->None:
    conn.drop_db()
    conn.table_creation("create table user(\
              Uid varchar(20) Primary key,\
              Name varchar(25),\
              User_type char(1),\
              Phone char(15),\
              Address varchar(30),\
              Password varchar(25))\
              ")

    conn.table_creation("create table product(\
              Pid varchar(20) Primary key,\
              Name varchar(25), Qty int,\
              Company_Name varchar(25),\
              Mfg_Date date)\
              ")
    

    conn.table_creation("create table seller(\
              Sid int Primary key,\
              Uid varchar(20), \
              Pid varchar(20), \
              Offer_Price int,\
              Expiry_Date date,\
              Security_Fees int,\
              FOREIGN KEY (Uid) REFERENCES User(Uid) on delete cascade,\
              FOREIGN KEY (Pid) REFERENCES Product(Pid) on delete cascade)\
              ")


    conn.table_creation("create unique index UK_Seller_Uid_Pid\
              on seller(Uid,Pid)\
              ")
    conn.table_creation("create table Bidding(\
              Bid int Primary key auto_increment,\
              Sid int,\
              Uid varchar(20),\
              Bidding_Price int,\
              Bid_Finalise int,\
              Security_Fees int,\
              FOREIGN KEY (Sid) REFERENCES Seller(Sid) on delete cascade,\
              FOREIGN KEY (Uid) REFERENCES User(Uid) on delete cascade)\
              ")
    conn.table_creation("create table Payment(\
              Card_No char(16),\
              Card_Name varchar(30),\
              Expiry_Date date,\
              Bid int,\
              Amount int,\
              FOREIGN KEY (Bid) REFERENCES Bidding(Bid) on delete cascade)\
              ")
    

def insert_records():
    table_creation()
    conn.insert_data("insert into user(Uid, Name, User_type, Phone, Address, Password)\
                     values('Anusha', 'Anusha Singh', 'B', '1234251871', 'Delhi', 'Anusha123') ")
    conn.insert_data("insert into user(Uid, Name, User_type, Phone, Address, Password)\
                     values('Aradhya', 'Aradhya Singh', 's', '9834255871', 'Delhi', 'Aradhya123') ")
    conn.insert_data("insert into user(Uid, Name, User_type, Phone, Address, Password)\
                     values('Rohan', 'Rohan Sharma', 'B', '8822251871', 'Mumbai', 'Rohan123') ")
    conn.insert_data("insert into user(Uid, Name, User_type, Phone, Address, Password)\
                     values('Ankit', 'Ankit Mishra', 's', '1237751991', 'Ranchi', 'Ankit123') ")
    conn.insert_data("insert into product(Pid, Name, Qty, Company_Name, Mfg_Date)\
                     values('mob', 'Mobile', '100', 'Samsung', '2022-10-08') ")
    conn.insert_data("insert into product(Pid, Name, Qty, Company_Name, Mfg_Date)\
                     values('airp', 'Air pod', '200', 'Apple', '2022-10-07') ")
    conn.insert_data("insert into product(Pid, Name, Qty, Company_Name, Mfg_Date)\
                     values('lap', 'Laptop', '300', 'Apple', '2022-10-06') ")
    conn.insert_data("insert into product(Pid, Name, Qty, Company_Name, Mfg_Date)\
                     values('tab', 'Tablet', '400', 'Acer', '2022-10-05') ")
    conn.insert_data("insert into seller(Sid,Uid, Pid, Offer_Price, Expiry_Date, Security_Fees)\
                     values(1,'Ankit', 'mob', '7000', '2022-12-8', 500) ")
    conn.insert_data("insert into seller(Sid,Uid, Pid, Offer_Price, Expiry_Date, Security_Fees)\
                     values(2,'Aradhya', 'tab', '2000', '2022-12-30', 100)")
    conn.insert_data("insert into seller(Sid,Uid, Pid, Offer_Price, Expiry_Date, Security_Fees)\
                     values(3,'Aradhya', 'lap', '6000', '2029-11-30', 300) ")
    conn.insert_data("insert into bidding(Sid, Uid, Bidding_Price, Bid_Finalise, Security_Fees) values(1, 'Anusha', 6000, 0, 500) ")
    conn.insert_data("insert into bidding(Sid, Uid, Bidding_Price, Bid_Finalise, Security_Fees) values(2, 'Rohan', 1700, 1, 100) ")
    conn.insert_data("insert into bidding(Sid, Uid, Bidding_Price, Bid_Finalise, Security_Fees) values(3, 'Rohan', 5500, 0, 300) ")
        
insert_records()


  





