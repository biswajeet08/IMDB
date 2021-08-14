from django.test import TestCase, Client
from .models import IMDB, User
from rest_framework.test import APITestCase
import json
import base64

credentials_file = open("API/credentials.json")
passwords = json.load(credentials_file)
admin_passwd = base64.b64decode(passwords["admin_password"]).decode()
user_passwd = base64.b64decode(passwords["user_password"]).decode()


class IMDBTestCase(APITestCase):
    def setUp(self):
        User.objects.create_user(username='joey', password=user_passwd)
        User.objects.create_superuser(username='vicky', password=admin_passwd)
        IMDB.objects.create(popularity=87.0, director="David Russel", genre=["Horror", " Mystery", " Thriller"],
                            imdb_score=8.7, name="Bourne")
        IMDB.objects.create(popularity=85.0, director="Zack Athens", genre=["Horror", " Mystery", " Thriller"],
                            imdb_score=8.7, name="MIB")
        self.admin_url = "http://127.0.0.1:8000/admin/imdbapi/"
        self.user_url = "http://127.0.0.1:8000/user/imdbapi/"
        self.headers = {'content-Type': 'application/json'}
        self.admin_auth_headers = {
            'HTTP_AUTHORIZATION': 'Basic ' +
                                  base64.b64encode(bytes(f'vicky:{admin_passwd}', 'utf-8')).decode("ascii")
        }
        self.user_auth_headers = {
            'HTTP_AUTHORIZATION': 'Basic ' +
                                  base64.b64encode(bytes(f'joey:{user_passwd}', 'utf-8')).decode("ascii")
        }

    def test_get_movies_for_admin(self):
        """
        This test method will test the GET request for Admins for all the Movies in database
        """

        payload = {}
        payload = json.dumps(payload)
        response = self.client.generic('GET', self.admin_url, data=payload, **self.admin_auth_headers,
                                       content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_get_movies_for_user(self):
        """
        This test method will test the GET request for Admins for all the Movies in database
        """

        payload = {}
        payload = json.dumps(payload)
        response = self.client.generic('GET', self.user_url, data=payload, **self.user_auth_headers,
                                       content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_get_movie_for_admin(self):
        """
        This test method will test the GET request for Admin for one movie whose name is given in the payload.
        """
        payload = {'name': 'Bourne'}
        payload = json.dumps(payload)
        response = self.client.generic('GET', self.admin_url, data=payload, **self.admin_auth_headers,
                                       content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_get_movie_for_user(self):
        """
        This test method will test the GET request for User for one movie whose name is given in the payload.
        """

        payload = {'name': 'Bourne'}
        payload = json.dumps(payload)
        response = self.client.generic('GET', self.user_url, data=payload, **self.user_auth_headers,
                                       content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_post_movie_for_admin(self):
        """
        This test method will test the POST request for Admin for one movie whose details are given in the payload.
        """
        payload = {"popularity": 88.0,

                   "director": "George Lucas",
                   "genre": [
                       "Action",
                       " Adventure",
                       " Fantasy",
                       " Sci-Fi"
                   ],
                   "imdb_score": 8.8,
                   "name": "Star Wars"}
        payload = json.dumps(payload, indent=4)
        response = self.client.generic('POST', self.admin_url, data=payload, **self.admin_auth_headers,
                                       content_type="application/json")
        self.assertEqual(response.status_code, 201)
        movies = IMDB.objects.all()
        self.assertEqual(len(movies), 3)

    def test_put_movie_for_admin(self):
        """
        This test method will test the PUT request for Admin to edit one movie whose details are given in the payload.
        """
        payload = {"popularity": 88.0,

                   "director": "George Lucas",
                   "name": "MIB"}
        payload = json.dumps(payload, indent=4)
        response = self.client.generic('PUT', self.admin_url, data=payload, **self.admin_auth_headers,
                                       content_type="application/json")
        self.assertEqual(response.status_code, 200)
        movie = IMDB.objects.get(name='MIB')
        self.assertEqual(movie.director, "George Lucas")

    def test_delete_movie_for_admin(self):
        """
        This test method will test the DELETE request for Admin to delete one movie whose details are given in the payload.
        """
        payload = {"name": "MIB"}
        payload = json.dumps(payload, indent=4)
        response = self.client.generic('DELETE', self.admin_url, data=payload, **self.admin_auth_headers,
                                       content_type="application/json")
        self.assertEqual(response.status_code, 200)
        movies = IMDB.objects.all()
        self.assertEqual(len(movies), 1)

    def test_post_movie_for_user(self):
        """
        This test method will test the POST request for User for one movie whose details are given in the payload. But,
        the request will not be completed as Users are not allowed to POST data.
        """

        payload = {"popularity": 88.0,

                   "director": "George Lucas",
                   "genre": [
                       "Action",
                       " Adventure",
                       " Fantasy",
                       " Sci-Fi"
                   ],
                   "imdb_score": 8.8,
                   "name": "Star Wars"}
        payload = json.dumps(payload, indent=4)
        response = self.client.generic('POST', self.user_url, data=payload, **self.user_auth_headers,
                                       content_type="application/json")
        self.assertEqual(response.status_code, 405)

    def test_put_movie_for_user(self):
        """
        This test method will test the PUT request for User to edit one movie whose details are given in the payload. But,
        the request will not be completed as Users are not allowed to PUT data.
        """

        payload = {"popularity": 88.0,
                   "director": "George Lucas",
                   "name": "MIB"}
        payload = json.dumps(payload, indent=4)
        response = self.client.generic('PUT', self.user_url, data=payload, **self.user_auth_headers,
                                       content_type="application/json")
        self.assertEqual(response.status_code, 405)

    def test_delete_movie_for_user(self):
        """
        This test method will test the DELETE request for User to delete one movie whose details are given in the payload.
        But,the request will not be completed as Users are not allowed to PUT data.
        """

        payload = {"name": "MIB"}
        payload = json.dumps(payload, indent=4)
        response = self.client.generic('DELETE', self.user_url, data=payload, **self.user_auth_headers,
                                       content_type="application/json")
        self.assertEqual(response.status_code, 405)
