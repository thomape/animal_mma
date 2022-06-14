import logging
import random


class Animal:
    def __init__(self):
        self.animal_class = 'Animal class'
        self.name = 'Common name'
        self.scientific_name = 'Latin name'
        self.hype_name = 'Hype name'
        self.origin = 'Origin'
        self.health = 100
        self.speed = 100
        self.attacks = 100
        self.defense = 100
        self.weight = 100
        self.intelligence = 100
        self.attack_count = 0

    def show_stats(self):
        stats = (
            f'Class = {self.animal_class}\n'
            f'Common name = {self.name}\n'
            f'Scientific name = {self.scientific_name}\n'
            f'Hype name = {self.hype_name}\n'
            f'Country of origin = {self.origin}\n'
            f'Health = {self.health}\n'
            f'Speed = {self.speed}\n'
            f'Attack = {self.attacks}\n'
            f'Defense = {self.defense}\n'
            f'Weight = {self.weight}\n'
            f'Intelligence = {self.intelligence}'
        )
        print(stats)

    def total_score(self):
        score = self.health + self.speed + self.attacks + self.defense + self.weight + self.intelligence
        print(f'{self.name} has a total score of {score}')

    def attack(self):
        attack_mode = random.randint(0,5)
        match attack_mode:
            case 0:
                return 0
            case 1:
                return 100
            case 2:
                return 200
            case 3:
                return 300
            case 4:
                return 400
            case 5:
                return 1000
            case _:
                print('No attack found')

    def defend(self):
        print('defend')

    def flee(self):
        print('flee')

class Bear(Animal):
    def __init__(self):
        self.animal_class = 'Mammalia'
        self.name = 'Grizzly bear'
        self.hype_name = 'Smokey'
        self.scientific_name = 'Ursus arctos horribillis'
        self.origin = 'The United States of America'
        self.health = 5000
        self.speed = 300
        self.attacks = 1000
        self.defense = 500
        self.weight = 600
        self.intelligence = 200
        self.attack_count = 0

    def sound_off(self):
        print('Grooooooowlllll\n')

class Gorilla(Animal):
    def __init__(self):
        self.animal_class = 'Mammalia'
        self.name = 'Silverback Gorilla'
        self.scientific_name = 'Gorilla beringei'
        self.hype_name = 'Harambe'
        self.origin = 'The Democratic Republic of the Congo'
        self.health = 5000
        self.speed = 500
        self.attacks = 700
        self.defense = 400
        self.weight = 440
        self.intelligence = 800
        self.attack_count = 0

    def sound_off(self):
        print('Roooooooarrrrrrr\n')




class Referee(Animal):
    def __init__(self):
        self.animal_class = 'Mammalia'
        self.name = 'Human'
        self.scientific_name = 'Homosapian'
        self.hype_name = 'Jeff'
        self.origin = 'Canada'
        self.health = 200
        self.speed = 10
        self.attacks = 20
        self.defense = 20
        self.weight = 180
        self.intelligence = 3000
        self.attack_count = 0

    def sound_off(self):
        print('Fight!\n') 
    
    def rules(self):
        rules = (
            f'Alright, I want a good fight.\n'
            f'No-holds-barred.\n'
            f'Protect yourself at all times. Follow my commands at all times.\n'
            f'Red corner ready?...Blue corner ready?...\n'
        )
        print(rules)

class Arena():
    def __init__(self, contender1, contender2):
        self.width = 50
        self.length = 50
        self.contender1 = contender1
        self.contender2 = contender2
        self.referee = Referee()

    def enter_arena(self):
        entrance = (
            f'{self.contender1.name} has entered the arena.\n'
            f'{self.contender2.name} has entered the arena.'
        )

        print(entrance)

    def hype_session(self):
        red = (
            f'In the red corner...\n'
            f'Weighting in at {self.contender1.weight} pounds.\n'
            f'Hailing from {self.contender1.origin}\n'
            f'{self.contender1.hype_name} the {self.contender1.name}\n'
        )
        blue = (
            f'In the blue corner...\n'  
            f'Weighting in at {self.contender2.weight} pounds.\n'
            f'All the way from {self.contender2.origin}\n'
            f'{self.contender2.hype_name} the {self.contender2.name}\n'
        )

        reffing = (
            f'Refereeing this epic bout is {self.referee.hype_name}.\n'
        )

        print(red)
        self.contender1.sound_off()
        print(blue)
        self.contender2.sound_off()
        print(reffing)





# Agnatha (jaw-less fish)
# Chrondrichtyes (cartilaginous fish)
# Osteichthyes (bony fish)
# Amphibia (amphibians)
# Reptilia (reptiles)
# Aves (birds)
# Mammalia (mammals)

def battle_sequence(contenders):
    return random.choice(contenders)


if __name__ == "__main__":

    matches = 0
    while(int(matches) < 1):
        matches = input('How many matches would you like to simulate?')
        if int(matches) != type(int):
            continue
        else:
            break

    logging.basicConfig(filename="std.csv", 
					format='%(asctime)s %(message)s', 
					filemode='w') 
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    for i in range(int(matches)):
        bear = Bear()
        gorilla = Gorilla()

        arena = Arena(gorilla, bear)

        arena.enter_arena()
        arena.hype_session()

        arena.referee.rules()
        arena.referee.sound_off()

        contenders = [bear.name, gorilla.name]

        while(bear.health > 0 and gorilla.health > 0):
            attacker = battle_sequence(contenders)
            if attacker == bear.name:
                damage = bear.attack()
                gorilla.health -= damage       
                bear.attack_count += 1     
                print(f'{bear.hype_name} attacks for {damage} damage!')
                if gorilla.health <= 0:
                    print(f'{gorilla.hype_name} has been knocked out!!!\n')
                    winner = bear
                    break
                else:
                    print(f'{gorilla.hype_name} is at {gorilla.health} health\n')
            elif attacker == gorilla.name:
                damage = gorilla.attack()
                bear.health -= damage
                gorilla.attack_count += 1
                print(f'{gorilla.hype_name} attacks for {damage} damage!')
                if bear.health <= 0:
                    print(f'{bear.hype_name} has been knocked out!!!\n')
                    winner = gorilla
                    break
                else:
                    print(f'{bear.hype_name} is at {bear.health} health.\n')
            else:
                print('idk') 


        print(f'{winner.hype_name} has been declared the Undisputed Champion of the World!!!')
        winner.sound_off()
        logger.debug(f',{winner.name}')
        if winner.attack_count > 19:
            print(f'{winner.hype_name} the {winner.scientific_name} has gone on a killing spree!!!')
            while(arena.referee.health > 0):
                damage = winner.attack()
                arena.referee.health -= damage
                print(f'{winner.hype_name} attacks {arena.referee.hype_name} for {damage} damage!')
                if arena.referee.health <= 0:
                    print(f'{arena.referee.hype_name} has been completely shredded to bits by {winner.hype_name}')

