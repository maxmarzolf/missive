import pytest

from app.sms.Parser import AddParser

def test_AddParser_getElements():
    ap = AddParser('+ @12:00;@13:00 "Get coffee" #1234567899')
    assert ap.getElements() == ['@12:00', '@13:00', '"Get coffee"', '#1234567899']

def test_AddParser_parseReminder():
    ap = AddParser('+ @14:00@12:00@9:00 "Pick up cake and cheese" #2342342344#8578478574')
    assert ap.parseReminder() == ['"Pick up cake and cheese"']

def test_AddParser_parseReminder_quotes():
    ap = AddParser('+ @14:00@12:00@9:00 "Pick up cake and \'cheese\'" #2342342344#8578478574')
    print(ap.msg_body)
    assert ap.parseReminder() == ['"Pick up cake and \'cheese\'"']

def test_AddParser_parseReminder_multiple():
    ap = AddParser('+ @14:00@12:00@9:00 "Pick up cake and cheese" "Grab coffee for road" #2342342344#8578478574')
    assert ap.parseReminder() == ['"Pick up cake and cheese"', '"Grab coffee for road"']

def test_AddParser_parseReminder_quotes_multiple():
    ap = AddParser('+ @14:00@12:00@9:00 "Pick up cake and \'cheese\'" "Get \'chicken\'" #2342342344#8578478574')
    assert ap.parseReminder() == ['"Pick up cake and \'cheese\'"', '"Get \'chicken\'"']

def test_AddParser_parseReceivers_nospace():
    ap = AddParser('+ @14:00@12:00@9:00 "Pick up cake and \'cheese\'" #2342342344#8578478574')
    assert ap.parseReceivers() == ['#2342342344', '#8578478574']

def test_AddParser_parseReceivers_semicolon():
    ap = AddParser('+ @14:00@12:00@9:00 "Pick up cake and \'cheese\'" #2342342344;#8578478574')
    assert ap.parseReceivers() == ['#2342342344', '#8578478574']

def test_AddParser_parseReceivers_space():
    ap = AddParser('+ @14:00@12:00@9:00 "Pick up cake and \'cheese\'" #2342342344 #8578478574')
    assert ap.parseReceivers() == ['#2342342344', '#8578478574']

def test_AddParser_parseTimes_nospace():
    ap = AddParser('+ @14:00@12:00@9:00 "Pick up cake and \'cheese\'" #2342342344#8578478574')
    assert ap.parseTimes() == ['@14:00', '@12:00', '@9:00']

def test_AddParser_parseTimes_space():
    ap = AddParser('+ @14:00 @12:00 @9:00 "Pick up cake and \'cheese\'" #2342342344#8578478574')
    assert ap.parseTimes() == ['@14:00', '@12:00', '@9:00']

def test_AddParser_parseTimes_semicolon():
    ap = AddParser('+ @14:00;@12:00;@9:00 "Pick up cake and \'cheese\'" #2342342344#8578478574')
    assert ap.parseTimes() == ['@14:00', '@12:00', '@9:00']

def test_AddParser_repr():
    ap = AddParser('+ @12:00;@13:00 "Get coffee" #1234567899')
    assert ap.__repr__() == '+ @12:00;@13:00 "Get coffee" #1234567899'