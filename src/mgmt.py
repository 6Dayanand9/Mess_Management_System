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