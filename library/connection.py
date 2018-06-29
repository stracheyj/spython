"""Connects to the web hosted data store and messaging service using credential from a config.json"""

class Connection(object):
    'Creates a connection object with properties from the config file \
    Tries to connect to the external sources and returns false if anything \
    goes wrong.  Otherwise returns true'

    def __init__(self):
        pass

    def testcon(self):  
        try:
            # attempt to connect to the external sources
            pass
        except Exception:
            return False
        else:
            return True



        