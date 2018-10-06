"""Connects to the web hosted data store and messaging service using credential from a config.json"""

import json

class Connection(object):
    'Creates a connection object with properties from the config file \
    Tries to connect to the external sources and returns false if anything \
    goes wrong.  Otherwise returns true'

    def __init__(self):
        with open('config.json') as f:
            self.settings = json.load(f)

    def getconnectionprop(self, index):
        return self.settings[index] # return the value corresponding to the index key

    def testcon(self):  
        try:
            # attempt to connect to the external sources
            pass
        except Exception:
            return False
        else:
            return True

if __name__ == "__main__":

    def debug():
        testconnection=Connection()
        print('Connection parameters:')
        print(testconnection.getconnectionprop("dbtarget"))
        print(testconnection.getconnectionprop("dbpassword"))
        print(testconnection.getconnectionprop("msgservicetarget"))
        print(testconnection.getconnectionprop("msgservicepwd"))

    debug()

        