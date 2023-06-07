import subprocess as sp
import pymysql
import pymysql.cursors
from prettytable import PrettyTable

def Insert_Payment():
    try:
        row={}
        print("Enter Payment Details:")
        row["OrderNo"]=int(input("Order Number: "))
        row["Mode"]=input("Payment Mode (Cheque/Cash): ")
        flag=0
        if(row["Mode"]=="Cheque"):
            row["Cheque_no"]=int(input("Cheque Number: "))
            flag=1
        row["Amount"]=int(input("Amount: "))
        row["Payment_date"]=input("Payment Date (YYYY-MM-DD): ")
        if(flag==1):
            query="INSERT INTO Payment(Order_no,Pay_Mode,Cheque_no,Amount,Pay_date) VALUES ( %d,'%s',%d,%d,'%s')" % (
            row["OrderNo"], row["Mode"], row["Cheque_no"],row["Amount"], row["Payment_date"])
        else:
            query="INSERT INTO Payment(Order_no,Pay_Mode,Cheque_no,Amount,Pay_date) VALUES ( %d,'%s',NULL,%d,'%s')" % (
            row["OrderNo"], row["Mode"],row["Amount"], row["Payment_date"])
        cur.execute(query)
        con.commit()
        print("Inserted Into Database")
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
    return

def Insert_Banks():
    try:
        row={}
        print("Enter Details of Bank: ")
        row["IFSC"]=input("Branch IFSC: ")
        row["Name"]=input("Name of Bank: ")
        row["Address"]=input("Address: ")

        query="INSERT INTO Banks(Branch_IFSC,Name_of_Bank,Bank_Address) VALUES ('%s','%s','%s')" % (
        row["IFSC"],row["Name"], row["Address"])

        cur.execute(query)
        con.commit()
        print("Inserted Into Database")
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
    return

def Insert_Employee_family():
    try:
        row={}
        print("Enter details of employee family members: ")
        row["id"]=int(input("Emplpoyee Id: "))
        name= (input("Name (Fname Lname)" )).split(' ')
        row["Fname"]=name[0]
        row["Lname"]=name[1]
        row["relation"]=input("Relation with emoployee: ")
        row["DOB"]=input("DOB (YYYY-MM-DD): ")
        row["Gender"]=input("Gender (M/F): ")

        query="INSERT INTO Employee_Family_details(Employee_id,FName ,Lname, Relation,DOB, Gender) VALUES (%d,'%s','%s','%s','%s','%s')" % (
        row["id"], row["Fname"],row["Lname"],row["relation"],row["DOB"],row["Gender"])

        cur.execute(query)
        con.commit()
        print("Inserted Into Database")
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
    return

def Insert_Pending_Payment():
    try:
        row={}
        print("Enter details of pending payment: ")
        row["id"]=int(input("Distributor ID: "))
        row["pending_id"]=int(input("Order Id: "))
        query="INSERT INTO Pending_payments( Distributor_id  ,Pending_Order_id) VALUES ( %d,%d)" % (
        row["id"],row["pending_id"])

        cur.execute(query)
        con.commit()
        print("Inserted Into Database")
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
    return

# def Insert_Dependants():
#     try:
#         row={}
#         name=(input("Name (Fname Lname): ")).split(' ')
#         row["Fname"]=name[0]
#         row["Lname"]=name[1]
#         row["DOB"]=input("DOB (YYYY-MM-DD): ")
#         row["Gender"]=input("Gender (M/F): ")

#         query="INSERT INTO Dependants(FName, LName  , DOB , Gender) VALUES ('%s','%s' '%s' ,'%c')" % (
#         row["Fname"],row["Lname"],row["DOB"],row["Gender"])

#         cur.execute(query)
#         con.commit()
#         print("Inserted Into Database")
#     except Exception as e:
#         con.rollback()
#         print("Failed to insert into database")
#         print(">>>>>>>>>>>>>", e)
#     return

def Insert_Order_Desc():
    try:
        row={}
        row["Order_no"]=int(input("Order Number : "))
        row["Product_no"]=int(input("Product Number: "))
        row["Quantity"]=int(input("Quantity ordered: "))

        query=" INSERT INTO Order_Description(Order_no, Product_no,Quantity) VALUES (%d,%d,%d)" % (
        row["Order_no"],row["Product_no"], row["Quantity"])

        cur.execute(query)
        con.commit()
        print("Inserted Into Database")
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
    return

