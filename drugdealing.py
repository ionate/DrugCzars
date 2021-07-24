# drugdealing.py
# 
import os
import sys
import random
import collections

drugsAvail = ['acid', 'cocaine', 'heroin', 'meth', 'weed']
#drugBasePrices = [5, 100, 60, 25]
#drugPriceModifier = [1, 1, 1, 1]
#drugPrices = list()
citiesAvail = ['boston', 'chicago', 'dallas', 'los angeles', 'new york']

# Enter city
# Get current prices on the street
# Ask if buy or sell?
# Which drug and how many?
# Adjust backpack values (dollars + drugs)

mainMenuOptions = ['[h]elp', '[i]nventory', '[p]rices', '[t]ravel', '[b]uy drugs', '[s]ell drugs', 'e[x]it']
mainMenuAbbr = ['h', 'i', 'p', 't', 'b', 's', 'x']

def percentage(percent, whole):
    return (percent * whole) / 100.0

#subMenu_BuyOptions = ['[]']
'''class EventClass(self):
    drug_events = [
        ('You found some hits of acid in the subway!', 3)
        ('You found some drugs laying on the street corner!', ),
        ('Weed prices hit rock bottom!'),
        ('Drug bust in Columbia! Cocaine is difficult to get and prices have SOARED to new heights!'),
        ('A weak strain of pot has hit the market and is selling CHEAP!'),
        ('You broke the rule- do not get high on your own supply - and consumed X units of Y.'),
        ('There is a heroin shortage in the city.  Prices have skyrocketed.'),
        ('There is an excess of meth in this city and prices are lower than normal.'),
        ('A new type of acid has hit the market and is selling cheap!'),
        ('Word on these streets says heroin is selling CHEAP!'),
        ('The city cracked down on pot growers and there is a shortage. Weed is selling at a premium!'),
        ('Meth is now stronger than ever! Prices have skyrocketed!', ),
        ('A bad supply of cocaine has hit the market and is selling cheap!', -0.6),
        ('Cops chased you!  You lost some dope while running!', -0.04),
        ('You get robbed in the subway! They took most of your stash!', -0.50)
        ]
    def __init__(self):
        super().__init__()

    def GetRandomEvent(self):
        rint = random.randint(0, len(EventClass.drug_events)-1)
        print(f'rint={rint}')
        event = collections.namedtuple('Event',['msg', 'mod'])
        eventmsg = EventClass.drug_events[rint]
        ev = Event(eventmsg, )
'''
class DrugBox:
    def __init__(self):
        super().__init__()
        self.drugs = dict([(drug, 0) for drug in drugsAvail])
        
    def __repr__(self):
        return("Acid=%d, Cocaine=%d, Heroin=%d, Meth=%d, Weed=%d" \
            % (self.drugs['acid'], self.drugs['cocaine'], self.drugs['heroin'],
               self.drugs['meth'] ,self.drugs['weed']))
    
    def __str__(self):
        return("Acid=%d, Cocaine=%d, Heroin=%d, Meth=%d, Weed=%d" \
            % (self.drugs['acid'], self.drugs['cocaine'], self.drugs['heroin'],
               self.drugs['meth'] ,self.drugs['weed']))
        
class Backpack:
    def __init__(self, startingmoney=200):
        super().__init__()
        #self.drugs = DrugBox()
        self.mydrugbox = DrugBox()
        self.mymoney = startingmoney
        
    def __repr__(self):
        return("Backpack contents: Money=%d, \nDrugs=%s" \
            % (self.mymoney, self.mydrugbox))
    
    def __str__(self):
        return("Backpack contents: Money=%d, \nDrugs=%s" \
            % (self.mymoney, self.mydrugbox))

class DrugName:
    acid = ('acid', 0)
    cocaine = ('cocaine', 1)
    heroin = ('heroin', 2)
    meth = ('meth', 3)
    weed = ('weed', 4)

