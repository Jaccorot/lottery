from django.db import models


class Num3D(models.Model):
    """the basic numbers"""
    turn = models.IntegerField(primary_key=True)
    num1 = models.IntegerField()
    num2 = models.IntegerField()
    num3 = models.IntegerField()

    def __unicode__(self):
        return u'%d %d %d' % (self.num1, self.num2, self.num3)

    class Meta:
        ordering = ['-turn']
