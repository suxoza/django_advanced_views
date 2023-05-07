from django.db import models
from django.contrib.auth.models import User

User._meta.get_field("email")._unique = True


class Poll(models.Model):
    question = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self) -> str:
        return str(self.question)


class Choice(models.Model):
    poll = models.ForeignKey(Poll, related_name="choices", on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(self.choice_text)


class Vote(models.Model):
    choice = models.ForeignKey(Choice, related_name="votes", on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    voted_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("poll", "voted_by")
