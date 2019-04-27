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
            print('Air left: ', self.tire, '(LOW AIR LEVEL)')
        else:
            print('Air left: ', self.tire)
    
    def zapravka(self):
        f = random.randint(2, 5)
        print ('You got', f, 'litres!')
        if self.fuel + f >= 100:
            print("Can't refill more, because ", self.fuel, '+', f, ' is equal or more than 100 (100 = full tank)')
            print('---')
            print()
        else:
            print('---')
            print()
            self.fuel += f
        
    def repairing(self):
        print('Tire fixed!')        

    def moneypocket(self):
        p = random.randint(1, 3)
        self.money += p
        print('You found ', p, ' coin(s) ')
        print('Total money:', self.money)
        print('---')

    def rand_money(self):
        m = random.randint(1, 10)
        return m

    def spending(self):
        j = self.rand_money()
        if self.money < j:
            return '1'
        else:
            return '0'

    def gas_spend(self):
        j = self.rand_money()
        self.money -= j
        print()
        print('You spent ', j, ' coins')
        print("Coins left: ", self.money)
        print('---')

    def money_left(self):
        return self.money

    def hud(self):
        if self.fuel <= 30:
            print('- Fuel:', self.fuel," (LOW FUEL LEVEL!)")
        else:
            print('- Fuel:', self.fuel)
        print('- Dist:', self.distance)
