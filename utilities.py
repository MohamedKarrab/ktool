import sys

def sys_arg_cleaner():
    prog_name = sys.argv[0]
    sys.argv.clear()
    sys.argv.append(prog_name)