def Insert_LoanTakers():
    try:
        row={}
        row["loan_id"]=int(input("Loan id: "))
        taker=input("Who has taken loan (Employee/Owner) : ")
        if(taker=="Employee"):
            row["emp_id"]=int(input("Employee id: "))
            query="INSERT INTO Loan_Takers(Loan_id ,Employee_id,Owner_id) VALUES (%d,%d,NULL)" % (
            row["loan_id"],row["emp_id"])
        else:
            row["owner_id"]=int(input("Owner id: "))
            query="INSERT INTO Loan_Takers(Loan_id ,Employee_id,Owner_id) VALUES (%d,NULL,%d)" % (
            row["loan_id"],row["owner_id"])
        cur.execute(query)
        con.commit()
        print("Inserted Into Database")
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
    return

def Insert_Loan():
    try:
        row={}
        print("Insert details of loan: ")
        row["id"]=int(input("Loan id: "))
        row["provider"]=int(input("Loan Provider: "))
        row["principal"]=int(input("Principal Amount of Loan: "))
        row["interest"]=int(input("Interest: "))
        row["collateral"]=input("Collateral: ")
        row["tenure"]=int(input("Tenure of loan: "))
        row["approval_date"]=input("Loan Approval date (YYYY-MM-DD): ")
        row["installments"]=int(input("Installments to be paid: "))

        query="INSERT INTO Loan(Loan_id ,Provider ,Principal_amt ,Interest_charge, Collateral   ,Loan_tenure ,Loan_approval_date,Installments) VALUES (%d,%d,%d,%d,'%s',%d,'%s',%d)" % (
        row["id"],row["provider"],row["principal"],row["interest"],row["collateral"],row["tenure"],row["approval_date"],row["installments"])


        cur.execute(query)
        con.commit()
        print("Inserted Into Database")
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
    return

def Insert_Bank_account():
    try:
        row={}
        print("Enter details of Bank Account: ")
        row["number"]=int(input("Account Number: "))
        row["holder"]=input("Name of Holder: ")
        row["type"]=input("Account type: ")
        row["balance"]=int(input("Current Balance: "))
        row["IFSC"]=input("Branch IFSC: ")
        
        query="INSERT INTO Bank_account(Account_number,Name_of_holder,Account_type,Current_Balance,Branch_IFSC) VALUES (%d,'%s','%s',%d,'%s')" % (
        row["number"],  row["holder"],row["type"],row["balance"], row["IFSC"])

        cur.execute(query)
        con.commit()
        print("Inserted Into Database")
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
    return
    
def Insert_Inventory():
    try:
        row={}
        print("Enter Details of New Product")
        row["ItemNo"]=int(input("Item ID: "))
        row["ItemName"]=input("Item Name: ")
        row["Availability"]=int(input("Available amount of prouduct: "))
        row["Profit"]=float(input("Profit: "))
        row["MRP"]=float(input("MRP: "))
        purchase = row["MRP"] - row["Profit"]

        query="INSERT INTO Inventory(Item_number,Item_name,Availability,Profit,Mrp,Purchase_cost) VALUES (%d,'%s',%d,%f,%f,%f)" % (
        row["ItemNo"],row["ItemName"],row["Availability"],row["Profit"], row["MRP"], purchase)

        cur.execute(query)
        con.commit()
        print("Inserted Into Database")
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
    return 

def Insert_Department():
    try:
        row={}
        print("Enter New Department Details:")
        row["Dno"]=int(input("Department Number: "))
        row["Dname"]=input("Department Name: ")
        row["Manager_id"]=int(input("Manger id: "))

        query="INSERT INTO Department(Dno,Dname,Manager_id) VALUES ( %d,'%s',%d)" % (
        row["Dno"],row["Dname"],row["Manager_id"])

        cur.execute(query)
        con.commit()
        print("Inserted Into Database")
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
    return 

