class parrot:
    species="bird"
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade = grade
ob=parrot("john",46,4)
ob1=parrot("lil bro",96,100)
print("first objekt has the name",ob.name,"his age is",ob.age,"years old and he is in grade ",ob.grade,"he belong to the species",ob.species)
print("second objekt has the name",ob1.name,"his age is",ob1.age,"years old and he is in grade ",ob1.grade,"he belong to the species",ob1.species)