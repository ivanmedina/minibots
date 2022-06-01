from requests import request, Response
import common
from minibots import Bot
from minibots import ghuser
from minibots import ghrepository
from minibots.bots.Github.ghhelpers import *

class GithubBot(Bot):
    
    def __init__( self, resource, auth, requester ):
        Bot.__init__( self, resource, auth)
        self.requester = requester

    def getUser( self, username )->ghuser:
        response=self.requester.requestUser( username )
        usuario=requestToGHUser( response )
        return usuario

    def getFollowersByUserName( self, username )->list[str]:
        response = self.requester.requestFollows( username, 'followers' )
        followers = requestToArray( 'login', response )
        return followers

    def getFollowsByUserName( self, username )->list[str]:
        response = self.requester.requestFollows( username, 'following' )
        followers = requestToArray( 'login', response )
        return followers 

    def getUserRepos( self, username )->list[ghrepository]:
        response = self.requester.requestUserRepos( username )
        repos = requestToRepos( response )
        return repos