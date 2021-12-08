# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-job is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

from storm_commons.records.base import BaseSQLAlchemyModelAPI
from invenio_records.systemfields import SystemFieldsMixin, ModelField

from .model import ExecutionJobModel


class ExecutionJob(BaseSQLAlchemyModelAPI, SystemFieldsMixin):
    """Execution model API"""

    model_cls = ExecutionJobModel
    """SQLAlchemy model class defining which table stores the records."""

    #
    # Creator
    #
    user = ModelField()
    user_id = ModelField()

    #
    # Associated project
    #
    project = ModelField()
    project_id = ModelField()

    #
    # Used pipeline
    #
    pipeline = ModelField()
    pipeline_id = ModelField()

    # General status
    status = ModelField()


__all__ = "ExecutionJob"
