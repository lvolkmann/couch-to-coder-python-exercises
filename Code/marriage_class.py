class person:

    def __init__(self, xname):
        self.name = xname
        self.spouse = ""

    def __add__(self, p2):
        
        self.spouse = p2
        p2.spouse = self

    def __str__(self):
        return self.name

    def showPartner(self):
        print(self.spouse)


me = person("landon")
her = person("literally anyone please")
me + her

me.showPartner()
her.showPartner()
