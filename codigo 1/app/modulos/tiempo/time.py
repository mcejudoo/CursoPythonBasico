class Time:

    def __init__(self,hh=0,MM=0,ss=0):
        self.hh = hh
        self.MM = MM
        self.ss = ss   
   
    def __str__(self):        
        return '%02d:%02d:%02d' % (self.hh,self.MM,self.ss)