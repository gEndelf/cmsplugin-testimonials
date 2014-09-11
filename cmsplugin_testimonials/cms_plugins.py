from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from models import Testimonial, TestimonialSettings


class TestimonialPlugin(CMSPluginBase):
    """
    This plugin renders a quote/testimonials from DB in 2 modes:
    - single random
    - all with carousel
    """

    model = TestimonialSettings
    name = _('Testimonial')
    render_template = 'cmsplugin_testimonials/quote.html'

    def render(self, context, instance, placeholder):
        _quotes = Testimonial.objects.order_by('?')

        if _quotes and self.model.SINGLE_RANDOM == instance.display_mode:
            _quotes = [_quotes[0]]

        context['quotes'] = _quotes
        context['display_mode'] = instance.display_mode
        return context

plugin_pool.register_plugin(TestimonialPlugin)
