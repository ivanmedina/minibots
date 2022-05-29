import common
from bot.entity import entity
import json

class user(entity):
    
    username: str
    url: str
    avatar: str
    
    def __init__( self, id:str, username:str, url:str, avatar:str ):
        self.id=id
        self.username=username
        self.url=url
        self.avatar=avatar

    def __str__(self) -> str:
        return json.dumps(self.__dict__, indent=2, separators=(',', ': '))