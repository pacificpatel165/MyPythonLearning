# A platform encoding issue. If you try this on your machine, you may or may not see the problem.

print(open('cafe.txt', 'w', encoding='utf_8').write('café'))

print(open('cafe.txt').read())
#'cafÃ©'