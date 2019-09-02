with open('E:/test.txt', encoding = 'utf-8') as file:
    new = file.read()


content = new.replace('\n','|').replace(';','\n')

import re
pattern = re.compile(r'(.+?)(\t.+?)(\|EX.+)\n')
result = re.findall(pattern, content)

final = []
for item in result:
    line = ''.join([item[0], item[2], item[1], '\n'])
    final.append(line)


with open('E:/output.txt', encoding = 'utf-8', mode = 'w') as file:
    file.write(''.join(final))

