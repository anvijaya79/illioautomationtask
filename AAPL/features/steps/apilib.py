import json

class core:

    def __init__(self):
        pass

    def read(self):
        with open("C://Users//anvij//PycharmProjects//AAPL//features//steps//data.json", 'r')  as data:
            value = json.load(data)
            print(value)
