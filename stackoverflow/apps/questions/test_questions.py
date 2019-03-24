"""
Testing the teammates app and endpoints
"""
from rest_framework.test import APITestCase


class QuestionsTestClass(APITestCase):
    """
    Testclass for teamates endpoints
    """

    def test_response_for_getting_all_questions(self):
        """
        Ensure we get a 200 response as we get all teammates
        """
        response = self.client.get("/questions/", format='json')
        self.assertEqual(response.status_code, 200)
