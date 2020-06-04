from abc import ABC, abstractmethod
import re

class ParserInterface(ABC):
    @staticmethod
    def __init__(self):
        pass

    @staticmethod
    def getElements(self):
        pass

    @staticmethod
    def __repr__(self):
        pass


class AddParser(ParserInterface):
    def __init__(self, msg_body):
        self.msg_body = msg_body
        self.times = []
        self.reminder = []
        self.receivers = []
        self.elements = []

    def getElements(self):
        for t in self.parseTimes():
            self.elements.append(t)

        for m in self.parseReminder():
            self.elements.append(m)

        for r in self.parseReceivers():
            self.elements.append(r)

        return self.elements

    def parseTimes(self):
        split_times = re.findall(r'(@\d+:\d+\s*\w*)', self.msg_body)

        for t in split_times:
            self.times.append(t.strip())

        return self.times
    
    def parseReceivers(self):
        split_receivers = re.findall(r'(#\d+)', self.msg_body)

        for r in split_receivers:
            self.receivers.append(r.strip())
        
        return self.receivers

    def parseReminder(self):
        split_reminders = re.findall(r'(\"[^\"]*\")', self.msg_body)

        for r in split_reminders:
            self.reminder.append(r.strip())

        return self.reminder

    def __repr__(self):
        return self.msg_body

ap = AddParser('+ @12:00 @13:00 "Get coffee" "get beans" #1234567899')
print(ap.msg_body)
print(ap.getElements())