class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print '%s: %s' % (self.name, self.score)

jim = Student('Jim', 98)
lucy = Student('Lucy', 99)

jim.print_score()
lucy.print_score()