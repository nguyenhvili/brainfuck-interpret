import settings


class Lex:
    def __init__(self, filename):
        self.program = open(filename, 'r').read()
        self.index = 0
        self.max_index = len(self.program)

    def get_char(self):
        if self.index == self.max_index:
            return ""

        result = "#"

        while result not in settings.ALLOWED_CHARACTERS:
            result = self.program[self.index]
            self.index += 1

        return result

    def jump(self, index):
        self.index = index
