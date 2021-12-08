from django.test import TestCase, Client		
from django.urls import resolve
from django.urls.base import reverse
from .models import *
from .views import *
from .forms import *

class TestPengumuman(TestCase):

    def test_harus_login(self):
        response = Client().get('/pengumuman/')
        self.assertEqual(response.status_code,302)
        response = Client().get('/pengumuman/pengumuman_saya/')
        self.assertEqual(response.status_code,302)
        response = Client().get('/pengumuman/buat_pengumuman')
        self.assertEqual(response.status_code,301)
        response = Client().get('/pengumuman/edit_pengumuman/1')
        self.assertEqual(response.status_code,302)
        response = Client().get('/pengumuman/hapus_pengumuman/1')
        self.assertEqual(response.status_code,302)
        