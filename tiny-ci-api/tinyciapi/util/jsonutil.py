import json

class JsonUtil(object):

    def stringify(self, obj, indent=None):
        return json.dumps(obj)

    def parse(self, data):
        return json.loads(data)

JSON = JsonUtil()
