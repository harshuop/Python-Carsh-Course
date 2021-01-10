from trial import AnonymousSurvey
import unittest

class AnonymousTest(unittest.TestCase):
    def setUp(self):
        self.question = "This is my question!"
        x = AnonymousSurvey(self.question)
        self.store_response = ['English','Hindi','spanish']
        for response in self.store_response:
            .store_response.append(response)
        self.assertIn('English', x.store_response())
unittest.main()