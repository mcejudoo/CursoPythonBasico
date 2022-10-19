class Date:

    def __init__(self, dd=1,mm=1,yy=1970):
        self.__dd = dd
        self.__mm = mm
        self.__yy = yy

    def __str__(self):
        return "%02d/%02d/%04d" % (self.__dd,self.__mm,self.__yy)

    def esBisiesto(self):
        anyo = self.__yy    
        if  (anyo % 4 == 0 and anyo % 100 != 0) or (anyo%100 == 0 and anyo % 400 == 0):
            return True    
        else:
            return False
