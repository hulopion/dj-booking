from django.conf import settings

PAGINATION = getattr(settings, 'DJ_BOOKING_PAGINATION', 10)

BOOKING_SUCCESS_REDIRECT_URL = getattr(settings, 'BOOKING_SUCCESS_REDIRECT_URL', None)

BOOKING_DISABLE_URL = getattr(settings, 'BOOKING_DISABLE_URL', "/")

BOOKING_BG = getattr(settings, 'BOOKING_BG', "img/booking_bg.jpg")

BOOKING_TITLE = getattr(settings, 'BOOKING_TITLE', "Booking")

BOOKING_DESC = getattr(settings, 'BOOKING_DESC', "Make your booking easy and fast with us.")

BOOKING_POSTHOG_API_KEY = getattr(settings, 'BOOKING_POSTHOG_API_KEY', None)

BOOKING_POSTHOG_HOST = getattr(settings, 'BOOKING_POSTHOG_HOST', "https://us.i.posthog.com")
