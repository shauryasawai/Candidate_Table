from django.db import models

class Alumni(models.Model):
    name = models.CharField(max_length=255)
    graduation_year = models.IntegerField()
    department = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    company_description = models.TextField()
    linkedin_profile = models.URLField()
    personal_email = models.EmailField()
    work_email = models.EmailField(blank=True, null=True)
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name
