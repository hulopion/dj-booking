from unittest.mock import patch

from django.template import Context, Template
from django.test import TestCase

TAG_MODULE = "booking.templatetags.booking_analytics"


def render_snippet():
    template = Template("{% load booking_analytics %}{% posthog_analytics %}")
    return template.render(Context({}))


class TestPosthogSnippet(TestCase):
    @patch(f"{TAG_MODULE}.BOOKING_POSTHOG_API_KEY", "phc_test_key")
    @patch(f"{TAG_MODULE}.BOOKING_POSTHOG_HOST", "https://eu.i.posthog.com")
    def test_snippet_renders_with_key(self):
        output = render_snippet()
        self.assertIn("posthog.init('phc_test_key'", output)
        self.assertIn("https://eu.i.posthog.com", output)

    @patch(f"{TAG_MODULE}.BOOKING_POSTHOG_API_KEY", None)
    def test_snippet_absent_without_key(self):
        output = render_snippet()
        self.assertNotIn("posthog.init", output)
