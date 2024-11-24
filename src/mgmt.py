import os
class Mgmt:
    def addEmp(self,e):
        fp = open("data.txt",'a')
        fp.write(str(e))
        fp.close()
    
    def display(self):
        if(os.path.exists("data.txt")):
            fp = open("data.txt",'r')
            # print(fp.read())  # to display all customer
            #to display customer one by one
            for member in fp:
                print(member)
    
    def searchEmp(self,id):
        with open("data.txt",'r') as fp:
            for e in fp:
                try:
                    e.index(str(id),4,7)
                    print("record found")
                    print(e)
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
                        e.index(str(id),4,7)
                        #print(e)
                    except ValueError:
                        records.append(e)
                    else:
                        found = True

            if(found == True):
                with open("data.txt",'w') as fp:
                    for e in records:
                        fp.write(e)
                print("id Deleted")
            else:
                print("record Not Found")
        
        else: 
            print("Invalid ID")