﻿#!/usr/bin/env python
"""
Command-line utility for administrative tasks.
"""

# coding: utf-8

import os
import sys

import dotenv
dotenv.read_dotenv()

if __name__ == "__main__":
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "mondja.settings"
    )

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
