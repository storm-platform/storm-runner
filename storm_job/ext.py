# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-job is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

"""Job schedule and management module for reproduce scientific research in the Storm Platform."""

from . import config

from .job.resources.config import ExecutionJobResourceConfig
from .job.resources.resource import ExecutionJobResource
from .job.services.config import ExecutionJobServiceConfig
from .job.services.service import ExecutionJobService


class StormJob(object):
    """storm-job extension."""

    def __init__(self, app=None):
        """Extension initialization."""
        if app:
            self.init_app(app)

    def init_app(self, app):
        """Flask application initialization."""
        self.init_config(app)
        self.init_services(app)
        self.init_resources(app)

        app.extensions["storm-job"] = self

    def init_config(self, app):
        """Initialize configuration."""
        for k in dir(config):
            if k.startswith("STORM_JOB_"):
                app.config.setdefault(k, getattr(config, k))

    def init_services(self, app):
        """Initialize the execution job services."""
        self.execution_job_service = ExecutionJobService(ExecutionJobServiceConfig)

    def init_resources(self, app):
        """Initialize the execution job resources."""
        self.execution_job_resource = ExecutionJobResource(
            ExecutionJobResourceConfig, self.execution_job_service
        )
