from random import randint


class Creature:
    def __init__(self, name: str, creature_type: str, quests=None):
        self.name = name
        self.creature_type = creature_type
        self.quests = quests or []
        self.health = randint(50, 149)

    def get_creature_type(self):
        return self.creature_type

    def add_quest(self, quest_name: str, status='incomplete'): # 4 marks
        for quest in self.quests:
            if quest['quest'] == quest_name:
                print(f'Quest {quest_name} already exists')
                return
        self.quests.append({'quest': quest_name, 'status':status})
        self.health += 5
        print(f'The quest {quest_name} has been added to {self.name}. They have a health status of {self.health}')

    def list_quests(self):
        print(f'{self.name} quests:')
        for quest in self.quests:
                print(f"{quest['quest']} -> {quest['status']}")

    def attack(self, other: "Creature"):
        print(f"{self.name} attacks {other.name}!")
        other.take_damage(self.health // 2)

    def take_damage(self, amount: int): # 3 marks
        self.health -= amount
        print(f'{self.name} take {amount} damage. Health now {self.health}')
        if self.health <= 0:
            print(f'The creature has been defeated.')

    def heal(self, amount: int): # 1 mark
        self.health += amount
        print(f'{self.name} heals for {amount}. Health now {self.health}')


class Fairy(Creature):
    def __init__(self, name: str):
        super().__init__(name,  creature_type='Fairy')

    def boost_dust(self, amount: int):
        self.health += amount
        print(f'{self.name}, gets a dose of fairy dust, this boosts their health to {self.health}')


class Realm:
    def __init__(self, name):
        self.name = name
        self.creatures = {}

    def add_creature(self, creature: Creature):  # 1 mark
        self.creatures[creature.name] = creature

    def list_creatures(self): # 2 marks
        for name, creature in self.creatures.items():
            print(name, creature.creature_type)



class RealmsRegistry:
    def __init__(self):
        self.mountains = Realm("Crimson Mountains")
        self.woods = Realm("Whispering Woods")
        self.realms = {}

    def add_realm(self, realm: Realm):
        self.realms[realm.name] = realm

    def setup_realms(self): # 2 marks
        print(f'Setting up all creatures in the realms and adding quests.....')
        blorg = Creature("Blorg", "Goblin")
        draven = Creature("Draven", "Elf")
        mira = Creature("Mira", "Witch")

        elara = Fairy("Elara")


        """
        - Code to add a quest to each Creature object is to be inserted here
        - You can assume that all creature names are unique
        creature:   quest:
        elara       Gather moonlight crystals
        blorg       Steal the wizard’s hat
        draven      Defend the dark forest
        mira        Brew potion of power
        """

        elara.add_quest('Gather moonlight crystals')
        blorg.add_quest('Steal the wizard\'s hat')
        draven.add_quest('Defend the dark forest')
        mira.add_quest('Brew potion of power')

        self.mountains.add_creature(elara)
        self.mountains.add_creature(blorg)

        self.woods.add_creature(draven)
        self.woods.add_creature(mira)

        self.add_realm(self.mountains)
        self.add_realm(self.woods)

    def list_all_realms(self):
        print("All Realms and Their Creatures")
        for realm_name, realm_obj in self.realms.items():
            if isinstance(realm_obj, Realm):
                print(f"\nRealm: {realm_obj.name}")
                realm_obj.list_creatures()

    def find_creature(self, creature_name: str): # 5 marks
        found_creature = False

        for realm in self.all_realms:
            for name, creature in realm.creatures.items():
                if name == creature_name:
                    found_creature = creature
                    found_realm = realm
                    break
            if found_creature:
                break

        if not found_creature:
            return None
        else:
            return found_creature, found_realm

    @property
    def all_realms(self):
        return [self.mountains, self.woods]


class BattleArena:
    def __init__(self, location: str):
        self.location = location

    def start_battle(self, c1: Creature, c2: Creature): # 8 marks
        print(f'The battle begins between {c1.name} and {c2.name}!\n')
        while c1.health > 0 or c2.health > 0:
            c1.attack(c2)
            if c2.health <= 0:
                break
            c2.attack(c1)
            if c1.health <= 0:
                break
        if c1.health <= 0:
            print(f'{c2.name} wins!')
        else:
            print(f'{c1.name} wins!')

        c1.heal(50)
        c2.heal(50)

def helper_find_creature(name: str, realms_obj: RealmsRegistry):
        for realm in realms_obj.all_realms:
            if name in realm.creatures:
                return realm.creatures[name]
        return None

def menu():
    choice = input("Welcome to the Realms of Pythonia:\nEnter your choice (1–4 or 5 to quit the game):\n"
                       "1. Display all realms and their creatures\n"
                       "2. Find a creature in a realm, sprinkle dust if this is a fairy\n"
                       "3. Add a quest for fairies only\n"
                       "4. Start a battle between 2 creatures\n"
                       "5. Exit\n")
    return choice

def main():
    realms_obj = RealmsRegistry()
    realms_obj.setup_realms()
    while True:
        choice = menu()
        match choice:
            case "1":
                realms_obj.list_all_realms()
            case "2":
               creature_name = input("Enter the creature's name that you would like to find out more about")

               check = realms_obj.find_creature(creature_name)
               if check is None:
                   print(f'{creature_name} is not found in any of the realms.')
                   continue
               creature = realms_obj.find_creature(creature_name)[0]
               realm = realms_obj.find_creature(creature_name)[1]
               print(f'The creature {creature.name} is in the {realm.name} and is of type {creature.creature_type}')
               if isinstance(creature, Fairy):
                   creature.boost_dust(70)
            case "3": # 4 marks
                creature_name = input("Name a fairy to add a quest: ")
                creature = realms_obj.find_creature(creature_name)[0]

                if creature is None:
                    print('You cannot add a quest to this creature.')
                    continue
                elif isinstance(creature, Fairy):
                    creature.add_quest('Create rain pearls')
                    creature.list_quests()
                else:
                    print(f'{creature_name} is not a fairy! No quest can be given to this creature.')
                    continue

            case "4":
                arena = BattleArena("Crimson Mountains")
                print(f'The battle will take place in the largest realm ->>> {arena.location}')
                creature1 = input("Who is the first creature that will battle?")
                c1 = helper_find_creature(creature1, realms_obj)
                creature2 = input("Who is the second creature that will battle?")
                c2 = helper_find_creature(creature2, realms_obj)
                if not c1:
                    print(f'Creature {creature1} not found')
                if not c2:
                    print(f'Creature {creature2} not found')
                if c1 and c2:
                    arena.start_battle(c1, c2)
            case "5":
                print("Exiting the realms.....")
                break
            case _:
                print("Invalid choice, try again.")

if __name__ == "__main__":
    main()