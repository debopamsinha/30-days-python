class Person:
    def __init__(self, initialAge):
        # to run some checks on initialAge
        if initialAge < 0:
            print("Age is not valid, setting age to 0.")
        else:
            self.age = initialAge

    def amIOld(self):
        # print out the correct statement to the console
        if age < 13:
            print("You are young.")
        elif 13 <= age < 18:
            print("You are a teenager.")
        elif age >= 18:
            print("You are old.")

    def yearPasses(self):    
        # Increment the age of the person in here
        global age
        age += 1
