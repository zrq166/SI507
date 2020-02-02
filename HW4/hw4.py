'''
SI 507 F19 homework 4: Classes and Inheritance

Your discussion section:
People you worked with:

######### DO NOT CHANGE PROVIDED CODE ############ 
'''

#######################################################################
#---------- Part 1: Class
#######################################################################

'''
Task A
'''
from random import randrange
class Explore_pet:
    boredom_decrement = -4
    hunger_decrement = -4
    boredom_threshold = 6
    hunger_threshold = 10
    def __init__(self, name="Coco"):
        self.name = name
        self.hunger = randrange(self.hunger_threshold)
        self.boredom = randrange(self.boredom_threshold)

    def mood(self):
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            return "happy"
        elif self.hunger > self.hunger_threshold:
            return "hungry"
        else:
            return "bored"

    def __str__(self):
        state = "I'm " + self.name + '. '
        state += 'I feel ' + self.mood() + '. '
        if self.mood() == 'hungry':
            state += 'Feed me.'
        if self.mood() == 'bored':
            state += 'You can teach me new words.'
        return state
coco = Explore_pet()

#your code begins here . . . 
brian=Explore_pet("brian")
brian.hunger=12
#print(brian)
'''
Task B
'''
#add your codes inside of the Pet class
class Pet:
    boredom_decrement = -4
    hunger_decrement = -4
    boredom_threshold = 6
    hunger_threshold = 10
    def __init__(self, name="Coco"):
        self.name = name
        self.hunger = randrange(self.hunger_threshold)
        self.boredom = randrange(self.boredom_threshold)
        self.words=[]
        self.words.append("hello")

    def mood(self):
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            return "happy"
        elif self.hunger > self.hunger_threshold:
            return "hungry"
        else:
            return "bored"

    def __str__(self):
        state = "I'm " + self.name + '. '
        state += 'I feel ' + self.mood() + '. '
        if self.mood() == 'hungry':
            state += 'Feed me.'
        if self.mood() == 'bored':
            state += 'You can teach me new words.'
        return state

    def clock_tick(self):
        self.hunger=self.hunger+2
        self.boredom=self.boredom+2

    def say(self):
        print("I know how to say: ")
        for oneword in self.words:
            print(oneword)

    def teach(self,word):
        self.words.append(word)
        if self.boredom+self.boredom_decrement<0:
            self.boredom=0
        else:
            self.boredom=self.boredom+self.boredom_decrement

    def feed(self):
        if self.hunger+self.hunger_decrement<0:
            self.hunger=0
        else:
            self.hunger=self.hunger+self.hunger_decrement

    def hi(self):
        print(self.words[randrange(len(self.words))])

'''
Task C
'''


def teaching_session(my_pet,new_words):
    #your code begins here . . .
    for i in new_words:
        my_pet.teach(i)
        my_pet.hi()
        print(my_pet)
        if my_pet.mood=='hungry':
            my_pet.feed()
        my_pet.clock_tick()

if  __name__=="__main__":
    alice=Pet("Alice")
    teaching_session(alice,['I am sleepy', 'You are the best','I love you, too'] )




#######################################################################
#---------- Part 2: Inheritance - subclasses
#######################################################################
'''
Task A: Dog and Cat    
'''
#your code begins here . . .
class Dog(Pet):
    def __str__(self):
        state = "I'm " + self.name + ', arrrf! '
        state += 'I feel ' + self.mood() + ', arrrf! '
        if self.mood() == 'hungry':
            state += 'Feed me, arrrf!'
        if self.mood() == 'bored':
            state += 'You can teach me new words, arrrf!'
        return state

class Cat(Pet):
    def __init__(self,name="Coco",meow_count=1):
        super().__init__(name)
        self.meow_count=meow_count

    def hi(self):
        choosen_word=self.words[randrange(len(self.words))]
        print_word=''
        for i in range(self.meow_count):
            print_word+=choosen_word
        print(print_word)

'''
Task B: Poodle 
'''

#your code begins here . . .
class Poodle(Dog):
    def dance(self):
        return "Dancing in circles like poodles do!"

    def say(self):
        print(self.dance())
        super().say()

if  __name__=="__main__":
    poodleA=Poodle("poodleA")
    poodleA.say()

    catA=Cat("catA",5)
    catA.hi()


