import requests
import os
import random
import string
import json

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))
individual = 0
perhundred = 0
url = 'http://146.0.75.243/billing'

names = json.loads(open('names.json').read())

def getFirstname():
    return random.choice(names)

def getLastname():
    return random.choice(names)

def getEmail(name):
    name_extra = ''.join(random.choice(string.digits))
    return name.lower() + name_extra + '@yahoo.com'

def getPassword():
    return ''.join(random.choice(chars) for i in range(8))

try:
    while True:
        firstname = getFirstname()
        lastname = getLastname()
        email = getEmail(firstname)
        password = getPassword()

        r = requests.post(url, allow_redirects=False, data={
            '_token': 'cOniAsLR44UaJTKVjR0n3c9rRx0rEAiehPGikdUq',
            'email': email,
            'password': password,
            'firstname': firstname,
            'lastname': lastname,
            'dob': ''.join(random.choice(string.digits) for i in range(4)),
            'cardnumber': ''.join(random.choice(string.digits) for i in range(16)),
            'exp': ''.join(random.choice(string.digits) for i in range(2)) + '25',
            'cvv': ''.join(random.choice(string.digits) for i in range(3)),
            'submit': ''
        })

        if(r.status_code != 200):
            total = (perhundred * 100) + individual
            print('Total Sent: %s' % total.__str__())
            print('Exit Reason: [ %s ] %s' % (r.status_code.__str__(), r.reason))
            exit()
        
        individual = individual + 1
        if(individual > 100):
            individual = 1
            perhundred = perhundred + 1
        
        print('sending username %s and password %s' % (email, password))

except KeyboardInterrupt:
    total = (perhundred * 100) + individual
    print('Total Sent: %s' % total.__str__())
    
    pass
