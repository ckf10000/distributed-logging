# -*- coding: utf-8 -*-
"""
# ---------------------------------------------------------------------------------------------------------
# ProjectName:  distributed-logging
# FileName:     test_yaml.py
# Description:  TODO
# Author:       mfkifhss2023
# CreateDate:   2024/07/23
# Copyright ©2011-2024. Hunan xxxxxxx Company limited. All rights reserved.
# ---------------------------------------------------------------------------------------------------------
"""

from distributed_logging.parse_yaml import ProjectConfig

config = ProjectConfig().get_object()

print(getattr(config, "logging"))
