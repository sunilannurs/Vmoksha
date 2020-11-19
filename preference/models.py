from django.db import models

# Create your models here.

class PCountry(models.Model):
    country_id = models.AutoField(primary_key=True)
    shortname = models.CharField(unique=True, max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'p_country'

class PState(models.Model):
    state_id = models.AutoField(primary_key=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    country = models.ForeignKey(PCountry, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'p_state'


class PCity(models.Model):
    city_id = models.AutoField(primary_key=True)
    country = models.ForeignKey('PCountry', models.DO_NOTHING, blank=True, null=True)
    state = models.ForeignKey('PState', models.DO_NOTHING, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'p_city'

class PLocation(models.Model):
    location_id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    state = models.ForeignKey('PState', models.DO_NOTHING, blank=True, null=True)
    country = models.ForeignKey(PCountry, models.DO_NOTHING, blank=True, null=True)
    city = models.ForeignKey(PCity, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'p_location'


class MyPreference(models.Model):
    id = models.IntegerField(primary_key=True)
    country = models.CharField(max_length=45, blank=True, null=True)
    city = models.CharField(db_column='City', max_length=45, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'my_preference'


