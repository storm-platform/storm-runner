# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-runner is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

"""Storm Runner module for schedule and manage execution tasks in the Storm Platform."""

from .ext import StormRunner
from .version import __version__

__all__ = (
    "__version__",
    "StormRunner",
)
