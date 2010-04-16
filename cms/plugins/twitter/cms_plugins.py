from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugins.twitter.models import TwitterRecentEntries
from cms.plugin_pool import plugin_pool

class TwitterRecentEntriesPlugin(CMSPluginBase):
    model = TwitterRecentEntries
    name = _("Twitter")
    render_template = "cms/plugins/twitter_recent_entries.html"
    
    def render(self, context, instance, placeholder):
        context.update({
            'title':_("Twitter"),
            'object': instance,
        })
        return context
    
plugin_pool.register_plugin(TwitterRecentEntriesPlugin)