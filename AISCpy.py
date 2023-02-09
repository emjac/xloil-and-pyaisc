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
        self.Wt = df.loc[name,"Wt"]
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