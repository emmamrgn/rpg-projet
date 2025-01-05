from termcolor import colored

class Stats:
    def __init__(self, ATQ, DEF, VIT, PVMAX, PV):
        self.ATQ = ATQ
        self.DEF = DEF
        self.VIT = VIT
        self.PVMAX = PVMAX
        self.PV = PV

    def afficher_PV(self) :
        if (self.PVMAX * 0.75 <= self.PV <= self.PVMAX):
            print("\t PV :", colored(self.PV, "green"),"/", self.PVMAX)
        if (self.PVMAX * 0.25 <= self.PV <= self.PVMAX * 0.75):
            print("\t PV :", colored(self.PV, "yellow"),"/", self.PVMAX)
        if (self.PVMAX * 0 <= self.PV <= self.PVMAX * 0.25):
            print("\t PV :", colored(self.PV, "red"),"/", self.PVMAX)

    def afficher_stats(self):
        print(f"\t Attaque :", colored(self.ATQ,"green"))
        print(f"\t Défense :", colored(self.DEF, "green"))
        print(f"\t Vitesse :", colored(self.VIT, "green"))
        self.afficher_PV()