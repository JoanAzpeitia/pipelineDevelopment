# Copyright (c) 2015 Shotgun Software Inc.
# 
# CONFIDENTIAL AND PROPRIETARY
# 
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit 
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your 
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights 
# not expressly granted therein are reserved by Shotgun Software Inc.

"""
Hook that controls various codec settings when submitting items for review
"""
import sgtk
import os
import sys

import nuke

HookBaseClass = sgtk.get_hook_baseclass()

class CodecSettings(HookBaseClass):

    def get_quicktime_settings(self, **kwargs):
        """
        Allows modifying default codec settings for Quicktime generation.
        Returns a dictionary of settings to be used for the Write Node that generates
        the Quicktime in Nuke.
        """
        settings = {}
        if sys.platform in ["darwin", "win32"]:
            settings["file_type"] = "mov"
            settings["colorspace"] = "Output - Rec.709"
            settings["meta_codec"] = "AVdn"
            settings["mov64_dnxhd_codec_profile"] = "DNxHD 422 10-bit 220Mbit"
        return settings