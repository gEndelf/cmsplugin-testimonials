from cms.models.pluginmodel import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Testimonial(models.Model):
    quote = models.TextField(_(u'Testimonial Text'))
    author = models.CharField(_(u'Author'), max_length=255)
    author_url = models.URLField(_(u'Author URL'), null=True, blank=True,
                                 default=None, max_length=255)

    def __unicode__(self):
        return '[%s] %s...' % (self.author, self.quote[:20])


class TestimonialSettings(CMSPlugin):
    SINGLE_RANDOM = 'RANDOM'
    CAROUSEL = 'CAROUSEL'
    DISPLAY_MODE_CHOICES = (
        (SINGLE_RANDOM, 'Single Random'),
        (CAROUSEL, 'Carousel'),
    )
    display_mode = models.CharField(max_length=8,
                                    choices=DISPLAY_MODE_CHOICES,
                                    default=SINGLE_RANDOM)
