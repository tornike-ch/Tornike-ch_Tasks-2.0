
class Inset:
    def __init__(self):
        self.elements = []

    def insert(self, element):
        if element not in self.elements:
            self.elements.append(element)

    def member(self, element):
        return element in self.elements

    def remove(self, element):
        if element in self.elements:
            self.elements.remove(element)
        else:
            raise ValueError("Element Not Found")

    def __str__(self):
        return str(sorted(self.elements))


inset = Inset()
inset.insert(5)
inset.insert(3)
inset.insert(7)
inset.insert(13)
inset.insert(11)
print(inset.member(3)) 
print(inset.member(8))  
inset.remove(3)
print(inset)