# NetBox "{{plugin_name}}"

## Features

The features the plugin provides should be listed here.

## Origin

Based on the NetBox plugin tutorial by [jeremystretch](https://github.com/jeremystretch):

- [demo repository](https://github.com/netbox-community/netbox-plugin-demo)
- [tutorial](https://github.com/netbox-community/netbox-plugin-tutorial)

All credit should go to Jeremy.  Thanks Jeremy!

This project just looks to build on top of this framework and model presented.

## Compatibility

| NetBox Version | Plugin Version |
|----------------|----------------|
|       {{netbox_version}}      |      {{version}}     |

## Installing

For adding to a NetBox Docker setup see
[the general instructions for using netbox-docker with plugins](https://github.com/netbox-community/netbox-docker/wiki/Using-Netbox-Plugins).

While this is still in development and not yet on pypi you can install with pip:

```bash
pip install git+{{git_url}}
```

or by adding to your `local_requirements.txt` or `plugin_requirements.txt` (netbox-docker):

```bash
git+{{git_url}}
```

Enable the plugin in `/opt/netbox/netbox/netbox/configuration.py`,
 or if you use netbox-docker, your `/configuration/plugins.py` file :

```python
PLUGINS = [
    '{{plugin_name}}}'
]

PLUGINS_CONFIG = {
    "{{plugin_name}}": {},
}
```
