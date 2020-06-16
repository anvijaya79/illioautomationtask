import json
import requests
class core:
    """
       This is a class for REST API connections.
     """

    responsevalue=[]

    def __init__(self,url,payload):
        self.url = url
        self.payload = payload


    def getstatus(self):
        response = requests.get(self.url, params=self.payload)
        statuscode = response.status_code
        core.responsevalue = response.json()
        print(core.responsevalue)
        print(type(core.responsevalue))
        if statuscode == 200:
            return True
        else:
            return False


    def getresponsedata(self):
        return core.responsevalue

