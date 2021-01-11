import pathlib
import json
from pprint import pprint   #  handy way of looking at nested data structures.

with open('service-policy.json', 'r') as opened_file:
    policy = json.load(opened_file)
print(policy)
pprint(policy)

# If you want to add any anything at any particular position

policy['Statement']['Resource'] = 'RDS'
pprint(policy)


with open('service-policy.json', 'w') as opened_file1:
    policy2 = json.dump(policy, opened_file1)
print(policy2)

