import uuid

from django.db import models



class Event(models.Model):
    CHOICES = (
        ('MARRIAGE' , 'marriage'),
        ('BIRTHDAY' , 'birthday'),
        ('FUNERAL' , 'funeral'),
        ('ENGAREMENT','engagement'),
        ('BAPTISM', 'baptism'),
        ('HOUSE WARMING','house warming')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    image = models.FileField(upload_to='events/')
    event_type = models.CharField(max_length=255 ,choices=CHOICES)
    event_date = models.DateField(max_length=64)
    single_time = models.BooleanField(default=True)
    is_deleted=models.BooleanField(default=False)
    customer=models.ForeignKey("users.Customer",on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.title