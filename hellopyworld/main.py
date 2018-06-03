#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of hellopyworld.
# https://github.com/scorphus/hellopyworld

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2018, Pablo S Blum <scorphus@gmail.com>

import logging
import sys

from hellopyworld import __version__
from hellopyworld.argparser import ArgParser


def set_log_level(parsed_args):
    logger = logging.getLogger()
    if parsed_args.verbose:
        logger.setLevel(logging.INFO)
    else:
        logger.setLevel(logging.WARNING)


def run_action(action):
    print(f'Hello Python World! Action is: `{action}`!')


def main():
    parser = ArgParser()
    parsed_args = parser.parse()
    set_log_level(parsed_args)
    if parsed_args.help:
        parser.print_help()
    elif parsed_args.version:
        parser.print_version(__version__)
    elif parsed_args.action:
        if parsed_args.action in ('greet', 'salute', 'compliment'):
            run_action(parsed_args.action)
        else:
            logging.error('No such action: %s', parsed_args.action)
            parser.print_usage()
    else:
        parser.print_usage()
