import requests
import json

reg='https://cit-home1.herokuapp.com/api/ga_homework'
txt = json.dumps({'1':{"value":5112,"weight":11881,"volume":11.9,"items":[0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0]},
'2':{"value":5271,"weight":11935,"volume":12,"items":[0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0]}})
head={'content-type': 'application/json'}

p = requests.post(reg, data=txt, headers=head)
print(p)
print(p.json())