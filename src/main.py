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
            id = int(input("Enter ID :"))
            nm = input("Enter Name :")
            fees_paid = int(input("Enter Fees Paid"))
            meal_per_day = int(input("Enter Meal per day(1/2/3)"))
            m = MemberInfo(id,nm,fees_paid,meal_per_day)
            k.addEmp(m)
        
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
            