
def wrap_basetemplate(instance, placeholder, rendered_content, original_context):
    '''
    This plugin processor that apply a basetemplate.
    '''
    if instance._render_meta.text_enabled:   # Plugins embedded in Text should remain unchanged in order not to break output
            return rendered_content
    template = None
    if getattr(instance, "plugin_basetemplate", None):
        template = instance.plugin_basetemplate
    elif 'plugin_basetemplate' in original_context:
        template = original_context['plugin_basetemplate']
    if template:
        from django.template.loader import render_to_string
        from django.template import Context
        data = {'content': rendered_content}
        for field in ['editable', 'deletable', 'closable', 
            'collapsable', 'refreshable', 'refresh_rate', 
            'extraclass']:
            if hasattr(instance, field):
                data[field] = getattr(instance, field)
        c = Context(data)
        return render_to_string(template, c, context_instance=original_context)
    return rendered_content
