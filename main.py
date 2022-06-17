import logging
import random
from smtplib import quoteaddr


class Animal:
    def __init__(self):
        self.animal_class = 'Animal class'
        self.species = 'Species'
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
            f'Species = {self.species}\n'
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
        print(f'{self.species} has a total score of {score}')

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

    def sound_off(self):
        print('Animal Noise\n')

class Bear(Animal):
    def __init__(self):
        self.animal_class = 'Mammalia'
        self.species = 'Grizzly bear'
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
        self.species = 'Silverback Gorilla'
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
        self.species = 'Human'
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
        self.death_count = 0

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
            f'{self.contender1.species} has entered the arena.\n'
            f'{self.contender2.species} has entered the arena.'
        )

        print(entrance)

    def hype_session(self):
        red = (
            f'In the red corner...\n'
            f'Weighting in at {self.contender1.weight} pounds.\n'
            f'Hailing from {self.contender1.origin}\n'
            f'{self.contender1.hype_name} the {self.contender1.species}\n'
        )
        blue = (
            f'In the blue corner...\n'  
            f'Weighting in at {self.contender2.weight} pounds.\n'
            f'All the way from {self.contender2.origin}\n'
            f'{self.contender2.hype_name} the {self.contender2.species}\n'
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

def create_new_contender():
    custom_contender = Animal()
    contender_data = {
        'object' : custom_contender,
        'Animal class' : '',
        'Species' : '',
        'Scientific name' : '',
        'Hype name' :'',
        'Origin' : '',
        'Health' : 0,
        'Speed' : 0,
        'Attacks' : 0,
        'Defense' : 0,
        'Weight' : 0,
        'Intelligence' : 0,
    }


    for data in contender_data:
        while True:            
            match data:
                case 'object':
                    break
                case 'Animal class':
                    try:
                        response = str(input(f'Set {data}:'))
                        contender_data[data] = response
                        custom_contender.animal_class = response
                    except ValueError:
                        print("Unaccaptable response. Enter valid value.")
                        continue
                    else:
                        break
                case 'Species':
                    try:
                        response = str(input(f'Set {data}:'))
                        contender_data[data] = response
                        custom_contender.species = response
                    except ValueError:
                        print("Unaccaptable response. Enter valid value.")
                        continue
                    else:
                        break                    
                case 'Scientific name':
                    try:
                        response = str(input(f'Set {data}:'))
                        contender_data[data] = response
                        custom_contender.scientific_name = response
                    except ValueError:
                        print("Unaccaptable response. Enter valid value.")
                        continue
                    else:
                        break                    
                case 'Hype name':
                    try:
                        response = str(input(f'Set {data}:'))
                        contender_data[data] = response
                        custom_contender.hype_name = response
                    except ValueError:
                        print("Unaccaptable response. Enter valid value.")
                        continue
                    else:
                        break                                   
                case 'Origin':
                    try:
                        response = str(input(f'Set {data}:'))
                        contender_data[data] = response
                        custom_contender.origin = response
                    except ValueError:
                        print("Unaccaptable response. Enter valid value.")
                        continue
                    else:
                        break                    
                case 'Health':
                    try:
                        response = int(input(f'Set {data}:'))
                        contender_data[data] = response
                        custom_contender.health = response
                    except ValueError:
                        print("Unaccaptable response. Enter valid value.")
                        continue
                    else:
                        break                          
                case 'Speed':
                    try:
                        response = int(input(f'Set {data}:'))
                        contender_data[data] = response
                        custom_contender.speed = response
                    except ValueError:
                        print("Unaccaptable response. Enter valid value.")
                        continue
                    else:
                        break                         
                case 'Attacks':
                    try:
                        response = int(input(f'Set {data}:'))
                        contender_data[data] = response
                        custom_contender.attacks = response
                    except ValueError:
                        print("Unaccaptable response. Enter valid value.")
                        continue
                    else:
                        break                         
                case 'Defense':
                    try:
                        response = int(input(f'Set {data}:'))
                        contender_data[data] = response
                        custom_contender.defense = response
                    except ValueError:
                        print("Unaccaptable response. Enter valid value.")
                        continue
                    else:
                        break    
                case 'Weight':
                    try:
                        response = int(input(f'Set {data}:'))
                        contender_data[data] = response
                        custom_contender.weight = response
                    except ValueError:
                        print("Unaccaptable response. Enter valid value.")
                        continue
                    else:
                        break                                                                                                                                                                                                          
                case 'Intelligence':
                    try:
                        response = int(input(f'Set {data}:'))
                        contender_data[data] = response
                        custom_contender.intelligence = response
                    except ValueError:
                        print("Unaccaptable response. Enter valid value.")
                        continue
                    else:
                        break 
                case _:
                    print('Unknown error occured.')
                   
    return contender_data

def create_match():
    response = input('What type of match? Custom, default, hybrid?')
    response = response.lower()

    match response:
        case 'custom':
            print('custom contender vs custom contender')
            contender1 = create_new_contender()
            contender2 = create_new_contender()
        case 'default':
            print('bear vs gorilla')
            contender1 = {'object': Bear()}
            contender2 = {'object': Gorilla()}
        case 'hybrid':
            print('bear/gorilla vs custom contender')
            bear_v_gorilla = input('Bear or Gorilla?')
            if bear_v_gorilla.lower() == 'bear':
                contender1 = {'object': Bear()}
                contender2 = create_new_contender()
            elif bear_v_gorilla.lower == 'gorilla':
                contender1 = {'object': Gorilla()}
                contender2 = create_new_contender()
            else:
                print('Unknown contender choice')
        case _:
            print('Unknown case')

    matches = input('How many matches would you like to simulate?')

    return contender1 ,contender2, matches

def reset_contenders(contender1_dict, contender2_dict):
    if contender1_dict['object'].species.lower() == 'grizzly bear' and contender2_dict['object'].species.lower() == 'silverback gorilla':
        print('if')
        contender1_dict['object'].__init__()
        contender2_dict['object'].__init__()
    elif contender1_dict['object'].species.lower() == 'grizzly bear' or contender1_dict['object'].species.lower() == 'grizzly bear':
        print('elif')
        contender1_dict['object'].__init__()
        contender2_dict['object'].animal_class = contender2_dict['Animal class']
        contender2_dict['object'].species = contender2_dict['Species']
        contender2_dict['object'].scientific_name = contender2_dict['Scientific name']
        contender2_dict['object'].hype_name = contender2_dict['Hype name']
        contender2_dict['object'].origin = contender2_dict['Origin']
        contender2_dict['object'].health = contender2_dict['Health']
        contender2_dict['object'].speed = contender2_dict['Speed']
        contender2_dict['object'].attacks = contender2_dict['Attacks']
        contender2_dict['object'].defense = contender2_dict['Defense']
        contender2_dict['object'].weight = contender2_dict['Weight']
        contender2_dict['object'].intelligence = contender2_dict['Intelligence']
    else:
        print('else')
        contender1_dict['object'].animal_class = contender1_dict['Animal class']
        contender1_dict['object'].species = contender1_dict['Species']
        contender1_dict['object'].scientific_name = contender1_dict['Scientific name']
        contender1_dict['object'].hype_name = contender1_dict['Hype name']
        contender1_dict['object'].origin = contender1_dict['Origin']
        contender1_dict['object'].health = contender1_dict['Health']
        contender1_dict['object'].speed = contender1_dict['Speed']
        contender1_dict['object'].attacks = contender1_dict['Attacks']
        contender1_dict['object'].defense = contender1_dict['Defense']
        contender1_dict['object'].weight = contender1_dict['Weight']
        contender1_dict['object'].intelligence = contender1_dict['Intelligence']

        contender2_dict['object'].animal_class = contender2_dict['Animal class']
        contender2_dict['object'].species = contender2_dict['Species']
        contender2_dict['object'].scientific_name = contender2_dict['Scientific name']
        contender2_dict['object'].hype_name = contender2_dict['Hype name']
        contender2_dict['object'].origin = contender2_dict['Origin']
        contender2_dict['object'].health = contender2_dict['Health']
        contender2_dict['object'].speed = contender2_dict['Speed']
        contender2_dict['object'].attacks = contender2_dict['Attacks']
        contender2_dict['object'].defense = contender2_dict['Defense']
        contender2_dict['object'].weight = contender2_dict['Weight']
        contender2_dict['object'].intelligence = contender2_dict['Intelligence']


def initiate_battle():
    print('battle begins')

if __name__ == "__main__":

    contender1_dict, contender2_dict, matches = create_match()
    contender1, contender2 = contender1_dict['object'], contender2_dict['object']

    # matches = 0
    # while(int(matches) < 1):
    #     matches = input('How many matches would you like to simulate?')
    #     if int(matches) != type(int):
    #         continue
    #     else:
    #         break

    logging.basicConfig(filename="std3.csv", 
					format='%(asctime)s %(message)s', 
					filemode='w') 
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    for i in range(int(matches)):


        arena = Arena(contender1,contender2)

        arena.enter_arena()
        arena.hype_session()

        arena.referee.rules()
        arena.referee.sound_off()

        contenders = [contender1.species, contender2.species]

        while(contender1.health > 0 and contender2.health > 0):
            attacker = battle_sequence(contenders)
            if attacker == contender1.species:
                damage = contender1.attack()
                contender2.health -= damage       
                contender1.attack_count += 1     
                print(f'{contender1.hype_name} attacks for {damage} damage!')
                if contender2.health <= 0:
                    print(f'{contender2.hype_name} has been knocked out!!!\n')
                    winner = contender1
                    break
                else:
                    print(f'{contender2.hype_name} is at {contender2.health} health\n')
            elif attacker == contender2.species:
                damage = contender2.attack()
                contender1.health -= damage
                contender2.attack_count += 1
                print(f'{contender2.hype_name} attacks for {damage} damage!')
                if contender1.health <= 0:
                    print(f'{contender1.hype_name} has been knocked out!!!\n')
                    winner = contender2
                    break
                else:
                    print(f'{contender1.hype_name} is at {contender1.health} health.\n')
            else:
                print('idk') 


        if winner.attack_count > 19:
            print(f'{winner.hype_name} the {winner.scientific_name} has gone on a killing spree!!!')
            arena.referee.death_count += 1
            while(arena.referee.health > 0):
                damage = winner.attack()
                arena.referee.health -= damage
                print(f'{winner.hype_name} attacks {arena.referee.hype_name} for {damage} damage!')
                if arena.referee.health <= 0:
                    print(f'{arena.referee.hype_name} has been completely shredded to bits by {winner.hype_name}')

        print(f'{winner.hype_name} has been declared the Undisputed Champion of the World!!!')
        winner.sound_off()
        logger.debug(f',{winner.species}, {arena.referee.death_count}')
        reset_contenders(contender1_dict, contender2_dict)

