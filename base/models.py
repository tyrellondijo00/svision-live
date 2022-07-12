import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
from audioop import maxpp
from turtle import title
from unicodedata import name
from django.db import models


# Create your models here.

MEMBER_CHOICES = [
    ("Management", "Management"),
    ("Associate", "Associate"),
]
class Client(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(null=True, blank=True, upload_to="images/") 

    def __str__(self):
        return self.name


class Member(models.Model):
    MANAGEMENT = "Management"
    ASSOCIATE = "Associate"

    MEMBER_CHOICES = [
    (MANAGEMENT, "Management"),
    (ASSOCIATE, "Associate"),
    ]

    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    bio = models.TextField()
    member_type = models.CharField(max_length=10, choices=MEMBER_CHOICES, default=MANAGEMENT,)
    photo = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.name

class Project(models.Model):

    COMPLETE = "Complete"
    ONGOING = "Ongoing"

    STATUS_CHOICES = [
    (COMPLETE, "Complete"),
    (ONGOING, "Ongoing"),
    ]

    title = models.CharField(max_length=200)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=ONGOING,)

    def __str__(self):
        return self.title

class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

class Testimony(models.Model):
    name = models.CharField(max_length=200)
    testimonial = models.TextField()
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name