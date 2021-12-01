class Configuration:
    def __init__(self, options):
        self.clientID: str = options.clientID
        self.clientOptions = options.clientOptions
        self.clientSecret = options.clientSecret
        self.owners = options.owners
        self.token = options.token