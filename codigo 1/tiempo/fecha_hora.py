



import date, times

class DateTime(date.Date,times.Time):

    def __init__(self,dd=1,mm=1,yy=1970,HH=0,MM=0,SS=0):
        date.Date.__init__(self, dd,mm,yy)
        times.Time.__init__(self,HH,MM,SS)

    def __str__(self):
        return date.Date.__str__(self)+ " "+times.Time.__str__(self)

class Crono(times.Time):
    pass

class Era(times.Time):
    pass

if __name__ == '__main__':
    dt = DateTime(HH=9)
    print(dt)
    print(isinstance(dt,times.Time))
    print(issubclass(DateTime,date.Date))
    print(times.Time.__subclasses__())





 

