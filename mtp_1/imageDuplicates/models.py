import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

# class Question(models.Model):
#     question_text = models.URLField(max_length=200,unique=True)
#     link=models.URLField(max_length=200)
#     # pub_date=models.DateField(default=2222-2-22)
#     def __str__(self):
#         return self.question_text
#     # def was_published_recently(self):
#     #     return self.pub_date >= timezone.now()-datetime.timedelta(days=1)    

# class Choice(models.Model):
#     question=models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.URLField(max_length=200)
#     votes = models.IntegerField(default=0)
#     types =models.URLField()
#     def __str__(self):
#         return self.choice_text

class Entity_hi(models.Model):
    entityId = models.BigIntegerField(db_column='entityId', primary_key=True, editable=False)  # Field name made lowercase.
    entityName = models.CharField(db_column='entityName', max_length=1000)  # Field name made lowercase.
    class Meta:
        managed=False
        db_table='Entity_hi'

class surfaceNames_hi(models.Model):
    surfaceNamesId = models.BigIntegerField(db_column='surfaceNamesId', primary_key=True)  # Field name made lowercase.
    surfaceName = models.CharField(db_column='surfaceName', max_length=750)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'surfaceNames_hi'

class entitySurfaceNames_hi(models.Model):
    SNo=models.BigIntegerField(db_column='SNo',primary_key=True)
    entityId = models.ForeignKey(Entity_hi,models.DO_NOTHING,db_column='entityId')
    surfaceNamesId = models.ForeignKey(surfaceNames_hi,models.DO_NOTHING,db_column='surfaceNamesId')
    frequency = models.BigIntegerField(blank=True, null=True)
    label = models.BigIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'entitySurfaceNames_hi2'
        unique_together = (('entityId', 'surfaceNamesId'),)
    
    def __str__(self):
        return '{}{}'.format(self.entityId,self.surfaceNamesId)


class Mention2_hi(models.Model):
    source = models.CharField(max_length=100, blank=True, null=True)
    dest = models.CharField(max_length=100, blank=True, null=True)
    SN = models.CharField(db_column='SN', max_length=145, blank=True, null=True)  # Field name made lowercase.
    context = models.CharField(max_length=250, blank=True, null=True)
    instanceId = models.OneToOneField('Mention_hi', models.DO_NOTHING, db_column='instanceId', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Mention2_hi'


class Mention_hi(models.Model):
    instanceid = models.BigIntegerField(db_column='instanceId', primary_key=True)  # Field name made lowercase.
    dest_eid = models.ForeignKey(Entity_hi,models.DO_NOTHING,db_column='dest_eid',related_name='des')
    mention_sid = models.ForeignKey(surfaceNames_hi,models.DO_NOTHING,db_column='mention_sid',related_name='men')
    source_eid = models.ForeignKey(Entity_hi,models.DO_NOTHING,db_column='source_eid',blank=True, null=True,related_name='sr')
    sentence = models.CharField(max_length=450, blank=True, null=True)
    link = models.CharField(max_length=105, blank=True, null=True)
    editDistance = models.BigIntegerField(db_column='editDistance', blank=True, null=True)  # Field name made lowercase.
    isCorrectSubstring = models.BigIntegerField(db_column='isCorrectSubString', blank=True, null=True)  # Field name made lowercase.
    isCorrectSuperstring = models.BigIntegerField(db_column='isCorrectSuperString', blank=True, null=True)  # Field name made lowercase.
    editsuggest = models.ForeignKey(surfaceNames_hi, models.DO_NOTHING, db_column='editSuggest', blank=True, null=True ,related_name='ed')  # Field name made lowercase.
    subsuggest = models.ForeignKey(surfaceNames_hi, models.DO_NOTHING, db_column='subSuggest', blank=True, null=True,related_name='sb')  # Field name made lowercase.
    supersuggest = models.ForeignKey(surfaceNames_hi, models.DO_NOTHING, db_column='superSuggest', blank=True, null=True,related_name='su')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Mention_hi'


