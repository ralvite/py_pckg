class Tree():
    """
    class defining a tree
    Paramenters:
    d: diameter (m)
    h: height (m). Default value = 10 m
    vol: volume (m3)
    """
    def __init__(self,d,h=10):
        self.d = d
        self.h = h
    def calc_vol(self):
        """
        Calculate de tree volume
        """
        self.vol = self.d * self.h
        return self.vol

class Caducif(Tree):
    """
    Inherit the class 'Tree' and
    set a new method called 'calc_vol_copa'
    on the inherited method 'calc_vol'
    """
    def __init__(self,d,h=10):
        Tree.__init__(self, d, h)
    def calc_vol_copa(self):
        self.vol_copa = float (Tree.calc_vol(self) ) * float(0.33)
        return self.vol_copa