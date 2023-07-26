from lex import Lex
from interpret import Interpret


def main():
    lex = Lex("program.txt")
    interpret = Interpret(lex)

    tmp = lex.get_char()

    while tmp != "":
        interpret.execute_command(tmp)
        tmp = lex.get_char()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
