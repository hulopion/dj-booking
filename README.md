 Django Booking
 ===============

Django Booking is a Complete Django booking system.

Overview
===============

what you get:
   - A booking page which users can book appointments.
   - A dashboard which the admin can see the bookings and make actions

Requirements
============
Django Booking requires Django 3 or later.

Getting It
==========

Python package::

    $ pip install dj-booking

Installing it
=============

To enable `dj-booking` in your project you need to add it to `INSTALLED_APPS` in your projects
`settings.py` file::

    INSTALLED_APPS = (
        ...
        'booking',
        ...
    )

And include dj-booking to your URLs::
    
    from django.urls import path, include


    urlpatterns = (
        ...
        path("booking/", include("booking.urls")),
        ...
    )

Using It
========
    $ python manage.py migrate
    $ python manage.py runserver

then you can visit the pages::

- Booking page: http://localhost:8000/booking
- Admin page: http://localhost:8000/booking/admin

Configuration
=============
Add this vars to settings.py

  .. code-block:: python

    BOOKING_TITLE = "Your title"
    BOOKING_DESC = "Your description"
    BOOKING_BG = "img/booking_bg.jpg"

    BOOKING_SUCCESS_REDIRECT_URL = "Success redirect url"
    BOOKING_DISABLE_URL = "Redirect to this url if create booking is disable"

Analytics
=============
To send page analytics to PostHog, set your project API key. The snippet loads
only when the key is present, so no data is sent until you opt in.

  .. code-block:: python

    BOOKING_POSTHOG_API_KEY = "phc_your_project_api_key"
    BOOKING_POSTHOG_HOST = "https://us.i.posthog.com"

`BOOKING_POSTHOG_HOST` is optional and defaults to the US cloud. Set it to your region host.

The App
=======

- booking page

  ![booking page](https://github.com/foad-heidari/dj-booking/blob/main/docs/img/1.png?raw=true)

- Admin Page

  ![booking page](https://github.com/foad-heidari/dj-booking/blob/main/docs/img/2.png?raw=true)
  

Getting Involved
================
Open Source projects can always use more help. Fixing a problem, documenting a feature, adding
translation in your language. If you have some time to spare and like to help us, here are the places to do so:

- GitHub: https://github.com/foad-heidari/dj-booking

Documentation
=============
You can view the documentation online at:

- https://dj-booking.readthedocs.io
- https://pypi.org/project/dj-booking

Or you can look at the docs/ directory in the repository.

Support
=======

Django Booking is free and always will be. It is developed and maintained by developers in an Open Source manner.
Any support is welcome. You could help by writing documentation, pull-requests, report issues and/or translations.
