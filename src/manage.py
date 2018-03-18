#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    if os.getenv('STAGING') == '1':
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gallery.settings.staging")
    elif os.getenv('PROD') == '1':
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gallery.settings.production")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gallery.settings.dev")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
