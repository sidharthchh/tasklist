from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Task(models.Model):
    """
    Model for storing task
    """
    STATUS_CHOICE = ("TO DO", "DONE", "ARCHIVED")
    name = models.CharField(max_length=511)
    description = models.CharField(max_length=1023)
    owner = models.ForeignKey(User, related_name="owner")  # The user to whom the task belongs to
    status = models.CharField(max_length=31, choices=zip(STATUS_CHOICE, STATUS_CHOICE))
    actor = models.ForeignKey(User, related_name="actor", null=True, blank=True)  # The user who acted upon the task
    created_at = models.DateTimeField(default=timezone.now)
    closed_at = models.DateTimeField(null=True, blank=True)
