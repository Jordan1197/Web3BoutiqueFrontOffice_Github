from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    nom = models.TextField(db_column='LastName', blank=True, null=True)  # Field name made lowercase.
    prenom = models.TextField(db_column='FirstName', blank=True, null=True)  # Field name made lowercase.
    email = models.TextField(db_column='Email', blank=True, null=True)  # Field name made lowercase.
    password = models.TextField(db_column='Password', blank=True, null=True)  # Field name made lowercase.
    addressid = models.IntegerField(db_column='AddressId',blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    createdby = models.TextField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    lastupdateddate = models.DateTimeField(db_column='LastUpdatedDate', blank=True, null=True)  # Field name made lowercase.
    lastupdatedby = models.TextField(db_column='LastUpdatedBy', blank=True, null=True)  # Field name made lowercase.
    deleteddate = models.DateTimeField(db_column='DeletedDate', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.TextField(db_column='DeletedBy', blank=True, null=True)  # Field name made lowercase.