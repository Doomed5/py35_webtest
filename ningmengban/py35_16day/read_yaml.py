import yaml

with open('demo.yaml', 'r', encoding='utf-8') as f:
    res = yaml.load(f, Loader=yaml.Loader)
print(res)
