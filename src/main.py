from info import MemberInfo
from mgmt import Mgmt

if(__name__)=="__main__":
    choice = 0

    k = Mgmt()
    while choice!=10:
        print()
        print("="*20)
        print("Enter 1 to add Emp")
        print("Enter 2 to display all Emp")
        print("Enter 3 to Search Customer By id")
        print("Enter 4 to Delete Customer By Id")
        print("Enter 5 to Update Customer By Id")
        print("Enter 6 to Sort Customer by Id,Name,Fees_Paid,Remaining_Fees")
        print("Enter 7 to Filter Customer on Condition")
        print("Enter 8 to get the info of all Customer with Remaining Fees ")
        print("="*20)
        print()
        choice = int(input("Enter Choice :"))
        if choice == 1:
            #============================================================================================
            
            id = int(input("Enter ID :"))
            nm = input("Enter Name :")
            Total_Meals = int(input("Enter Total_Meal_Per_Month(30/60)"))

            if Total_Meals==30:
                Total_fee = 3000
            elif Total_Meals==60:
                Total_fee = 4500
            
            fees_paid = int(input("Enter Fees Paid"))
            remaining_fees = Total_fee - fees_paid
            
            phoneno = input("Enter Phone No(10 digits)")
            while len(phoneno)!=10 or not phoneno.isdigit():
                print('Invalid input! Please enter a valid 10-digit phone number.')
                phoneno = input("Enter Phone No(10 digits)")
            #--------------------------------------------------------------------------------------------
            m = MemberInfo(id,nm,Total_Meals,Total_fee,fees_paid,remaining_fees,phoneno)
            k.addEmp(m) 
            #============================================================================================

        elif choice==2:
            k.display()
        
        elif choice==3:
            try:
                id = int(input("Enter Id to Search"))
                k.searchEmp(id)
            except ValueError:
                print()
                print("***************************")
                print("\033[1mERROR:\033[0m Enter Id in Integer Format")
                print("***************************")
                print()
                
        
        elif choice==4:
            id = int(input("Enter Id to Search"))
            k.DeleteEmp(id)
        
        elif choice==5:
            id = int(input("Enter id to update"))
            k.UpdateCustomer(id)
        
        elif choice == 6:
            k.sortCustomer(input("Sort by (id, name, fees_paid,Remaining_Fees): "))
            
        elif choice ==7:
            condition=input("Enter Condition e.g., 'int(record[5]) > 1000'):")
            k.FilterCustomer(condition)
        
        elif choice ==  8:
            k.Remaining_Fees()