from oop1 import Car
from oop1 import Person


gas1 = ''

nissan = Car()
norbert = Person()
andreea = Person()


print(nissan.get_consumption())

nissan.start_engine()
nissan.refill(30)
nissan.drive(11)

nissan.add_person(norbert)
nissan.add_person(andreea)


print(nissan.get_consumption())
