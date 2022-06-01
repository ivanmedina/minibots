from requests import request, Response

class requestsGithub():
    
    def __init__( self, repositorio, resource ):
        self.repositorio = repositorio
        self.resource = resource

    def requester( self, url )->Response:
        bconection = self.repositorio.bconnect( self.resource )
        if bconection.status_code==200:
            self.repositorio.disconnect( bconection )
            bconection=self.repositorio.get( url )
            self.repositorio.disconnect( bconection )
        return bconection

    def requestUser( self, username )->Response:
        return self.requester(f'{self.resource}/users/{username}' )

    def requestFollows( self, username, param )->Response:
        return self.requester( f'{self.resource}/users/{username}/{param}?per_page=100' )

    def requestUserRepos( self, username )->Response:
        return self.requester( f'{self.resource}/users/{username}/repos' )