def Insert_Distributors():
    try:
        row={}
        print("Enter Distributor Details: ")
        row["id"]=int(input("Distributor ID: "))
        row["Name"]=input("Name: ")
        row["Bank_Acc"]=int(input("Bank Account Detail: "))
        row["IFSC"]=input("Bank IFSC: ")
        row["Area"]=input("Area of Control: ")
        row["Yearly"]=int(input("Yearly Sales: "))
        row["salesman"]=int(input("Salesman ID: "))
        row["Address"]=input("Address: ")
        row["Phone_NO"]=int(input("Phone Number: "))
        row["GST"]=input("G.S.T. Number: ")

        query="INSERT INTO Distributors( Distributor_id,Distributor_name, Bank_Acc_No,IFSC,Area_of_jurisdiction, Yearly_Sales,Area_Salesman_id,Address,Phone_no,GST) VALUES (%d,'%s',%d,'%s','%s',%d,%d,'%s',%d,'%s')" % (
        row["id"],row["Name"],row["Bank_Acc"],row["IFSC"], row["Area"],row["Yearly"],row["salesman"],row["Address"],row["Phone_NO"], row["GST"])

        cur.execute(query)
        con.commit()
        print("Inserted Into Database")
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
    return 

def Insert_Spendings():
    try:
        row={}
        print("Enter Spending Details: ")
        row["Department Number"]=int(input("Department Number: "))
        row["AmountSpend"]=int(input("Amount Spend: "))
        row["Date"]=input("Date of Spending (YYYY-MM-DD): ")
        row["Description"]=input("Any details to be added: ")

        query="INSERT INTO Department_Spendings(Department_Number,Amount_Spend,Date_of_spend,Description) VALUES (%d,%d,'%s','%s')" % (
        row["Department Number"], row["AmountSpend"], row["Date"], row["Description"])

        cur.execute(query)
        con.commit()
        print("Inserted Into Database")
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
    return 

def Insert_WorksFor():
    try:
        row={}
        row["owner_id"]=int(input("Owner id: "))
        row["emp_id"]=int(input("Employee id: "))
        row["dept_id"]=int(input("Department id: "))

        query="INSERT INTO Works_for(Owner_id,Employee_id,Department_id) VALUES (%d,%d,%d)" % (
        row["owner_id"],row["emp_id"], row["dept_id"]) 
        cur.execute(query)
        con.commit()
        query= "Select Manager_id FROM Department WHERE Dno=%d" % (row["dept_id"])
        cur.execute(query)
        row=cur.fetchall()
        query="UPDATE Employee SET Manager_id=%d WHERE Id_number=%d" % (row[0][0],row["emp_id"])
        cur.execute(query)
        con.commit()
        print("Inserted Into Database")
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
    return 

def Insert_Monitors():
    try:
        row={}
        row["order_id"]=int(input("Order Number: "))
        row["dist_id"]=int(input("Distributor id: "))
        row["emp_id"]=int(input("Employee ID: "))
        row["owner_id"]=int(input("Owner ID: "))

        query="INSERT INTO Monitors(Order_no ,Distributor_id ,Employee_id,Owner_id ) VALUES ( %d,%d,%d,%d)" % (
        row["order_id"],row["dist_id"],row["emp_id"], row["owner_id"])

        cur.execute(query)
        con.commit()
        print("Inserted Into Database")
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
    return 

def Insert_Employee():
    try:
        row={}
        print("Enter Employee Details:")
        row["ID_number"]=int(input("Enter ID of Employee: "))
        name=(input("Name (Fname Lname): ")).split(' ')
        row["Fname"]=name[0]
        row["Lname"]=name[1]
        row["Salary"]=int(input("Enter Salary: "))
        row["Gender"]=input("Gender (M/F): ")
        row["Address"]=input("Address: ")
        row["DOB"]=input("Date of Birth (YYYY-MM-DD): ")
        row["Post"]=input("Post: ")
        row["Acc_no"]=int(input("Account Number: "))

        query="INSERT INTO Employee(Employee_id,Fname,Lname,Post,Salary,Gender,Address,DOB,Acc_no,Manager_id) VALUES (%d ,'%s','%s','%s',%d,'%c','%s','%s',%d,NULL)" % (
        row["ID_number"],row["Fname"],row["Lname"],row["Post"],row["Salary"],row["Gender"],row["Address"],row["DOB"],row["Acc_no"])
        
        cur.execute(query)
        con.commit()
        print("Inserted Into Database")
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return
        
