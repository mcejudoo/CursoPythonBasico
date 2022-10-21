#-*- coding: cp1252 -*-
# Unión, intersección, mezcla de listas:


def union(L1, L2):
        """
        >>> L1=[1,2,3,4,5]
        >>> L2 = [1,2,6,7]
        >>> union(L1,L2)
        [1,2,3,4,5,60,7]
        """
        LU = []

        for i in L1:
                if i not in LU:
                        LU.append(i)
        for j in L2:
                if j not in LU:
                        LU.append(j)
        LU.sort()
        return LU

def interseccion(L1, L2):
        """
        >>> L1 = [2,3]
        >>> L2 = [12,3,4,6]
        >>> interseccion(L1,L2)
        [12,3]
        """        
        LI = []
        for i in L1:
                if i in L2 and i not in LI:
                        LI.append(i)

        LI.sort()                
        return LI

def unionALL(L1,L2):
        L = L1+L2
        L.sort()
        return L
        
def _test():
        import doctest
        doctest.testmod()

if __name__ == "__main__":
        _test()


