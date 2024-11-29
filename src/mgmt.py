import os
from tabulate import tabulate
class Mgmt:

    def addEmp(self,e):

        fp = open("data.txt",'a')
        fp.write(str(e))
        fp.close()
    
    def display(self):

        if(os.path.exists("data.txt")):
            table_data = []
            fp = open("data.txt",'r')
            # print(fp.read())  # to display all customer
            #to display customer one by one
            for member in fp:
                data = member.strip().split(',')
                table_data.append(data)
            
            fp.close()
            
            headers= ['ID','Name','Meals Per Month','Total Fees','Fees Paid','Fees Remaining','PhoneNo']
            print(tabulate(table_data,headers=headers,tablefmt='grid'))

        else:
            print("Wrong File Name or No such file Present in Directory")
    
    def searchEmp(self,id):

        with open("data.txt",'r') as fp:
            table_data = []
            for member in fp:
                try:
                    member.index(str(id),0,4)
                    print("record found")
                    #print(e)
                    data = member.strip().split(',')
                    table_data.append(data)
                    headers= ['ID','Name','Meals Per Month','Total Fees','Fees Paid','Fees Remaining','PhoneNo']
                    print(tabulate(table_data,headers=headers,tablefmt='grid'))
                    break
                except ValueError:
                    pass

            else:
                print("record Not found")


    def DeleteEmp(self,id):

        records = []
        found = False

        if len(str(id))==3:
            with open("data.txt",'r') as fp:
                
                for e in fp:
                    try:
                        e.index(str(id),0,4)
                        k=e

                    except ValueError:
                        records.append(e)

                    else:
                        found = True

            if(found == True):
                
                table_data = [k.strip().split(',')]
                headers = ['ID', 'Name', 'Meals Per Month', 'Total Fees', 'Fees Paid', 'Fees Remaining', 'PhoneNo']
                print(tabulate(table_data, headers=headers, tablefmt='grid'))

                confirmation = input("Do u really want to delete customer(yes/no)")
                if confirmation.lower() == "yes" or confirmation.lower() == 'y':
                    with open("data.txt",'w') as fp:
                        for e in records:
                            fp.write(e)
                    print("id Deleted")
                
                else:
                    print("Deletion cancel")

            else:
                print("record Not Found")
        
        else: 
            print("Invalid ID")
        

    def UpdateCustomer(self,id):

        myrecords = []
        found=False
        with open ("data.txt",'r') as fp:
            for e in fp:
                try:
                    e.index(str(id),0,4)
                
                except:
                    myrecords.append(e)
                
                else:
                    ch = input("Do You want to change Name (y/n):")

                    if ch.lower()=="y":
                        name = input("Enter New Name")
                        splitted_data=e.split(',')
                        splitted_data[1]=name
                        k= ','.join(splitted_data)
                        myrecords.append(k)
                    
                    ch = input("Do You want to change fees_paid (y/n):")

                    if ch.lower()=="y":
                        fees = input("Enter fees paid")
                        splitted_data=e.split()
                        splitted_data[2]=fees
                        k = ','.join(splitted_data)
                        myrecords.append(k)
                    
                    found = True

        if (found == True):
            with open ("data.txt",'w') as fp:
                for c in myrecords:
                    fp.write(c)
        
        else:
            print("record Not Found")
    
    def sortCustomer(self,field):

        if os.path.exists('data.txt'):

            with open ("data.txt",'r') as fp:
                customer_list = []

                for line in fp:
                    customer_list.append(line.strip().split(','))
                
                if field=="id":
                    customer_list.sort(key=lambda x:int(x[0]))
                
                elif field=="name":
                    customer_list.sort(key=lambda x: (x[1]).lower())
                
                elif field=="fees_paid":
                    customer_list.sort(key= lambda x:int(x[2]))
                
                else:
                    print('choose the correct input as :id,name,fees_paid')
                
                headers= ['ID','Name','Fees_Paid','Meals Per Day']
                print(tabulate(customer_list,headers=headers,tablefmt='grid'))

        else:
            print("File Not Found or Wrong File Name")
    
    def FilterCustomer(self):
        pass
                


