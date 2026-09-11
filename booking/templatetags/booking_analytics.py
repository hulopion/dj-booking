from django import template

from booking.settings import BOOKING_POSTHOG_API_KEY, BOOKING_POSTHOG_HOST

register = template.Library()


@register.inclusion_tag('booking/posthog.html')
def posthog_analytics():
    """Render the PostHog snippet when the host sets an API key."""
    return {
        'posthog_api_key': BOOKING_POSTHOG_API_KEY,
        'posthog_host': BOOKING_POSTHOG_HOST,
    }
