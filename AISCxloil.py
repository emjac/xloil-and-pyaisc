import xloil as xlo

import pandas as pd

df = pd.read_csv("AISC_Database_V15_1.csv")
df.index=df.iloc[:,2]

class Shape:
    def __init__(self,name):
        self.name = name
        self.aisctype = df.loc[name,"Type"]
        self.A = df.loc[name,"A"]
        self.d = df.loc[name,"d"]
        self.ddet = df.loc[name,"ddet"]
        self.tw = df.loc[name,"tw"]
        self.twdet = df.loc[name,"twdet"]
        self.bf = df.loc[name,"bf"]
        self.bfdet = df.loc[name,"bfdet"]
        self.tf = df.loc[name,"tf"]
        self.tfdet = df.loc[name,"tfdet"]
        self.kdes = df.loc[name,"kdes"]
        self.kdet = df.loc[name,"kdet"]
        self.k1 = df.loc[name,"k1"]
        self.T = df.loc[name,"T"]
        self.Wt = df.loc[name,"W"]
        self.Ix = df.loc[name,"Ix"]
        self.Sx = df.loc[name,"Sx"]
        self.rx = df.loc[name,"rx"]
        self.Zx = df.loc[name,"Zx"]
        self.Iy = df.loc[name,"Iy"]
        self.Sy = df.loc[name,"Sy"]
        self.ry = df.loc[name,"ry"]
        self.Zy = df.loc[name,"Zy"]
        self.rts = df.loc[name,"rts"]
        self.ho = df.loc[name,"ho"]
        self.J = df.loc[name,"J"]
        self.Cw = df.loc[name,"Cw"]


@xlo.func
def shape(name):
    return Shape(name)
    
@xlo.func
def A(Shape):
    return Shape.A
    
@xlo.func
def AISCType(Shape):
    return Shape.aisctype
    
@xlo.func
def ddet(Shape):
    return Shape.ddet
    
@xlo.func
def tw(Shape):
    return Shape.tw   

@xlo.func
def twdet(Shape):
    return Shape.twdet
    
@xlo.func
def bf(Shape):
    return Shape.bf
    
@xlo.func
def bfdet(Shape):
    return Shape.bfdet

@xlo.func
def tf(Shape):
    return Shape.tf

@xlo.func
def tfdet(Shape):
    return Shape.tfdet
    
@xlo.func
def kdes(Shape):
    return Shape.kdes

@xlo.func
def kdet(Shape):
    return Shape.kdet   

#@xlo.func
#def k1(Shape):
#    return Shape.k1   

@xlo.func
def T(Shape):
    return Shape.T   

@xlo.func
def Wt(Shape):
    return Shape.Wt  

@xlo.func
def Ix(Shape):
    return Shape.Ix  

@xlo.func
def Sx(Shape):
    return Shape.Sx   

@xlo.func
def rx(Shape):
    return Shape.rx   

@xlo.func
def Zx(Shape):
    return Shape.Zx  

@xlo.func
def Iy(Shape):
    return Shape.Iy  

@xlo.func
def Sy(Shape):
    return Shape.Sy   

@xlo.func
def ry(Shape):
    return Shape.ry   

@xlo.func
def Zy(Shape):
    return Shape.Zy    

@xlo.func
def rts(Shape):
    return Shape.rts  

@xlo.func
def ho(Shape):
    return Shape.ho   

@xlo.func
def J(Shape):
    return Shape.J   

@xlo.func
def Cw(Shape):
    return Shape.Cw    
    
@xlo.func
def get_prop(Shape,attribute):
    if attribute == "A":
        return Shape.A 
    elif attribute == "Type":
        return Shape.aisctype
    elif attribute == "d":
        return Shape.d
    elif attribute == "ddet":
        return Shape.ddet
    elif attribute == "tw":
        return Shape.tw   
    elif attribute == "twdet":
        return Shape.twdet
    elif attribute == "bf":
        return Shape.bf
    elif attribute == "bfdet":
        return Shape.bfdet
    elif attribute == "tf":
        return Shape.tf
    elif attribute == "tfdet":
        return Shape.tfdet
    elif attribute == "kdes":
        return Shape.kdes
    elif attribute == "kdet":
        return Shape.kdet    
    elif attribute == "T":
        return Shape.T   
    elif attribute == "Wt":
        return Shape.Wt  
    elif attribute == "Ix":
        return Shape.Ix  
    elif attribute == "Sx":
        return Shape.Sx   
    elif attribute == "rx":
        return Shape.rx   
    elif attribute == "Zx":
        return Shape.Zx  
    elif attribute == "Iy":
        return Shape.Iy  
    elif attribute == "Sy":
        return Shape.Sy   
    elif attribute == "ry":
        return Shape.ry   
    elif attribute == "Zy":
        return Shape.Zy    
    elif attribute == "rts":
        return Shape.rts  
    elif attribute == "ho":
        return Shape.ho   
    elif attribute == "J":
        return Shape.J   
    elif attribute == "Cw":
        return Shape.Cw
    else:
        return False

    