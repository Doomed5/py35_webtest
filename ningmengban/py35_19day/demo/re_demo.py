import re

str1 = 'dsafadqed13edasd13123456789d! $asdasfgs     asdasfd13221334444r21253gvsdfs13213'
res = re.findall('\d{11}', str1)
print(res)
print(re.findall('\D', str1))
print(re.findall('\s', str1))
print(re.findall('.', str1))
s2 = "1122334455abcdefg"
print(re.findall('[1-9]', s2))

