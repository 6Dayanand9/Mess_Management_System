from info import MemberInfo
from mgmt import Mgmt

if(__name__)=="__main__":
    choice = 0
    k = Mgmt()
    while choice!=10:
        print("="*20)
        print("Enter 1 to add Emp")
        print("Enter 2 to display all Emp")
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