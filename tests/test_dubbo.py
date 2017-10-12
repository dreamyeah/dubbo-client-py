import httplib
import json

__author__ = 'caozupeng'


def raw_client(app_params):
    headers = {"Content-type": "application/json-rpc",
               "Accept": "text/json"}
    h1 = httplib.HTTPConnection('10.165.124.205', port=2181)
    h1.request("POST", '/com.netease.pop.ic.service.ProvinceService', json.dumps(app_params), headers)
    response = h1.getresponse()
    return response.read()


if __name__ == '__main__':
    app_params = {
        "jsonrpc": "2.0",
        "method": "isPhoneNoLimit",
        "params": ["MOBILE", "130000", "A001"],
        "id": 1
    }
    print json.loads(raw_client(app_params), encoding='utf-8')
