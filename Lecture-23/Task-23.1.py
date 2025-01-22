
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def get_info(self):
        return f"Name: {self._name}, Age: {self._age}"

def main():    
    person_1 = Person("თორნიკე", 28)
    person_2 = Person("ნინო", 27)

    print(person_1.get_info)
    print(person_2.get_info)

if __name__ == "__main__":
    main()