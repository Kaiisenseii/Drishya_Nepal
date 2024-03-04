from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import DrishyaNepalUser, Notification, Otp
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse
from .models import DrishyaNepalUser

class RegisterClientViewTests(TestCase):
    def test_register_client_with_valid_data_and_file(self):
        # Open the test image file in binary mode
        with open('path/to/your/tests/test_data/test_image.jpg', 'rb') as image:
            # Create a SimpleUploadedFile object
            uploaded_image = SimpleUploadedFile(name='test_image.jpg', content=image.read(), content_type='image/jpeg')

            # Post request with the image file included
            response = self.client.post(reverse('register-client'), data={
                'email': 'client@example.com',
                'password': 'testpass123',
                'first_name': 'Client',
                'last_name': 'Test',
                'phone_number': '1234567890',
                'address': 'Test Address',
                'profile_picture': uploaded_image,  # Include the uploaded image in the POST data
            })

            self.assertEqual(DrishyaNepalUser.objects.count(), 1)
            self.assertTrue(DrishyaNepalUser.objects.filter(username='client@example.com').exists())
            user = DrishyaNepalUser.objects.get(username='client@example.com')
            # Ensure the file was uploaded successfully
            self.assertTrue(user.profile_pic, 'users/test_image.jpg')


class DrishyaNepalUserModelTest(TestCase):
    def test_user_creation(self):
        user = DrishyaNepalUser.objects.create_user(
            username="testuser", email="test@example.com", password="test12345",
            phone="123456789", address="Test Address"
        )
        self.assertEqual(user.email, "test@example.com")
        self.assertTrue(user.check_password("test12345"))
        self.assertEqual(user.phone, "123456789")
        self.assertEqual(user.address, "Test Address")

class NotificationModelTest(TestCase):
    def setUp(self):
        self.user = DrishyaNepalUser.objects.create_user(username="testuser", password="test12345")

    def test_notification_creation(self):
        notification = Notification.objects.create(user=self.user, message="Test Notification")
        self.assertEqual(notification.user, self.user)
        self.assertEqual(notification.message, "Test Notification")


class OtpModelTest(TestCase):
    def setUp(self):
        self.user = DrishyaNepalUser.objects.create_user(username="testuser", password="test12345")

    def test_otp_creation(self):
        otp_instance = Otp.objects.create(user=self.user, otp=123456)
        self.assertEqual(otp_instance.user, self.user)
        self.assertEqual(otp_instance.otp, 123456)


class LoginViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        DrishyaNepalUser.objects.create_user(username='testuser', email='user@example.com', password='password123')

    def test_login_with_valid_credentials(self):
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'password123'}, follow=True)
        # Check if the response redirected to the expected url
        self.assertRedirects(response, reverse('index'))  # 'index' to the name of home page's URL
        # Now, check if the user is authenticated
        user = response.context['user']
        self.assertTrue(user.is_authenticated)

class LogoutViewTests(TestCase):
    def setUp(self):
        self.user = DrishyaNepalUser.objects.create_user(username='testuser', email='user@example.com', password='password123')
        self.client.login(username='testuser', password='password123')

    def test_logout(self):
        response = self.client.get(reverse('logout'), follow=True)
        # Check if the response redirected to the expected url, e.g., login page
        self.assertRedirects(response, '/')  # Adjust to the correct URL for your login page
        # Check if the user is no longer authenticated
        self.assertFalse(response.wsgi_request.user.is_authenticated)