def Insert_Orders():
    try:
        row={}
        print("Enter order details")
        row["Order No"]= int(input("Ordr Number: "))
        row["Customer Name"]= input("Enter Customer Name: ")
        row["Order Date"]=input("Enter Purchase Date (YYYY-MM-DD): ")
        row["Net Amount"]=int(input("Enter total Billing amount: "))
        row["Advance Paid"]=int(input("Enter advance Payment: "))
        row["Order Status"]=input("Enter Current Status of Order (Dispatched,To be Shipped, Delivered ): ")
        flag=0
        if row["Order Status"]=="Dispatched" :
            row["Shipping_Date"]=input("Enter Shipping Date (YYYY-MM-DD): ")
            flag=1
        row["Discount"]=int(input("Enter Discount Given: "))
        query=""
        if flag==1:
            query=" INSERT INTO Orders(Order_no,Customer_name,Order_date,Net_amount,Advance_paid,Order_status,Shipping_date,Discount) VALUES(%d,'%s','%s',%d,%d,'%s','%s',%d)" % (
            row["Order No"],row["Customer Name"],row["Order Date"],row["Net Amount"],row["Advance Paid"],row["Order Status"],row["Shipping_Date"],row["Discount"])
        else : 
            query=" INSERT INTO Orders(Order_no,Customer_name,Order_date,Net_amount,Advance_paid,Order_status,Shipping_date,Discount) VALUES(%d,'%s','%s',%d,%d,'%s',NULL,%d)" % (
            row["Order No"],row["Customer Name"],row["Order Date"],row["Net Amount"],row["Advance Paid"],row["Order Status"],row["Discount"])

        cur.execute(query)
        con.commit()

        print("Inserted Into Database")
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def Insert_Owner():
    try:
        # Takes emplyee details as input
        row = {}
        print("Enter new owner's details: ")
        row["Owner_id"] = int(input("Owner ID: "))
        name = (input("Name (Fname Lname): ")).split(' ')
        row["Fname"] = name[0]
        row["Lname"] = name[1]
        row["Equity_Share"]=int(input("Equity of owner: "))
        query="SELECT SUM(Equity_share) FROM Owner"
        cur.execute(query)
        output=cur.fetchall()
        if(row["Equity_Share"]+ output[0][0] > 100):
            print("Equity not balanced between owner")
        else:
            query = "INSERT INTO Owner(Fname, Lname,Owner_id,Equity_share) VALUES('%s', '%s',%d,%d)" % (
                row["Fname"], row["Lname"], row["Owner_id"], row["Equity_Share"])

            #print(query)
            cur.execute(query)
            con.commit()

            print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def Delete_Employee():
    try:
        id=int(input("Enter Employee id of employee to be fired: "))
        query= "Delete FROM Employee WHERE Employee_id=%d" % (id)
        cur.execute(query)
        con.commit()
        print("Employee Fired")
    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)
    return   

def Delete_Distributor():
    try:
        print("Enter Distributor Details")
        id=int(input("Distributor ID: "))
        area=input("Area of jurisdication: ")
        query="DELETE FROM Distributors WHERE Distributor_id=%d AND Area_of_jurisdiction='%s'" % (id,area)
        cur.execute(query)
        con.commit()
        print("Removed Distributor")
    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)
    return 

def Delete_Pending_payment():
    try:
        print("Enter details of order whose payment is not pending")
        order_id= int(input("Order id: "))
        query="DELETE FROM Pending_payments WHERE Pending_Order_id=%d" % (order_id)
        cur.execute(query)
        con.commit()
        print("Removed Order ID")
    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)
    return

def Delete_Owner():
    try:
        input("Enter details of owner leaving company")
        id=int(input("Owner id: "))
        query="DELETE FROM Owner WHERE Owner_id=%d" % (id)
        cur.execute(query)
        con.commit()
        print("Deleted Owner Entry")
    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)
    return  

def Delete_Loan():
    try:
        print("Enter details of Loan:")
        id=int(input("Enter Loan id: "))
        query="DELETE FROM Loan WHERE Loan_id=%d" % (id)
        cur.execute(query)
        con.commit()
        print("Removed from loan entries")
    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)
    return  

