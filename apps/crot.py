import time
import json
import urllib3
http = urllib3.PoolManager()

while True:
    print('crot ok')

    data = {
        'app': 'crot from ' + os.environ['APP']
    }
    print(json.dumps(data))
    c = http.request(
        "POST", "http://logs-01.loggly.com/inputs/69d55737-fc2f-444e-a642-d50f0d514af0/tag/cargo_remote",
        body=json.dumps(data),
        headers={'Content-Type': 'application/json'}).data