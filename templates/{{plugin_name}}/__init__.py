"""
Define the NetBox Plugin
"""

from extras.plugins import PluginConfig


class {{class_name}}Config(PluginConfig):
    name = "{{plugin_name}}"
    verbose_name = "{{plugin_name}}"
    description = "{{description}}"
    version = "1.0.0"
    base_url = "access-lists"


config = {{class_name}}Config
