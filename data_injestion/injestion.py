import configparser


class Injestor: 

    #consturctor
    def __init__(self):
        config = configparser.RawConfigParser()
        config.read('myconfig.cfg')
        self.yahoo_key = config['yahoo_auth']['consumer_key']
        self.yahoo_secret = config['yahoo_auth']['consumer_secret']
        
