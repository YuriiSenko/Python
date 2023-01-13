# Create a parent class for game characters
class NinjaTurtles:

    # Initiate characters
    def __init__(self, name, skill_level, blindfold):
        self.name = name
        self.skills = skill_level
        self.blindfold = blindfold
        self.health = 100

    # Presentation of the characters
    def ninja_presentation(self):
        presentation = (self.name + ":\n 1) Skill level - " + str(self.skills) + "\n 2) Blindfold color - " +
                        self.blindfold + "\n 3) Health - " + str(self.health).title())
        print(presentation)

    # Increase the level of characters
    def level_up(self):
        self.skills += 10

    # Make characters move
    def move(self):
        print(self.name + " is moving")

    # Change the blindfold color
    def set_blindfold(self, new_blindfold):
        self.blindfold = new_blindfold

    # Make characters fight
    def fight(self):
        print(self.name + " is fighting")

    # Change health
    def change_health(self, new_health):
        self.health = new_health

# Create a child class for the super character
class SuperTurtle(NinjaTurtles):
    # Initiate the super character
    def __init__(self, name, skill_level, blindfold, superpower):
        super().__init__(name, skill_level, blindfold)
        self.power = superpower
        self.power = 100

    # Presentation of the super character
    def ninja_presentation(self):
        presentation = (self.name + ":\n 1) Skill level - " + str(self.skills) + "\n 2) Blindfold - " +
                        self.blindfold + "\n 3) Health - " + str(self.health) + "\n 4) Superpower level - " +
                        str(self.power).title())
        print(presentation)

    # Use the power
    def use_power(self):
        self.power -= 5


# Create objects
superturtle = SuperTurtle("Massimo", 99, "green", 100)
my_turtle1 = NinjaTurtles("Leonardo", 50, "blue")
my_turtle2 = NinjaTurtles("Rafael", 47, "red")
my_turtle3 = NinjaTurtles("Michelangelo", 45, "orange")
my_turtle4 = NinjaTurtles("Donatello", 46, "purple")

# Use character methods
my_turtle1.ninja_presentation()  # present Leonardo
my_turtle1.move()  # move Leonardo
my_turtle2.level_up()  # boost Rafael's level
my_turtle2.ninja_presentation()  # present Rafael
my_turtle3.ninja_presentation()  # present Michelangelo
my_turtle3.fight()  # make Michelangelo fight
my_turtle4.set_blindfold("violet")  # change Donatello's blindfold
my_turtle4.ninja_presentation()  # present Donatello
superturtle.use_power()  # use Massimo's superpower
superturtle.change_health(99)  # change Massimo's health
superturtle.ninja_presentation()  # present Massimo