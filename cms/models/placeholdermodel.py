from django.db import models
from django.utils.translation import ugettext_lazy as _


class Placeholder(models.Model):
    slot = models.CharField(_("slot"), max_length=50, db_index=True, editable=False)
    default_width = models.PositiveSmallIntegerField(_("width"), null=True, editable=False)
    noedit = models.BooleanField(default=False, verbose_name=_("disable frontend editing"), editable=False)
    
    def __unicode__(self):
        return self.slot
        
    class Meta:
        app_label = 'cms'

    def has_change_permission(self, request):
        opts = self._meta
        if request.user.is_superuser:
            return True
        return request.user.has_perm(opts.app_label + '.' + opts.get_change_permission())
    
    def render(self, context, width):
        from cms.utils.plugin import render_plugins_for_context
        if not 'request' in context:
            return '<!-- missing request -->'
        return render_plugins_for_context(self, context, width or self.default_width, self.noedit)