class aclass:
    def __init__(self):
        self.text = ""

    def getString(self):
        self.text = input("Enter a string ")

    def printString(self):
        print(self.text.upper())


obj = aclass()
obj.getString()
obj.printString()