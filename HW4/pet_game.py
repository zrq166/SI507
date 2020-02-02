from pip._vendor.distlib.compat import raw_input
import hw4


class Pet(hw4.Pet):
    def __init__(self, name="Coco"):
        super().__init__(name)
        self.age = 0


class Dog(hw4.Dog):
    def __init__(self, name="Coco"):
        super().__init__(name)
        self.age = 0

    def clock_tick(self):
        super().clock_tick()
        self.age += 2


class Cat(hw4.Cat):
    def __init__(self, name="Coco", meow_count=1):
        super().__init__(name, meow_count)
        self.age = 0

    def clock_tick(self):
        super().clock_tick()
        self.age += 3


class Poodle(hw4.Poodle):
    def __init__(self,name="Coco"):
        super().__init__(name)
        self.age = 0

    def clock_tick(self):
        super().clock_tick()
        self.age += 2


def whichone(petlist, name):
    for pet in petlist:
        if pet.name == name:
            return pet
    return None  # no pet matched


pet_types = {'dog': Dog, 'poodle': Poodle, 'cat': Cat}


def whichtype(adopt_type="general pet"):
    return pet_types.get(adopt_type.lower(), Pet)


def play():
    animals = []
    option = ""
    base_prompt = """
        Quit
        Adopt <petname_with_no_spaces> <pet_type - choose dog, cat, lab, poodle, bird, or another unknown pet type>
        Greet <petname>
        Teach <petname> <word>
        Feed <petname>

        Choice: """
    feedback = ""
    haspetyet=0
    while True:
        if len(animals)!=0:
            haspetyet=1
        temp_animals = []
        action = raw_input(feedback + "\n" + base_prompt)
        feedback = ""
        words = action.split()
        if len(words) > 0:
            command = words[0]
        else:
            command = None
        if command == "Quit":
            print("Exiting...")
            return
        elif command == "Adopt" and len(words) > 1:
            if whichone(animals, words[1]):
                feedback += "You already have a pet with that name\n"
            else:
                # figure out which class it should be
                if len(words) > 2:
                    Cl = whichtype(words[2])
                else:
                    Cl = Pet
                # Make an instance of that class and append it
                animals.append(Cl(words[1]))
        elif command == "Greet" and len(words) > 1:
            pet = whichone(animals, words[1])
            if not pet:
                feedback += "I didn't recognize that pet name. Please try again.\n"
                # print
            else:
                pet.hi()
        elif command == "Teach" and len(words) > 2:
            pet = whichone(animals, words[1])
            if not pet:
                feedback += "I didn't recognize that pet name. Please try again."
            else:
                pet.teach(words[2])
        elif command == "Feed" and len(words) > 1:
            pet = whichone(animals, words[1])
            if not pet:
                feedback += "I didn't recognize that pet name. Please try again."
            else:
                pet.feed()
        else:
            feedback += "I didn't understand that. Please try again."

        for pet in animals:
            pet.clock_tick()
            if pet.age > 18:
                print(pet.name+" leaves the world.")
            else:
                temp_animals.append(pet)
                feedback += "\n" + pet.__str__()


        while len(animals) != 0:
            animals.pop()
        for i in temp_animals:
            animals.append(i)

        if haspetyet==1:
            if len(animals)==0:
                print("Game ends!")
                userinput=input("Input your option(PLAY IT AGAIN or QUIT):")
                if userinput=="PLAY IT AGAIN":
                    while len(animals) != 0:
                        animals.pop()
                    haspetyet=0
                else:
                    return

play()