class DrugDealing:
    def __init__(self, backpack, drugdealername):
        super().__init__()
        self.myname = drugdealername
        #self.dollars = startingMoney
        self.backpack = backpack
        self.currentCity = 'boston'
        self.currentDrugPrices = list(zip(drugsAvail,[random.randint(1,8),
                                                      random.randint(100,400),
                                                      random.randint(999,4000),
                                                      random.randint(20,200),
                                                      random.randint(10,40)]))

    def GetCurrentPrice(self, drugname):
        if drugname.lower() == 'acid':
            offset = DrugName.acid[1]
        elif drugname.lower() == 'cocaine':
            offset = DrugName.cocaine[1]
        elif drugname.lower() == 'heroin':
            offset = DrugName.heroin[1]
        elif drugname.lower() == 'meth':
            offset = DrugName.meth[1]
        elif drugname.lower() == 'weed':
            offset = DrugName.weed[1]
        print(f'{drugname} offset={offset}')
        return int(self.currentDrugPrices[offset][1])
    
    def GetAllCurrentPrices(self):
        self.currentDrugPrices = list(zip(drugsAvail,[random.randint(1,5),
                                                      random.randint(40,200),
                                                      random.randint(999,4000),
                                                      random.randint(20,100),
                                                      random.randint(10,40)]))
    
    def PrintCurrentPrices(self):
        print(f'\n--------- Current Pricing -----------')
        print(f'${self.currentDrugPrices[DrugName.acid[1]]}')
        print(f'${self.currentDrugPrices[DrugName.cocaine[1]]}')
        print(f'${self.currentDrugPrices[DrugName.heroin[1]]}')
        print(f'${self.currentDrugPrices[DrugName.meth[1]]}')
        print(f'${self.currentDrugPrices[DrugName.weed[1]]}')
        print(f'-------------------------------------')
    
    def ReduceCurrentPrice(self, drugName):
        randPerc = random.randint(10, 60)
        currentPrice = self.GetCurrentPrice(drugName) ##currentDrugPrices[drugName]
        print(f'(ReducingCurrentPrice: {drugName}')
        print(f'Current=${currentPrice}')
        print(f'Random Perc={randPerc}')
        newVal = float(currentPrice) * (randPerc / 100.0)
        print(f'NEWVAL={newVal}')
        
    def TravelToNewCity(self, newCity=None):
        if newCity == None:
            self.currentCity = citiesAvail[random.randint(0,4)]
        print(f'\nTraveling to {self.currentCity}...')
        self.GetAllCurrentPrices()
 
    def BuyDrugs(self):
        rc = 1
        print(f'\n----------- Buy Drugs --------------')
        drugname = input('Which drug?')
        if drugname.lower() in drugsAvail:
            drugquant = int(input(f'({self.backpack.mydrugbox.drugs[drugname]}) How many?'))
            currprice = self.GetCurrentPrice(drugname.lower())
            mytotalprice = currprice * drugquant
            print(f' Buy {drugquant} of {drugname} at {currprice} dollars per unit (${mytotalprice})?')
            yesorno = str(input('[y]es or [n]o?')).lower()
            if yesorno == 'y':
                if self.backpack.mymoney >= mytotalprice: 
                    self.backpack.mydrugbox.drugs[drugname] += drugquant
                    self.backpack.mymoney -= mytotalprice
                    print(f'Balance now= {self.backpack.mymoney}')
                else:
                    print(f'You do not have enough money!')
                # END IF
                print(f'-------------------------------------')            
                rc = 0
            else:
                rc = 0
            # END IF
        else:
            print(f'Unknown drug!')
            rc = 0
        return rc

    def SellDrugs(self):
        rc = 1
        print(f'\n----------- Sell Drugs --------------')
        drugname = input('Which drug?')
        if drugname.lower() in drugsAvail:
            drugquant = int(input(f'({self.backpack.mydrugbox.drugs[drugname]}) How many?'))
            currprice = self.GetCurrentPrice(drugname.lower())
            mytotalprice = currprice * drugquant
            if self.backpack.mydrugbox.drugs[drugname] >= drugquant:
                print(f' Sell {drugquant} of {drugname} at {currprice} dollars per unit (${mytotalprice})?')
                yesorno = str(input('[y]es or [n]o?')).lower()
                if yesorno == 'y':
                    self.backpack.mydrugbox.drugs[drugname] -= drugquant
                    self.backpack.mymoney += mytotalprice
                    rc = 0
                else:
                    rc = 0
                # END IF
            else:
                print(f'You do not have enough to sell {drugquant}!')
            # END IF
        else:
            print(f'Unknown drug!')
        # END IF
        return rc
    
if __name__ == "__main__":
    print('\n==================================')
    print(f'    DrugDealing [v0.0.1]           ')
    print('==================================')
    
    bp = Backpack(200)
    ddMain = DrugDealing(bp, 'Lefty')
    ddMain.PrintCurrentPrices()

    process = True
    ####  MAIN PROCE SSING LOOP #####
    while process == True:
        print(f'\n(Wallet: ${bp.mymoney})')
        reply = str(input(mainMenuAbbr)).lower()
        if reply in mainMenuAbbr:
            if reply == "x":
                print(f'Bye!')
                break
                        
            elif reply == "h":
                ## HELP ##
                print(mainMenuOptions)
        
            elif reply == "t":
                ## TRAVEL ##
                ddMain.TravelToNewCity()
                ddMain.ReduceCurrentPrice('cocaine')
                ddMain.PrintCurrentPrices()
                
            elif reply == "p":
                ## PRICES ##
                ddMain.PrintCurrentPrices()
                
            elif reply == "i":
                ## INVENTORY ##
                print(f'\n----------- Inventory ------------')
                print(f'Drug Dealer: {ddMain.myname}')
                print(f'Total Cash: ${ddMain.backpack.mymoney}')
                print(f'Drugs: {bp.mydrugbox}')
                print(f'\n----------------------------------')
            
            elif reply == "b":
                ## BUY ##
                rc = ddMain.BuyDrugs()
            
            elif reply == "s":
                ## SELL ##
                rc = ddMain.SellDrugs()
            else:
                ## UNKNOWN ##
                print(f'Try again!')
            # END IF
        else:
            print(f'Unknown option!')
        # END IF
    # END WHILE