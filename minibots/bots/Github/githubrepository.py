from requests import request, Response
import common
import requests
from minibots import IBot

class GithubRepository(IBot):

    def bconnect( self, resource:str )->Response:
        r=requests.get(resource)
        return r
    
    def disconnect( self, req:Response )->bool:
        try:
            req.close()
            return True
        except: return False

    def get(self, resource:str)->Response:
        return requests.get(resource)