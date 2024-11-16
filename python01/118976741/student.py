class Student:
    def __init__(self,name,house,):
        self.name=name
        self.house=house


    def __str__(self):
        return f"{self.name} from {self.house}"
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name)L
        if not name:
            raise ValueError
        

    #getter
    @property
    def house(self):
        return self._house
    #setter
    @house.setter
    def house(self,house):
        self._house=house


def main():
    student=get_student()
    print(student)



def get_student():
    name=input("name")
    house=input("house")

    return Student(name,house)

    return student
if __name__=="__main__":
    main()
