class RegularMedia:
    def __init__(self,name="No title"):
        self.name=name
        self.status=0  #status 0 means in library, 1 means checked out
        self.max_days=15
        self.days_remaining=self.max_days
    def clock_tick(self):
        self.days_remaining =self.days_remaining-1
    def checkout(self):
        self.status=1
        self.days_remaining=self.max_days
    def item_return(self):
        self.status=0
    def advance(self,num_days):
        self.days_remaining=self.days_remaining+num_days
    def overdue(self):
        if self.days_remaining>0:
            return False
        else:
            return True

class Reserve(RegularMedia):
    def __init__(self,name="No title"):
        super().__init__(name)
        self.max_days=1
        self.days_remaining=self.max_days

class CD(RegularMedia):
    def __init__(self,name="No title"):
        super().__init__(name)
        self.max_days=7
        self.days_remaining=self.max_days

class Movies(RegularMedia):
    def __init__(self,name="No title"):
        super().__init__(name)
        self.max_days=2
        self.days_remaining=self.max_days


class Library:
    def __init__(self):
        self.reserve_list=[]
        self.reserve_list.append(Reserve("Math"))
        self.reserve_list.append(Reserve("Chemisty"))
        self.cd_list=[]
        self.cd_list.append(CD("Taylor"))
        self.cd_list.append(CD("Michael"))
        self.movie_list=[]
        self.movie_list.append(Movies("love"))
        self.movie_list.append(Movies("summer"))

    def show_catalog(self):
        print("reserve books:")
        print(self.reserve_list[0].name + ', '+ self.reserve_list[1].name)
        print("CDs:")
        print(self.cd_list[0].name+', '+self.cd_list[1].name)
        print("movies:")
        print(self.movie_list[0].name+', '+self.movie_list[1].name)


library=Library()
while True:
    prompt = """
        What would you like to do? 
            catalog: show the catalog
            checkout <item_number>
            return <item_number>
            advance <num_days>
            account: see account status, including checked out items and overdue items
    """
    input1=input(prompt)
    if input1=="catalog":
        library.show_catalog()