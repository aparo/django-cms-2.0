
def wrap_basetemplate(instance, placeholder, rendered_content, original_context):
    '''
    This plugin processor that apply a basetemplate.
    '''
    if instance._render_meta.text_enabled:   # Plugins embedded in Text should remain unchanged in order not to break output
            return rendered_content
    if instance.plugin_basetemplate or 'plugin_basetemplate' in original_context:
        from django.template.loader import render_to_string
        from django.template import Context
        template = instance.plugin_basetemplate if instance.plugin_basetemplate else original_context['plugin_basetemplate']
        c = Context({
            'content': rendered_content,
            'editable': instance.editable,
            'deletable': instance.deletable,
            'closable': instance.closable,
            'collapsable': instance.collapsable,
            'refreshable': instance.refreshable,
            'refresh_rate': instance.refresh_rate,
            'extraclass': instance.extraclass,
            })
        return render_to_string(template, c, context_instance=original_context)
    return rendered_content
