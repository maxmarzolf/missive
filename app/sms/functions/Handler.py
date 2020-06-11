import Parser


def Handler(sms_message):
    if sms_message[0] == '+':
        ap = Parser.AddParser(sms_message)  # .getElements() which returns an object
        # DBHandler (to log the request)
        # Scheduler (to schedule the request)
        # MessageHandler (to communicate with the user)
        print(ap.getElements())
    elif sms_message[0] == '-':
        rp = Parser.RemoveParser(sms_message)
        print(rp.getElements())
    elif sms_message[0] == '!':
        ip = Parser.InfoParser(sms_message)
        print(ip.getElements())
    elif sms_message[0] == '?':
        hp = Parser.HelpParser(sms_message)
    else:
        print("other/unknown command")


Handler('+ @12:00 "something here" #1234121234')