def Update_Employee_address():
    try:
        print("Enter details of employee:")
        id=int(input("Employee id: "))
        address=input("New Address: ")
        query="UPDATE Employee SET Address='%s' WHERE Employee_id=%d" % ( address,id)
        cur.execute(query)
        con.commit()
        print("Updated Address")
    except Exception as e:
        con.rollback()
        print("Failed to update database")
        print(">>>>>>>>>>>>>", e)
    return  

def Update_Department():
    try:
        print("Enter New details:")
        dept=int(input("Department Number: "))
        id=int(input("New Manager ID: "))
        query="UPDATE Department SET Manager_id=%d WHERE Dno=%d" % (id,dept)
        cur.execute(query)
        con.commit()
        print("Updated Manager ID")
    except Exception as e:
        con.rollback()
        print("Failed to update database")
        print(">>>>>>>>>>>>>", e)
    return

def Update_Orders():
    try:
        print("Enter New details: ")
        order=int(input("Order Number: "))
        order_stat=input("Status of Order (Dispatched,To be Shipped, Delivered): ")
        shipping_date=-1
        query=""
        if order_stat=="Dispatched":
            shipping_date=input("Enter Shipping Date (YYYY-MM-DD): ")
            query="UPDATE Orders SET Order_status='%s', Shipping_date='%s' WHERE Order_no=%d" % (order_stat,shipping_date,order)
        else:
            query="UPDATE Orders SET Order_status='%s' WHERE Order_no=%d" % (order_stat,order)

        cur.execute(query)
        con.commit()
        print("Updated Status of Order")
    except Exception as e:
        con.rollback()
        print("Failed to update database")
        print(">>>>>>>>>>>>>", e)
    return

def Update_Owner():
    try:
        print("Enter new Details: ")
        id=int(input("Owner ID: "))
        equity= int(input("New Equity Share: "))
        query="SELECT SUM(Equity_share) FROM OWNER WHERE Owner_id!=%d" % (id)
        cur.execute(query)
        output=cur.fetchall()
        if(output[0][0]+ equity > 100):
            print("Share not balanced among owner")
        else:
            query="UPDATE Owner SET Equity_share=%d WHERE Owner_id=%d" % (equity,id)
            cur.execute(query)
            con.commit()
            print("Updated Owner Details")
    except Exception as e:
        con.rollback()
        print("Failed to update database")
        print(">>>>>>>>>>>>>", e)
    return

def Update_Salary():
    try:
        print("Enter details of employee:")
        id=int(input("Employee id: "))
        sal=int(input("Increment (in Rs): "))
        query="UPDATE Employee SET Salary = Salary+ %d WHERE Employee_id=%d" % (sal,id)
        cur.execute(query)
        con.commit()
        print("Updated Address")
    except Exception as e:
        con.rollback()
        print("Failed to update database")
        print(">>>>>>>>>>>>>", e)
    return 

def Update_Inventory():
    try:
        print("Enter the details: ")
        order=int(input("Product Number: "))
        available= int(input("Available Stock: "))
        query="UPDATE Inventory SET Availability=%d WHERE Item_number=%d" % (available,order)
        cur.execute(query)
        con.commit()
        print("Updated Product details")
    except Exception as e:
        con.rollback()
        print("Failed to update database")
        print(">>>>>>>>>>>>>", e)
    return

def display_distributer():
    try:
        id=int(input("Enter distributor id whose details need to be displayed: "))
        query ="SELECT * from Distributors where Distributor_id=%d"%(id)
        cur.execute(query)
        output=cur.fetchall()
        ret=len(output)
        if ret==0:
            print("No such distributor")
        else:
            myTable= PrettyTable(["Distributor_id","Distributor_name","Bank_Acc_no","IFSC","Area of Control","Sales","Salesman_id","Address","Phone Number","GST No."])
            for row in output:
                myTable.add_row(row)
            print(myTable)
    except Exception as e:
        print("Failed to display requirements")
        print(">>>>>>>>>>>>>", e)

def display_spendings():
    try:
        query="SELECT Department_Number, SUM(Amount_spend) as Spendings from Department_Spendings GROUP BY Department_Number ORDER BY spendings"
        myTable= PrettyTable(["Department_Number","Spendings"])
        cur.execute(query)
        output=cur.fetchall()
        for row in output:
            myTable.add_row(row)
        print(myTable)
    except Exception as e:
        print("Failed to display requirements")
        print(">>>>>>>>>>>>>", e)

