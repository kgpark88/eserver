from django.db import models

class EnergyUsage(models.Model):
    b_name =  models.CharField('빌딩 이름', max_length=20)
    daq_time = models.DateTimeField('일시')
    wday = models.IntegerField('요일', blank=True, null=True)
    day_type = models.IntegerField('구분', blank=True, null=True)
    hour = models.IntegerField('시간', blank=True, null=True)	
    temp = models.FloatField('온도', blank=True, null=True)	
    rh = models.FloatField('습도', blank=True, null=True)	
    p_usage= models.FloatField('전기 사용량', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'energy_usage'
        unique_together = [['b_name', 'daq_time']]
        ordering = ['-daq_time']
        verbose_name = '에너지 사용량'
        verbose_name_plural = '에너지 사용량'
