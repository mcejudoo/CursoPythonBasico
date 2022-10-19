
class Time:

    def __init__(self,hh=0,MM=0,ss=0):
        self.hh = hh
        self.MM = MM
        self.ss = ss   
   
    def __str__(self):        
        return '%02d:%02d:%02d' % (self.hh,self.MM,self.ss)

class Date:

    def __init__(self, dd=1,mm=1,yy=1970):
        self.dd = dd
        self.mm = mm
        self.yy = yy

    def __str__(self):
        return "%02d/%02d/%04d" % (self.dd,self.mm,self.yy)

    def esBisiesto(self):
        anyo = self.yy    
        if  (anyo % 4 == 0 and anyo % 100 != 0) or (anyo%100 == 0 and anyo % 400 == 0):
            return True    
        else:
            return False

class DateTime(Time,Date):

    def __init__(self,dd=1,mm=1,yy=1970,HH=0,MM=0,SS=0):
        Date.__init__(self, dd,mm,yy)
        Time.__init__(self,HH,MM,SS)

    def __str__(self):
        return Date.__str__(self)+ " "+Time.__str__(self)

if __name__ == '__main__':
    dt = DateTime(HH=9)
    print(dt)





 

