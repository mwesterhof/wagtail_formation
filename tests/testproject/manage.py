#!/usr/bin/env python
import os
import sys
from os.path import abspath, dirname

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "testproject.settings.dev")

    root_path = dirname(dirname(dirname(abspath(__file__))))
    sys.path.append(root_path)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
