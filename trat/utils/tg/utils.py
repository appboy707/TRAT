import shlex


def parse_command(command: str) -> tuple[str]:
    lexer = shlex.shlex(command, posix=True)
    lexer.whitespace_split = True
    lexer.whitespace = ' '
    return tuple(lexer)
