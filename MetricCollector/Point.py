import json


class Point:
    def __init__(self, measurement, time):
        self.point = dict()
        self.measurement = measurement
        self.time = time
        self.fields = dict()
        self.tags = dict()

    def addField(self, key, value):
        self.fields[key] = value

    def addTag(self, key, value):
        self.tags[key] = value

    def clearFields(self):
        self.fields.clear()

    def clearTags(self):
        self.tags.clear()

    def createJsonObject(self):
        self.point["time"] = self.time
        self.point["tags"] = self.tags
        self.point["measurement"] = self.measurement
        self.point["fields"] = self.fields
        return self.point

    def printJsonObject(self):
        print(json.dumps(self.point, indent = 4))
