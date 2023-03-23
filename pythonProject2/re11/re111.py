import re

match_obj = re.match("^\d.*", "1hellowwewww")
result = match_obj.group()
print(result)
