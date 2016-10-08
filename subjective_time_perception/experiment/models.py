from datetime import datetime
from datetime import timezone
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.db import models


class Experiment(models.Model):
    RHYTHMS = [
        ('perfect', _('Perfect')),
        ('above-average', _('Above average')),
        ('average', _('Average')),
        ('below-average', _('Below average')),
        ('poor', _('Poor'))]
    GENDERS = [
        ('female', _('Female')),
        ('male', _('Male')),
        ('other', _('Other'))]
    CONDITIONS = [
        ('well-rested', _('Well rested')),
        ('normal', _('Normal')),
        ('tired', _('Tired'))]
    POLARIZATIONS = [
        ('horizontal', _('Horizontal')),
        ('vertical', _('Vertical')),
        ('cross', _('Cross')),
        ('mixed', _('Mixed'))]

    location = models.CharField(max_length=50)
    experiment_start = models.DateTimeField(null=True)
    experiment_end = models.DateTimeField(null=True)
    polarization = models.CharField(max_length=15, choices=POLARIZATIONS)
    device = models.CharField(max_length=50)
    order = models.CharField(max_length=70, null=True)
    timeout = models.PositiveIntegerField(help_text=_('Microseconds'))
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField()
    rhythm = models.CharField(max_length=50, choices=RHYTHMS)
    gender = models.CharField(max_length=50, choices=GENDERS)
    condition = models.CharField(max_length=50, choices=CONDITIONS)

    white_start = models.DateTimeField(null=True)
    white_end = models.DateTimeField(null=True)
    blue_start = models.DateTimeField(null=True)
    blue_end = models.DateTimeField(null=True)
    red_start = models.DateTimeField(null=True)
    red_end = models.DateTimeField(null=True)

    @property
    def where(self):
        return self.location

    def add(**data):
        def make_datetime(string):
            return datetime.strptime(string, '%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=timezone.utc)

        date_of_experiment = [make_datetime(d.get('datetime')) for d in data.get('events') if d.get('action') == 'start' and d.get('message') == 'experiment']

        experiment, status = Experiment.objects.get_or_create(
            date=date_of_experiment,
            location=data.get('location'),
            polarization=data.get('polarization'),
            device=data.get('device'),
            first_name=data.get('first_name').title(),
            last_name=data.get('last_name').title(),
            timeout=data.get('timeout'),
            age=data.get('age'),
            gender=data.get('gender'),
            rhythm=data.get('rhythm'),
            condition=data.get('condition'))

        for event in data.get('events'):
            Event.objects.get_or_create(
                experiment=experiment,
                datetime=make_datetime(event.get('datetime')),
                action=event.get('action'),
                message=event.get('message'))

        for click in data.get('clicks'):
            Click.objects.get_or_create(
                experiment=experiment,
                datetime=make_datetime(click.get('datetime')),
                background=click.get('background'))
        return experiment


    def __str__(self):
        return '[{experiment_start}] {last_name}, {first_name}'.format(**self.__dict__)

    class Meta:
        ordering = ["-experiment_start"]
        verbose_name = _("Experiment")
        verbose_name_plural = _("Experiments")


class Click(models.Model):
    BACKGROUNDS = [
        ('white', _('White')),
        ('blue', _('Blue')),
        ('red', _('Red'))]
    experiment = models.ForeignKey(to='experiment.Experiment')
    datetime = models.DateTimeField()
    background = models.CharField(max_length=15, choices=BACKGROUNDS)

    def __str__(self):
        return '[{datetime}] clicked background {background}'.format(**self.__dict__)

    class Meta:
        ordering = ["datetime"]
        verbose_name = _("Click event")
        verbose_name_plural = _("Click events")


class Event(models.Model):
    ACTIONS = [
        ('start', _('Start')),
        ('end', _('End'))]
    experiment = models.ForeignKey(to='experiment.Experiment')
    datetime = models.DateTimeField()
    action = models.CharField(max_length=15, choices=ACTIONS)
    message = models.CharField(max_length=30)

    def __str__(self):
        return '[{datetime}] - {message} - {action}'.format(**self.__dict__)

    class Meta:
        ordering = ["datetime"]
        verbose_name = _("Event")
        verbose_name_plural = _("Events")
