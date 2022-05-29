import unittest
from test.bot import common
from bot.bot import Bot

class TestBot(unittest.TestCase):
    
    resource = 'https://api.github.com'
    auth={}

    def test_isConnected(self):
        b=Bot( self.resource, self.auth )
        self.assertFalse(b.isConnect())
        b.connected=True
        self.assertTrue(b.isConnect())