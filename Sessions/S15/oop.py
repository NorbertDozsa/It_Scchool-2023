class Person:
    
    def __init__(self):
          self.__height = 195
          self.__weight = 0

    def get_height_cm(self):
         return self.__height
    
    def get_height_m(self):
         return self.__height / 100
     

norbert = Person()
andreea = Person()

print(f"Height in cm: {norbert.get_height_cm()}")
print(f"Height in m: {norbert.get_height_m()}")
