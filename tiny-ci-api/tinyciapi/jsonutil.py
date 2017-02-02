import json

class JsonUtil(object):

    def stringify(self, obj):
        return json.dumps(obj)

    def parse(self, data):
        return json.loads(data)

JSON = JsonUtil()
