import settings


class Interpret:
    def __init__(self, lex):
        self.buffer = [0 for _ in range(settings.BUFFER_SIZE)]
        self.pointer = 0
        self.call_stack = []
        self.lex = lex

    def execute_command(self, command):
        if command == '+':
            self.buffer[self.pointer] += 1

            if self.buffer[self.pointer] > 255:
                self.buffer[self.pointer] = 0
        elif command == '-':
            self.buffer[self.pointer] -= 1

            if self.buffer[self.pointer] < 0:
                self.buffer[self.pointer] = 255
        elif command == '<':
            self.pointer -= 1

            if self.pointer < 0:
                self.buffer[self.pointer] = settings.BUFFER_SIZE - 1
        elif command == '>':
            self.pointer += 1

            if self.pointer >= settings.BUFFER_SIZE:
                self.buffer[self.pointer] = 0
        elif command == '.':
            print(chr(self.buffer[self.pointer]), end='')
        elif command == ',':
            # TODO
            pass
        elif command == '[':
            self.call_stack.append(self.lex.index - 1)
        elif command == ']':
            index = self.call_stack.pop()

            if self.buffer[self.pointer] != 0:
                self.lex.jump(index)