def num_employees():
    try:
        query="SELECT COUNT(Employee_id) as Total_employees from Employee"
        cur.execute(query)
        output=cur.fetchall()
        print("Total Number of Employee: " + str(output[0][0]))
    except Exception as e:
        print("Failed to display requirements")
        print(">>>>>>>>>>>>>", e)

def total_loan():
    try:
        id=int(input("Enter Id for person whose total loan needs to be diplayed: "))
        query="SELECT SUM(Principal_amt) as Total_loan from Loan where Loan_id in (select Loan_id from Loan_Takers where Employee_id=%d or Owner_id=%d)"%(id,id) 
        cur.execute(query)
        output=cur.fetchall()
        ret=len(output)
        if ret ==0:
            print("This employee/ owner has not taken a loan")
        else:
            print("Total Loan taken " + str(output[0][0]))
            if (output[0][0]==0):
                return
            query="SELECT * from Loan where Loan_id IN (SELECT Loan_id from Loan_Takers where Employee_id=%d)"%(id)       
            cur.execute(query)
            output=cur.fetchall()
            myTable=PrettyTable(["Loan_id","Provider","Principal_Amt","Interest_charge","Collateral","Loan_tenure","Loan_approval_date","Installments"])
            for row in output:
                myTable.add_row(row)
            print(myTable)
    except Exception as e:
        print("Failed to display requirements")
        print(">>>>>>>>>>>>>", e)

def names_employees():
    try:
        start= input("Enter start letter(* if you want to display all names): ")
        myTable=PrettyTable(["Name","Salary"])
        if start=="*":
            query="SELECT CONCAT(CONCAT(Fname,' '),Lname) as Name, Salary from Employee"
            cur.execute(query)
            output=cur.fetchall()
            for row in output:
                myTable.add_row(row)
            print(myTable)
        else:
            query="SELECT CONCAT(CONCAT(Fname,' '),Lname) as Name, Salary from Employee WHERE CONCAT(CONCAT(Fname,' '),Lname) LIKE '%c%%'"%(start)
            print(query)
            cur.execute(query)
            output=cur.fetchall()
            ret=len(output)
            if ret ==0:
                print("No such employee")
            else:
                for row in output:
                    myTable.add_row(row)
            print(myTable)
                   
    except Exception as e:
        print("Failed to display requirements")
        print(">>>>>>>>>>>>>", e)

def Sales_distributor():
    print("Enter 1 to get Distributor with Minimum Yearly Sales")
    print("Enter 2 to get Distributor with Maximum Yearly Sales")
    myTable=PrettyTable(["Distributor_id","Distributor_Name","Yearly_sales"])
    choice= int(input("Enter your choice: "))
    if choice == 1:
        query="SELECT Distributor_id,Distributor_Name,Yearly_sales from Distributors where Yearly_sales IN (SELECT MIN(Yearly_sales) from Distributors)"
        cur.execute(query)
        output=cur.fetchall()
        for row in output:
            myTable.add_row(row)        
    elif choice ==2:
        query="SELECT Distributor_id,Distributor_Name,Yearly_sales from Distributors where Yearly_sales IN (SELECT MAX(Yearly_sales) from Distributors)"
        cur.execute(query)
        for row in cur:
            myTable.add_row(row)
    print(myTable)

