class Bot():

    resource: str
    auth: dict
    connected: bool
    bheaders: dict
    bcookies: dict
    timeout: int

    def __init__( self, resource:str , auth:dict={} ):
        self.resource=resource
        self.auth = auth
        self.connected = False

    def isConnect(self):
        return self.connected