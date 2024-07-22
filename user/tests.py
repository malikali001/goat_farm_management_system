from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse


class CustomUserViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user_password = 'testpassword123'
        self.user = get_user_model().objects.create_user(
            email='testuser@example.com',
            password=self.user_password,
            first_name='Test',
            last_name='User'
        )

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_logout_view(self):
        self.client.login(email=self.user.email, password=self.user_password)
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 405)

    def test_user_list_view(self):
        self.client.login(email=self.user.email, password=self.user_password)
        response = self.client.get(reverse('user_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/list.html')
        self.assertContains(response, self.user.email)

    def test_user_detail_view(self):
        self.client.login(email=self.user.email, password=self.user_password)
        response = self.client.get(reverse('user_detail', args=[self.user.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/detail.html')
        self.assertContains(response, self.user.email)

    def test_user_create_view(self):
        self.client.login(email=self.user.email, password=self.user_password)
        response = self.client.get(reverse('user_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/add.html')

    def test_user_update_view(self):
        self.client.login(email=self.user.email, password=self.user_password)
        response = self.client.get(reverse('user_update', args=[self.user.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/update.html')

    def test_user_delete_view(self):
        self.client.login(email=self.user.email, password=self.user_password)
        response = self.client.get(reverse('user_delete', args=[self.user.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/confirm_delete.html')
