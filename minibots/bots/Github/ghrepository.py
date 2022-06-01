from minibots import entity
import json

class ghrepository(entity):
    
    name: str
    description: str
    url: str
    size: int
    clone: str

    def __init__( self, id:int, name:str, description:str, url:str, size:int, clone:str ):
        self.id=id
        self.name=name
        self.description=description
        self.url=url
        self.size=size
        self.clone=clone
    
    def __str__(self) -> str:
        return json.dumps(self.__dict__, indent=2, separators=(',', ': '))