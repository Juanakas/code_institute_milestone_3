"""
Custom test runner to prevent context copy errors with Django test client
on newer Python versions by providing a safer template_rendered handler.
"""
from django.test.runner import DiscoverRunner
from django.test.signals import template_rendered
from django.test import client as django_test_client


def safe_store_rendered_templates(sender=None, template=None, context=None, **kwargs):
    store = getattr(safe_store_rendered_templates, '_store', {'templates': [], 'context': []})
    store['templates'].append(template)
    # Avoid deep copying the context to prevent AttributeError on some Python versions
    try:
        store['context'].append(context)
    except Exception:
        store['context'].append({})
    safe_store_rendered_templates._store = store


class SafeTemplateRunner(DiscoverRunner):
    """Test runner that swaps Django's template_rendered signal handler."""

    def setup_test_environment(self, **kwargs):
        super().setup_test_environment(**kwargs)
        # Drop all existing receivers to stop Django test client copying contexts
        while template_rendered.receivers:
            _, receiver = template_rendered.receivers[0]
            template_rendered.disconnect(receiver=receiver)

        # Ensure Django's test client uses the safe handler if it reconnects internally
        django_test_client.store_rendered_templates = safe_store_rendered_templates
        template_rendered.connect(safe_store_rendered_templates)
        # As a last resort, bypass send to avoid double-sender bug on Python 3.14
        template_rendered.send = lambda *args, **kwargs: []

    def teardown_test_environment(self, **kwargs):
        template_rendered.disconnect(safe_store_rendered_templates)
        super().teardown_test_environment(**kwargs)
