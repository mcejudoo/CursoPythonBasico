class DateTime(Time,Date):

    def __init__(self,dd=1,mm=1,yy=1970,HH=0,MM=0,SS=0):
        Date.__init__(self, dd,mm,yy)
        Time.__init__(self,HH,MM,SS)

    def __str__(self):
        return Date.__str__(self)+ " "+Time.__str__(self)
