import json

class JsonUtil(object):

    def stringify(self, obj):
        return json.dumps(obj)

JSON = JsonUtil()
