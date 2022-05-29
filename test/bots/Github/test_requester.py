import unittest
from unittest.mock import patch
from bots.Github.requester import requestsGithub
from test.bots.Github import common
from bots.Github.githubrepository import GithubRepository
from bot.IRepository import IBot

class TestGithubRepository(unittest.TestCase):
    
    resource="https://api.github.com"
    username="ivanmedina"

    def test_requester(self):
        with patch('bots.Github.githubrepository.requests.get') as mock_get:
            mock_get.return_value.status_code=200
            repo = GithubRepository()
            requester = requestsGithub( repo, self.resource )
            bcon=requester.requester( self.resource )
            self.assertEqual( bcon.status_code, 200 )
            disc = repo.disconnect(bcon)
        self.assertTrue(disc)

    def test_requestUser(self):
        with patch('bots.Github.githubrepository.requests.get') as mock_get:
            mock_get.return_value.status_code=200
            repo = GithubRepository()
            requester = requestsGithub( repo, self.resource )
            bcon=requester.requestUser( self.username )
            self.assertEqual( bcon.status_code, 200 )
            disc = repo.disconnect(bcon)
        self.assertTrue(disc)

    def test_requestFollowers(self):
        with patch('bots.Github.githubrepository.requests.get') as mock_get:
            mock_get.return_value.status_code=200
            repo = GithubRepository()
            requester = requestsGithub( repo, self.resource )
            bcon=requester.requestFollows( self.username, 'followers' )
            self.assertEqual( bcon.status_code, 200 )
            disc = repo.disconnect(bcon)
        self.assertTrue(disc)

    def test_requestFollows(self):
        with patch('bots.Github.githubrepository.requests.get') as mock_get:
            mock_get.return_value.status_code=200
            repo = GithubRepository()
            requester = requestsGithub( repo, self.resource )
            bcon=requester.requestFollows( self.username, 'following' )
            self.assertEqual( bcon.status_code, 200 )
            disc = repo.disconnect(bcon)
        self.assertTrue(disc)

    def test_requestRepos(self):
        with patch('bots.Github.githubrepository.requests.get') as mock_get:
            mock_get.return_value.status_code=200
            repo = GithubRepository()
            requester = requestsGithub( repo, self.resource )
            bcon=requester.requestUserRepos( self.username )
            self.assertEqual( bcon.status_code, 200 )
            disc = repo.disconnect(bcon)
        self.assertTrue(disc)