from django.test import TestCase, Client		
from django.urls import resolve
from django.urls.base import reverse
from .models import *
from .views import *
from .forms import *

class TestPengumuman(TestCase):

    def test_harus_login(self):
        response = Client().get('/auth/login')
        self.assertEquals(response.status_code, 200)
        