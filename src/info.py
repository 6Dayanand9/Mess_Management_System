class MemberInfo:
    def __init__(self,id,nm,mealpm,total_fees,fees_paid,fees_remaining,phoneno):
        self.__id = id
        self.__nm = nm
        self.__fees_paid = fees_paid
        self.__mealPerMonth = mealpm
        self.__total_fees = total_fees
        self.__remaining_fees = fees_remaining
        self.__PhoneNo = phoneno
    
    def getid(self):
        return self.__id
    
    def getName(self):
        return self.__nm
    
    def getFeesPaid(self):
        return self.__fees_paid
    
    def getPhoneno(self):
        return self.__PhoneNo

    def getMeaLPerMonth(self):
        return self.__mealPerMonth

    def getTotalFees(self):
        return self.__total_fees

    def getRemainingFees(self):
        return self.__remaining_fees

    def setId(self,id):
        self.__id = id
    
    def setName(self,nm):
        self.__nm = nm
    
    def setFeesPaid(self,fp):
        self.__fees_paid = fp

    def setMealPerMonth(self,mp):
        self.__mealPerMonth = mp
    
    def setTotalFees(self,tf):
        self.__total_fees = tf
    
    def setRemainingFees(self,rf):
        self.__remaining_fees =rf
    
    def SetPhoneno(self,ph):
        self.__PhoneNo = ph
    
    def __str__(self):
        return str(self.__id)+","+str(self.__nm)+","+str(self.__mealPerMonth)+","+str(self.__total_fees)+","+str(self.__fees_paid)+","+str(self.__remaining_fees)+","+str(self.__PhoneNo)+"\n"
#testing
if(__name__)=="__main__":
    I = MemberInfo(101,"daya",30,)
    print(I)