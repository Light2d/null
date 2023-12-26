from django.db import models
from django.contrib.auth import get_user_model

class Direction(models.Model):
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='created_directions', verbose_name='Создатель')
    title = models.CharField(max_length=20, unique=True, verbose_name='Направление')

    def __str__(self):
        return self.title
    
class Event(models.Model):
    title = models.CharField(max_length=20, unique=True, verbose_name='Мероприятие')
    date = models.DateField(verbose_name='Дата мероприятия')
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE, verbose_name='Направление')

    def __str__(self):
        return self.title
    
class Participant(models.Model):
    event = models.ForeignKey('Event', on_delete=models.CASCADE, verbose_name='Мероприятие', related_name='participant_event')
    participant =  models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Пользователь', related_name='participant')
