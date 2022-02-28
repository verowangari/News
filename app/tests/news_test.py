import unittest
from utils import get_latest_news
class NewsTest(unittest.TestCase):
    def setUp(self):
        self.news_headlines = get_latest_news(
            "Former Attorney General William Barr writes in his forthcoming me...", 
            "Barr says Trump 'lost his grip' in forthcoming memoir",
            "https://thehill.com/homenews/administration/596063-barr-says-trump-lost-his-grip-in-forthcoming-memoir",
            "Donald Trump",
            "2022-02-28T04:15:00Z"
        )

    def test_instance(self):
        self.assertTrue(isinstance(self.news_headlines, get_latest_news))

if __name__ == "__main__":
    unittest.main()
