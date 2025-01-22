class NewList(list):
    def minimum(self):
        if len(self) == 0:
            raise ValueError("List is Empty")
        return min(self)

    def maximum(self):
        if len(self) == 0:
            raise ValueError("List is Empty")
        return max(self)


new_list = NewList([4, 7, 2, 9])
print(new_list.minimum())
print(new_list.maximum())

empty_list = NewList()
print(empty_list.minimum())
print(empty_list.maximum())