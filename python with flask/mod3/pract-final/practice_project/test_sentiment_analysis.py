from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

import unittest

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        result_1 = sentiment_analyzer('I love working')
        
        self.assertEqual(result_1['label'], 'SENT_POSITIVE')

        result_2 = sentiment_analyzer('I hate working')
        self.assertEqual(result_2['label'], 'SENT_NEGATIVE')


        result_3 = sentiment_analyzer('I neutral about that event')
        self.assertEqual(result_3['label'], 'SENT_NEUTRAL')

unittest.main()