def dispatch(choice):
    """
    Function that maps helper functions to option entered
    """
    if(choice==1):
        print("Enter 1 to include New Owner")
        print("Enter 2 to Hire Employee")
        print("Enter 3 to Insert Details of a new Bank Account")
        print("Enter 4 to create new Department")
        print("Enter 5 to Insert details of new Bank")
        print("Enter 6 to Insert details of a new payment")
        print("Enter 7 to Get a new Distributor")
        print("Enter 8 to Insert details of a pending payment")
        print("Enter 9 to Store details about spending of a Department")
        print("Enter 10 for a new Order")
        print("Enter 11 to give details of People Accountable for an Order")
        print("Enter 12 to Insert details of Employee's Boss and Department")
        print("Enter 13 to give Order Deatails for an order")
        print("Enter 14 for new item in inventory")
        print("Enter 15 to give details of a loan Taker")
        print("Enter 16 to Enter Dependants of an employee")
        print("Enter 17 to Insert details of a loan")
        print("Enter Anything Else to go back to Previous menu")
        ch=int(input("Enter your choice: "))
        if(ch == 1):
            Insert_Owner()
        elif(ch == 2):
            Insert_Employee()
        elif(ch == 3):
            Insert_Bank_account()
        elif(ch == 4):
            Insert_Department()
        elif(ch==5):
            Insert_Banks()
        elif(ch==6):
            Insert_Payment()
        elif(ch==7):
            Insert_Distributors()
        elif(ch==8):
            Insert_Pending_Payment()
        elif(ch==9):
            Insert_Spendings()
        elif(ch==10):
            Insert_Orders()
        elif(ch==11):
            Insert_Monitors()
        elif(ch==12):
            Insert_WorksFor()
        elif(ch==13):
            Insert_Order_Desc()
        elif(ch==14):
            Insert_Inventory()
        elif(ch==15):
            Insert_LoanTakers()
        elif(ch==16):
            Insert_Employee_family()
        elif(ch==17):
            Insert_Loan()
    if(choice==2):
        print("Enter 1 to Fire an Employee")
        print("Enter 2 to Remove a Distributor")
        print("Enter 3 When Owner Leaves Company")
        print("Enter 4 when a distributor has completed payment of an order")
        print("Enter 5 to Remove a loan Repaid")
        print("Enter Anything Else to go to previous Menu")
        ch=int(input("Enter the Choice: "))
        if(ch==1):
            Delete_Employee()
        elif(ch==2):
            Delete_Distributor()
        elif(ch==3):
            Delete_Owner()
        elif(ch==4):
            Delete_Pending_payment()
        elif(ch==5):
            Delete_Loan()
    elif(choice==3):
        print("Enter 1 to change Address of Employee")
        print("Enter 2 to change Manager ID of a department")
        print("Enter 3 to update order status and shipping date")
        print("Enter 4 to change equity of owner in a company")
        print("Enter 5 to give an Employee increment or decrement in salary")
        print("Enter 6 to Enter details of stock availabel of a product ")
        print("Enter Anything Else to go to previous Menu")
        ch = int(input("Enter the choice: "))
        if(ch==1):
            Update_Employee_address()
        elif(ch==2):
            Update_Department()
        elif(ch==3):
            Update_Orders()
        elif(ch==4):
            Update_Owner()
        elif(ch==5):
            Update_Salary()
        elif(ch==6):
            Update_Inventory()
    elif(choice==4):
        print("Enter 1 to display Details of a Distributor")
        print("Enter 2 to Diplay Spendings of Departments in Sorted Order")
        print("Enter 3 to Get Total number of employees")
        print("Enter 4 to Diplay Loans Taken by a specific Person")
        print("Enter 5 to Search for an Employee")
        print("Enter 6 to Get Distributor with Min/Max Sales")
        print("Enter Anything Else to go to previous Menu")
        ch=int(input("Enter your choice: "))
        if(ch==1):
            display_distributer()
        elif(ch==2):
            display_spendings()
        elif(ch==3):
            num_employees()
        elif(ch==4):
            total_loan()
        elif(ch==5):
            names_employees()
        elif(ch==6):
            Sales_distributor()
# Global
while(1):
    tmp = sp.call('clear', shell=True)
    
    # Can be skipped if you want to hardcode username and password
    username = input("Username: ")
    password = input("Password: ")

    try:
        # Set db name accordingly which have been create by you
        # Set host to the server's address if you don't want to use local SQL server 
        con = pymysql.connect(host='localhost',
                              user="root",
                              password=password,
                              db='team_6',
                            )
        tmp = sp.call('clear', shell=True)

        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")

        tmp = input("Enter any key to CONTINUE>")

        with con.cursor() as cur:
            while(1):
                tmp = sp.call('clear', shell=True)
                # Here taking example of Employee Mini-world
                print("1. Insert")  # Hire an Employee
                print("2. Delete")  # Fire an Employee
                print("3. Update")  # Promote Employee
                print("4. Query")  # Employee Statistics
                print("5. Logout")
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear', shell=True)
                if ch == 5:
                    exit()
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")

    except Exception as e:
        tmp = sp.call('clear', shell=True)
        print(e)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")