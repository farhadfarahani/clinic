from django.db import models
from django.core.validators import RegexValidator
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class Doctor(models.Model):
    name = models.CharField(max_length=50)
    expertise = models.CharField(max_length=100)
    visiting_days = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    address = models.TextField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="شماره تلفن باید در فرمت صحیح باشد.")
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('doctor_detail', args=[self.pk])


class ActiveCommentsManager(models.Manager):
    def get_queryset(self):
        return super(ActiveCommentsManager, self).get_queryset().filter(active=True)


class Comment(models.Model):
    DOCTOR_STARS = [
        ('1', _('Very Bad')),
        ('2', _('Bad')),
        ('3', _('Normal')),
        ('4', _('Good')),
        ('5', _('Perfect')),
    ]
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='comments',)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments', verbose_name=_('Comment author'))
    body = models.TextField(verbose_name=_('Write your comment text'))
    stars = models.CharField(max_length=10, choices=DOCTOR_STARS, verbose_name=_('Your score with this Doctor'))
    datetime_created = models.DateTimeField(_('Date time of creation'), default=timezone.now)
    datetime_modified = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    objects = models.Manager()
    active_comments_manager = ActiveCommentsManager()

    def get_absolute_url(self):
        return reverse('doctor_detail', args=[self.doctor.id])
