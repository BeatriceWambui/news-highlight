import unittest
from app.models import News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behavior of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will before every Test
        '''
        self.new_news = News(1234,'Python Must Be Crazy','A thrilling new Python Series','https://image.tmdb.org/t/p/w500/khsjha27hbs',8.5,129993')
    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))
