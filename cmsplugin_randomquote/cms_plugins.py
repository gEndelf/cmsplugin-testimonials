from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from models import Quote, QuoteSettings


class QuotePlugin(CMSPluginBase):
    """This plugin randomly renders a quote from the database."""
    model = QuoteSettings
    name = _('Quote')
    render_template = 'cmsplugin_randomquote/quote.html'

    def render(self, context, instance, placeholder):
        _quotes = Quote.objects.order_by('?')

        if _quotes and self.model.SINGLE_RANDOM == instance.display_mode:
            _quotes = [_quotes[0]]

        context['quotes'] = _quotes
        context['display_mode'] = instance.display_mode
        return context

plugin_pool.register_plugin(QuotePlugin)
