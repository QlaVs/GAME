
import random
class Car:
    def __init__(self, distance):
        self.fuel = 100
        self.distance = distance
        self.money = 35
        self.tire = 21

    def fuel_left(self):
        return self.fuel

    def dist_left(self):
        dlft = self.distance
        return dlft

    def move(self):
        self.distance -= 2
        self.fuel -= 3

    def prokol(self):
        print('!!!!!!!!!')
        print('You broke your tier!!')
        print('You have 20 hp for you tire and it spends every move')
        print('You can repair it in gas station for 5 coins')
        print('If air ends - you lose')
        print('New HUD: "Air left:" ')

    def dirty_road(self):
        print('---')
        print('You stuck in a dirt, so you spend more fuel to get out of it')
        self.fuel -= 6
        
    def clean_road(self):
        print('---')
        print('The clean road was the way longer')
        self.distance += 5
        self.fuel -= 3
        
    def tire_hp(self):
        self.tire -= 1
        if self.tire <= 8:
            print('Air left: ', self.tire, RED + '(LOW AIR LEVEL)'  + END)
        else:
            print('Air left: ', self.tire)
    
    def zapravka(self):
        f = random.randint(2, 5)
        print()
        print ('You got', f, 'litres!')
        if self.fuel + f >= 100:
            print("Can't refill more, because ", self.fuel, '+', f, ' is more than 100 (more then full tank)')
            print()
        else:
            print('---')
            self.fuel += f
        
    def repairing(self):
        print('Tire fixed!')        

    def moneypocket(self):
        p = random.randint(1, 3)
        self.money += p
        print('You found ', p, ' coins ')
        print('Total money:', self.money)
        print('---')

    def spending(self):
        m = random.randint(1, 10)
        if self.money < m:
            return '1'
        else:
            return '0'
    def gas_spend(self):
        self.money -= m
        print('You spent ', m, ' coins')
        print("Coins left: ", self.money)
        print('---')

    def money_left(self):
        return self.money

    def hud(self):
        if self.fuel <= 30:
            CREDBG = '\33[31m'
            CEND = '\033[0m'
            print('- Fuel: ', self.fuel, (CREDBG + "(!LOW FUEL LEVEL!)" + CEND))
        else:
            print('- Fuel: ', self.fuel)
        print('- Dist: ', self.distance)