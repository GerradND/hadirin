from django.forms import ModelForm
from .models import Thread, ThreadReply

class ThreadForm(ModelForm):
    class Meta:
        model = Thread
        fields = ['title', 'content']

class ThreadReplyForm(ModelForm):
    class Meta:
        model = ThreadReply
        fields = ['content']