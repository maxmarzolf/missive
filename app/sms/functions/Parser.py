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
        self.times = self.parseTimes()
        self.reminder = self.parseReminder()
        self.receivers = self.parseReceivers()
        self.elements = []

    def getElements(self):
        for t in self.times:
            self.elements.append(t)

        for m in self.reminder:
            self.elements.append(m)

        for r in self.receivers:
            self.elements.append(r)

        return self.elements

    def parseTimes(self):
        times = []
        split_times = re.findall(r'(@\d+:\d+\s*\w*)', self.msg_body)

        for t in split_times:
            times.append(t.strip())

        return times

    def parseReceivers(self):
        receivers = []
        split_receivers = re.findall(r'(#\d+)', self.msg_body)

        for r in split_receivers:
            receivers.append(r.strip())

        return receivers

    def parseReminder(self):
        reminders = []
        split_reminders = re.findall(r'(\"[^\"]*\")', self.msg_body)

        for r in split_reminders:
            reminders.append(r.strip())

        return reminders

    def __repr__(self):
        return self.msg_body


class RemoveParser(ParserInterface):
    def __init__(self, sms_msg):
        self.sms_msg = sms_msg
        self.missive_id = self.parseMissiveID()
        self.elements = []

    def getElements(self):
        for m in self.missive_id:
            self.elements.append(m.strip())

        return self.elements

    def parseMissiveID(self):
        message = re.findall(r'(\d+)', self.sms_msg)

        return message

    def __repr__(self):
        return self.sms_msg


class InfoParser(ParserInterface):
    def __init__(self, sms_msg):
        self.sms_msg = sms_msg
        self.times = self.parseTimes()
        self.elements = []

    def getElements(self):
        for t in self.times:
            self.elements.append(t)

        return self.elements

    def parseTimes(self):
        times = []
        split_times = re.findall(r'(@\d+:\d+\s*\w*)', self.sms_msg)

        for t in split_times:
            times.append(t.strip())

        return times

    def __repr__(self):
        return self.sms_msg


class HelpParser(ParserInterface):
    pass
