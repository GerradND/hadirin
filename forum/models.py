from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Thread(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)

    def __str__(self) -> str:
        return self.title


class ThreadReply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    main_thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name="replies")
    date_posted = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)

    def __str__(self) -> str:
        return f'Re: {self.main_thread.title}'
