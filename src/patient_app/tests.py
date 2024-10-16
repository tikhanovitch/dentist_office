from django.test import TestCase
from .models import User
# Create your tests here.


class TestUserModel(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='testuser',
            email='testuser@test.com',
            password='password123'
        )

    def test_user_creation(self):
        self.assertTrue(User.objects.exists())  # создание пользователя

    def test_username_field(self):
        self.assertEqual(self.user.username, 'testuser')  # проверка имени
                                                                 # пользователя

    def test_email_field(self):
        self.assertEqual(self.user.email, 'testuser@test.com')  # проверка email

    def test_password_field(self):
        self.assertIsNotNone(self.user.password)  # проверка пароля

