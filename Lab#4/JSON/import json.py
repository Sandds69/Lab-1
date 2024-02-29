import json

with open('sample-data.json', 'r') as file:
    data = json.load(file)

print("Interface Status")
print('=' * 80)
print(f"DN{" "*30}DESCRIPTION{" "*10}SPEED{" "*10}MTU{" "*10}")
print('-'*80)

for dat in data['imdata'][:3]:
    attributes = dat['l1PhysIf']['attributes']
    print(attributes['dn'], attributes['descr'], " " * 10, attributes['speed'], " " * 5, attributes['mtu'])
          
