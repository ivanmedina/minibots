import unittest
from unittest.mock import patch
import common 
from minibots import GithubRepository

class TestGithubRepository(unittest.TestCase):

    resource="https://api.github.com"

    def test_bconnect(self):

        with patch('minibots.bots.Github.githubrepository.requests.get') as mock_get:
            mock_get.return_value.status_code=200
            obj = GithubRepository()
            response = obj.bconnect(self.resource)
        self.assertEqual(response.status_code,200)

    def test_disconnect(self):

        with patch('minibots.bots.Github.githubrepository.requests.Response') as mock_response:
            mock_response.return_value.close=None
            obj = GithubRepository()
            status = obj.disconnect(mock_response)
        self.assertTrue(status)

    def test_get(self):

        with patch('minibots.bots.Github.githubrepository.requests.get') as mock_get:
            mock_get.return_value.status_code=200
            obj = GithubRepository()
            response = obj.bconnect(self.resource)
        self.assertEqual(response.status_code,200)     