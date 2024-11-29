from info import MemberInfo
from mgmt import Mgmt

if(__name__)=="__main__":
    choice = 0

    k = Mgmt()
    while choice!=10:
        print("="*20)
        print("Enter 1 to add Emp")
        print("Enter 2 to display all Emp")
        print("Enter 3 to Search Customer By id")
        print("Enter 4 to Delete Customer By Id")
        print("Enter 5 to Update Customer By Id")
        print("Enter 6 to Sort Customer by Id,Name,Fees_Paid")
        print("="*20)
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
            id = int(input("Enter Id to Search"))
            k.searchEmp(id)
        
        elif choice==4:
            id = int(input("Enter Id to Search"))
            k.DeleteEmp(id)
        
        elif choice==5:
            id = int(input("Enter id to update"))
            k.UpdateCustomer(id)
        
        elif choice == 6:
            k.sortCustomer(input("Sort by (id, name, fees_paid): "))
            
        elif choice ==7:
            k.FilterCustomer()