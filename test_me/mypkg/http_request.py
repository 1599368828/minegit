
import requests
import json

#get请求
def get_response(url):
    r = requests.get(url)
    r = json.loads(r.text)
    return r


#post请求
def post_response(url, data):
    payjson = json.dumps(data)
    r = requests.post(url, data=payjson)
    r = json.loads(r.text)
    return r


