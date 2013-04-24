#!/bin/env python
#
# Copyright (c) 2013 Guilaume Delpierre <gde@llew.me>
# Copyright (c) 2013 Sylvain Mora <sylvain.mora@solevis.net>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer
# in this position and unchanged.
# 2. Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR(S) ``AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
# OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE AUTHOR(S) BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
# NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
# THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import os
from setuptools import setup

setup(
    name = "tonic",
    version = "0.1-dev",
    author = ["Guillaume Delpierre", "Sylvain Mora"],
    author_email = ["gde@llew.me", "sylvain.mora@solevis.net"],
    description = ("A simple GUI for pkgin."),
    license = "BSD",
    keywords = "package manager gui pkgin tonic pkgsrc",
    url = "http://tonic.pkgin.net/",
    packages = ['tonic', 'tonic.widgets'],
    scripts = ["./tonic-client"],
    install_requires = ["pykgin"],
    long_description = "Tonic is a GUI written with wxWidget to "\
                       "manage binary package from pkgsrc using "\
                       "pykgin as backend for pkgin",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: Unix",
        "Programming Language :: Python",
    ],
)
