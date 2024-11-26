class MemberInfo:
    def __init__(self,id,nm,mealpd,fees_paid):
        self.__id = id
        self.__nm = nm
        self.__fees_paid = fees_paid
        self.__mealPerDay = mealpd
    
    def getid(self):
        return self.__id
    
    def getName(self):
        return self.__nm
    
    def getFeesPaid(self):
        return self.__fees_paid

    def getMeaLPerDay(self):
        return self.__mealPerDay

    def setId(self,id):
        self.__id = id
    
    def setName(self,nm):
        self.__nm = nm
    
    def setFeesPaid(self,fp):
        self.__fees_paid = fp

    def setMealPerDay(self,mp):
        self.__mealPerDay = mp
    
    def __str__(self):
        return str(self.__id)+","+str(self.__nm)+","+str(self.__mealPerDay)+","+str(self.__fees_paid)+"\n"
#testing
if(__name__)=="__main__":
    I = MemberInfo(101,"daya",1,1000)
    print(I)