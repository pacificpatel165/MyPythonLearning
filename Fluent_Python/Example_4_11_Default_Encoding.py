# Exploring encoding defaults

expressions = ('\n'
               '    locale.getpreferredencoding()\n'
               '    type(my_file)\n'
               '    my_file.encoding\n'
               '    sys.stdout.isatty()\n'
               '    sys.stdout.encoding\n'
               '    sys.stdin.isatty()\n'
               '    sys.stdin.encoding\n'
               '    sys.stderr.isatty()\n'
               '    sys.stderr.encoding\n'
               '    sys.getdefaultencoding()\n'
               '    sys.getfilesystemencoding()\n'
               '    ')

my_file = open('dummy', 'w')
for expression in expressions.split():
    value = eval(expression)
    print(expression.rjust(30), '->', repr(value))
