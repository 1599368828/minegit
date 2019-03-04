

import json
from test_me.mypkg.json_data import lend_invalid_json


a = lend_invalid_json["lend_json_invalid1"]
print("ashiduos",a)
c = json.dumps(a)
b = json.loads(c)
print(a)



































