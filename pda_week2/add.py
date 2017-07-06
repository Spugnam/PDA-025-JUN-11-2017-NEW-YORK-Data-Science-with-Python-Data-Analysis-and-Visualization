import re
from sys import argv
script, expression = argv
arg1, arg2 = re.findall('\d', expression)
print float(arg1) + float(arg2)