import re

text = '''
Ich bin ein http://www.google.de 
Text
über mehrere Zeilen und 
enthalte mehrere Links
wie http://www.spiegel.de
'''

print(text)

urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)

if urls:
    for i in urls:
        print('Link gefunden:', i)