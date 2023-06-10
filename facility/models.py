from django.db import models
class Region(models.Model):
    name = models.CharField(max_length=100)
    sub_county = models.CharField(max_length=100)

class District(models.Model):
    name = models.CharField(max_length=100)
    map_code = models.CharField(max_length=100)
    region_id = models.ForeignKey(Region,on_delete=models.CASCADE) 
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return self.name
    class Meta:
        ordering = ('name',)

class HOD(models.Model):
    name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    district_id = models.ForeignKey(District,on_delete=models.CASCADE)

class Facility(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=5)
    phone = models.CharField(max_length=10)
    fax = models.CharField(max_length=10)
    website = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=100) 
    hod_id = models.ForeignKey(HOD,on_delete=models.CASCADE)
    district_id = models.ForeignKey(District,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return self.name
    class Meta:
        ordering = ('name',)


