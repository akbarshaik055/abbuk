import re
line = " I am having a very nice look."
count = len(re.findall(r'\w+', line))
print (count)
