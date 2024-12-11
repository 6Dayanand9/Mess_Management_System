import os
from tabulate import tabulate
# -----------------------------------------------------------------------------------------------------
class Mgmt:

    def addEmp(self,e):

        fp = open("data.txt",'a')
        fp.write(str(e))
        fp.close()
# =====================================================================================================

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

# =====================================================================================================
    
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

# =====================================================================================================

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
        
# =====================================================================================================
    def UpdateCustomer(self,id):
        myrecords = []
        found = False 

        with open("data.txt", 'r') as fp:
            for e in fp:
                #print(f"Checking record: {e.strip()}")
                if e.strip().startswith(str(id) + ",") and not found:
                    print("Record found for update.")
                    splitted_data = e.strip().split(',')

                    # Update Name
                    ch = input("Do you want to change Name (y/n): ").lower()
                    if ch == "y":
                        name = input("Enter New Name: ")
                        splitted_data[1] = name

                    # Update Fees Paid
                    ch = input("Do you want to change fees_paid (y/n): ").lower()
                    if ch == "y":
                        try:
                            fees = int(input("Enter Fees Paid: "))
                        except ValueError:
                            print("Invalid input. Please enter a number.")
                            return

                        total_fees = 3000 if int(splitted_data[2]) == 30 else 4500
                        remaining_fees = total_fees - fees
                        splitted_data[4] = str(fees)
                        splitted_data[5] = str(remaining_fees)

                    # Reconstruct the updated record
                    e = ','.join(splitted_data) + '\n'
                    found = True
                myrecords.append(e.strip())

        print("Updated Records:")
        
        if found:
            print("Writing records back to file...")
            with open("data.txt", 'w') as fp:
                for record in myrecords:
                    fp.write(record + '\n')
            print("Record Updated Successfully.")
        else:
            print("Record Not Found.")


# =====================================================================================================
    
    def sortCustomer(self,field):
    # Check if the file exists
        if os.path.exists('data.txt'):
            with open("data.txt", 'r') as fp:
                customer_list = []

                # Read and split the file lines into lists
                for line in fp:
                    customer_list.append(line.strip().split(','))

                # Check for valid fields and sort accordingly
                if field.lower() == "id":
                    customer_list.sort(key=lambda x: int(x[0]))  # Sort by ID (index 0)
                elif field.lower() == "name":
                    customer_list.sort(key=lambda x: x[1].lower())  # Sort by Name (index 1)
                elif field.lower() == "fees_paid":
                    customer_list.sort(key=lambda x: int(x[4]))  # Sort by Fees Paid (index 4)
                
                elif field.lower() == "remaining_fees":
                    customer_list.sort(key=lambda x: int(x[5]),reverse=True) # Sort by remaining Fees
                else:
                    print('Invalid field. Choose from: id, name, fees_paid.')
                    return

                # Define table headers dynamically based on file format
                headers = ['ID', 'Name', 'Meals Per Month', 'Total Fees', 'Fees Paid', 'Remaining Fees', 'Phone Number']

                # Print sorted data as a table
                print(tabulate(customer_list, headers=headers, tablefmt='grid'))

        else:
            print("File not found or wrong file name. Please check and try again.")
    
# =====================================================================================================
    
    def FilterCustomer(self,condition):
        if os.path.exists('data.txt'):

            with open ('data.txt','r') as fp:
                table_data = []
                headers=['ID','NAME','MEALS PER MONTH','TOTAL FEES','FEES PAID','REMAINING FEES','PHONENO']

                for line in fp:
                    record = line.strip().split(',')
                    if eval(condition):
                        table_data.append(record)

                if table_data:
                    print('Filtered Employees :')
                    print(tabulate(table_data,headers=headers,tablefmt='grid'))

                else:
                    print('No record Found')
        else:
            print("Wrong File Name Or No Such File Present In Directory")

# =====================================================================================================

    def Remaining_Fees(self):
        if os.path.exists("data.txt"):
            with open ("data.txt",'r') as fp:
                table_data = []
                headers=['ID','NAME','MEALS PER MONTH','TOTAL FEES','FEES PAID','REMAINING FEES','PHONENO']
                for line in fp:
                    record = line.strip().split(',')
                    if int(record[5]) > 0:
                        table_data.append(record)
                
                if table_data:
                    print('Member With Remaining Fees :')
                    print(tabulate(table_data,headers=headers,tablefmt='grid'))
                
                else:
                    print("No Data To Print")
        else:
            print("File Not Found or Wrong File Name")

# =====================================================================================================

