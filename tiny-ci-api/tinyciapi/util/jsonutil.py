import json

class JsonUtil(object):

    def stringify(self, obj, indent=False):
        return json.dumps(obj, indent=False)

    def parse(self, data):
        return json.loads(data)

JSON = JsonUtil()
