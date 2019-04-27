from Car_specs import *

RED = '\33[31m'
YELLOW = '\33[33m'
END = '\33[0m'
x = int(input("Distance? (optimal - 100) = "))
My_Car = Car(x)
p = 0
w = 0

while My_Car.fuel_left() > 0:
    z = str(input('Press ENTER'))
    print('\n'*15)
    if z == '':
        My_Car.move()
        if My_Car.tire == 0:
            print(RED + 'OUT OF AIR - GAME OVER' + END)
            quit(0)
        if My_Car.fuel_left() <= 0:
            print()
            print(RED + 'OUT OF FUEL = GAME OVER' + END)
            quit(0)
        if My_Car.dist_left() <= 0:
            print(YELLOW + 'End of the road = You won!' + END)
            quit(0)
        gas = random.randint(0, 100)
        mon = random.randint(0, 100)
        ways = random.randint(0, 100)
        broke = random.randint(0, 100)
        if gas <= 20:
            print('!GAS STATION!')
            print('You have:')
            print('- Coins: ', My_Car.money_left())
            My_Car.hud()
            j = str(input('Do you want to spend randomly 1-10 coins for 2-5 liters? Y/N: '))
            j=j.title()
            if j == "Y":
                if My_Car.spending() == '1':
                    print('Not enough money! Moving without refueling!')
                    print('---')
                elif My_Car.spending() == '0':
                    My_Car.gas_spend
                    My_Car.zapravka()
            if p == 1:
                t = str(input('You have a broken tire. Do you want to repair for 5 coins? Y/N: '))
                t=t.title()
                if t == "Y":
                    if My_Car.spending() == '1':
                        print('Not enough money! No repairing!')
                        print('---')
                    else:
                        My_Car.repairing()
                        w = 1
                        p = 0
                else:
                    print('No repairing!')
            if j == "N":
                print()
                print('No refueling!')
                print()
        elif mon <= 7:
            print('Found money!')
            My_Car.moneypocket()
        elif ways <= 4:
            print('The road branches in 2 ways')
            print('The dirty one is faster, but full of dirt (-3 ext fuel)')
            print('There is also clean one but a way longer (+5 distance)')
            q = str(input('Will you use the dirty road? Y/N?: '))
            q=q.title()
            if q == 'Y':
                My_Car.dirty_road()
            else:
                My_Car.clean_road()
        elif broke <= 4:
            if p == 0 and w == 0:
                My_Car.prokol()
                p=1
        print('Moving...')
        My_Car.hud()
        if p == 1:
            My_Car.tire_hp()
    print('↓↓↓↓↓')
