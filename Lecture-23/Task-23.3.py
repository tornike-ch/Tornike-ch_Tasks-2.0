
class Student:
    def __init__(self, name):
        self._name = name
        self._scores = []

    def add_score(self, score):
        if 0 <= score <= 100:
            self._scores.append(score)
        else:
            print("ქულა არასწორადაა შეყვანილი")

    @property
    def average(self):
        if self._scores:
            return round(sum(self._scores) / len(self._scores))
        return 0.0

    @property
    def scores(self):
        return self._scores.copy()


def main():
    students = [
        Student("თორნიკე"),
        Student("ნინო")
    ]

    students[0].add_score(85)
    students[0].add_score(90)
    students[0].add_score(78)

    students[1].add_score(92)
    students[1].add_score(88)
    students[1].add_score(95)


    for student in students:
        print(f"{student._name}ის ქულების საშუალოა: {student.average:}")


    new_student = Student("მარიამი")
    new_student.add_score(99)
    new_student.add_score(85)
    new_student.add_score(101)
    print(f"{new_student._name}ის ქულების საშუალოა: {new_student.average:}")


if __name__ == "__main__":
    main()