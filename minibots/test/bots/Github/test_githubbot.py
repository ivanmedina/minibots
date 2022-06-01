import unittest
from unittest.mock import patch
import common 
from minibots import GithubRepository

class TestGithubBot(unittest.TestCase):

    resource = "https://api.github.com"

    def test_getUser(self):

        with patch('minibots.bots.Github.githubrepository.requests.get') as mock_get:
            mock_get.return_value.status_code=200
            obj = GithubRepository()
            response = obj.bconnect(self.resource)
        self.assertEqual(response.status_code,200)