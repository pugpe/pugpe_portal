# -*- coding:utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.encoding import smart_unicode


class Location(models.Model):
    class Meta:
        verbose_name = u'Local'
        verbose_name_plural = u'Locais'

    description = models.CharField(u'Descrição', max_length=100)

    street = models.CharField(u'Rua', max_length=255)
    number = models.CharField(u'Número', max_length='15')
    district = models.CharField(u'Bairro', max_length='255')
    postal_code = models.CharField(u'CEP', max_length='50')
    city = models.CharField(u'Cidade', max_length=50)
    state = models.CharField(u'Estado', max_length='50')
    country = models.CharField(u'País', max_length='50')

    reference = models.CharField(u'Referência', max_length=100)

    map = models.URLField(
        u'Mapa', max_length=255, null=True, blank=True,
        help_text=u'Caso preenchido, sobrescreve o mapa gerado '
        u'automaticamente',
    )

    def __unicode__(self):
        return self.description

    @property
    def address(self):
        address = (self.street, self.number, self.district)
        return u'{0} nº{1} {2}'.format(*address)

    def get_map(self):
        if self.map:
            return self.map

        base_url = 'http://maps.google.com.br/maps?q={0}'

        qs = u'{0},{1},{2},{3},{4}'
        qs = qs.format(
            self.street, self.number, self.district, self.city, self.state,
        )

        return base_url.format(qs)


class EventLecture(models.Model):
    class Meta:
        verbose_name = u'Palestra do Evento'
        verbose_name_plural = u'Palestras do Evento'

    event = models.ForeignKey('event_generator.Event', verbose_name=u'Evento')
    lecture = models.ForeignKey('palestra.Lecture', verbose_name=u'Palestra')
    start = models.TimeField(u'Início')
    end = models.TimeField(u'Fim')

    def __unicode__(self):
        return smart_unicode(self.lecture)


class Event(models.Model):
    class Meta:
        verbose_name = u'Evento'
        verbose_name_plural = u'Eventos'

    description = models.CharField(u'Descrição', max_length=100)
    full_description = models.TextField(u'Descrição Completa')

    date = models.DateTimeField(u'Data')
    location = models.ForeignKey(
        'event_generator.Location', verbose_name=u'Local',
    )
    image = models.ImageField(upload_to='uploads/events')

    slug = models.SlugField()

    def __unicode__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('event', kwargs={'slug': self.slug})
