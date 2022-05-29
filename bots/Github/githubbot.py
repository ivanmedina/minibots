from requests import request, Response
import common
from bot.bot import Bot
from bots.Github.user import user
from bots.Github.repository import repository
from helpers import *

class GithubBot(Bot):
    
    def __init__( self, resource, auth, requester ):
        Bot.__init__( self, resource, auth)
        self.requester = requester

    def getUser( self, username )->user:
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

    def getUserRepos( self, username )->list[repository]:
        response = self.requester.requestUserRepos( username )
        repos = requestToRepos( response )
        return repos