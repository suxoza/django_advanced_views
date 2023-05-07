from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from polls import apiviewset
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model


class TestPoll(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = apiviewset.PollViewSet.as_view({"get": "list"})
        self.uri = "/polls/"

        self.user = self.setup_user()
        self.token = Token.objects.create(user=self.user)
        self.token.save()

    @staticmethod
    def setup_user():
        User = get_user_model()
        return User.objects.create_user(
            "test", email="testuser@test.com", password="test"
        )

    def test_list(self):
        request = self.factory.get(self.uri)
        response = self.view(request)
        self.assertEqual(
            response.status_code,
            200,
            f"Expected Response Code 200, received {response.status_code} instead.",
        )

    def test_auth_list(self):
        request = self.factory.get(
            self.uri, HTTP_AUTHORIZATION=f"Token {self.token.key}"
        )
        request.user = self.user
        response = self.view(request)
        self.assertEqual(
            response.status_code,
            200,
            f"Expected Response Code 200, received {response.status_code} instead.",
        )


# apiClient
from rest_framework.test import APIClient


class TestPoll2(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.factory = APIRequestFactory()
        self.view = apiviewset.PollViewSet.as_view({"get": "list"})
        self.uri = "/polls/"

        self.user = self.setup_user()
        self.token = Token.objects.create(user=self.user)
        self.token.save()

    @staticmethod
    def setup_user():
        User = get_user_model()
        return User.objects.create_user(
            "test", email="testuser@test.com", password="test"
        )

    def test_list(self):
        response = self.client.get(self.uri)
        self.assertEqual(
            response.status_code,
            200,
            "Expected Response Code 200, received {0} instead.".format(
                response.status_code
            ),
        )

    def test_create(self):
        self.client.login(username="test", password="test")
        params = {"question": "some question", "created_by": 1}
        response = self.client.post(self.uri, params)
        self.assertEqual(
            response.status_code,
            200,
            f"Expected Response Code 200, received {response.status_code} instead.",
        )
