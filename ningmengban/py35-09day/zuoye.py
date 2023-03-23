list1 = []
with open(file='1.txt', mode='r', encoding='utf-8') as f:
    res = {}
    for k,v in enumerate(f.readlines()):
        key = 'data{}'.format(k)
        value = v.replace('\n','').replace(' ','')
        res[key] = value
        # list1.extend((line[0],line[1]))
    print(res)
 