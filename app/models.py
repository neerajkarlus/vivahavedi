from django.db import models
from datetime import datetime, date
community_choice = (
    ('Syro-Malabar','SYRO-MALABAR'),
    ('Latin', 'LATIN'),
    ('Malankara','MALANKARA'), 
)
fam_choice = (
    ('Low','LOW'),
    ('Middle', 'MIDDLE'),
    ('Upper Middle','UPPER MIDDLE'),
    ('Rich','RICH'), 
)
# Create your models here.
class Profile(models.Model):
    Name = models.CharField(max_length=50, blank=True, null=True)
    Address = models.CharField(max_length=200, blank=True, null=True)
    Age = models.CharField(max_length=5, blank=True, null=True)
    Sex = models.CharField(max_length=10, blank=True, null=True)
    Education = models.CharField(max_length=100, blank=True, null=True)
    Occupation = models.CharField(max_length=100, blank=True, null=True)
    Hight = models.CharField(max_length=5, blank=True, null=True)
    Weight = models.CharField(max_length=5, blank=True, null=True)
    Mobile_no = models.CharField(max_length=15, blank=True, null=True)
    Diocese = models.CharField(max_length=200, blank=True, null=True)
    Parish = models.CharField(max_length=200, blank=True, null=True)
    Community = models.CharField(max_length=50, choices=community_choice, default=community_choice[0][0])
    Town = models.CharField(max_length=50, blank=True, null=True)
    Family_Status = models.CharField(max_length=50, choices=fam_choice, default=fam_choice[0][0])
    Name_of_the_Parent = models.CharField(max_length=50, blank=True, null=True)
    Parent_mobile = models.CharField(max_length=15, blank=True, null=True)
    Partners_Requirements = models.CharField(max_length=500, blank=True, null=True)
    Contact_address = models.CharField(max_length=200, blank=True, null=True)
    Office_use = models.CharField(max_length=200, blank=True, null=True)
    Place = models.CharField(max_length=15, blank=True, null=True)
    date = models.DateField(default=datetime.now(), blank=True)


    def __str__(self):
        return self.Name