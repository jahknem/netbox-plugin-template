# NetBox Plugin Template

This is a template for creating a new plugin for [NetBox](https://github.com/netbox-community/netbox)
THe template is based on the great [NetBox ACL Plugin](https://github.com/ryanmerolle/netbox-acls) by [ryanmerolle](https://github.com/ryanmerolle)

To use this template, simply clone it, fill out the plugin.yaml and run the makefile. This will create a new directory with the name of your plugin. 


```bash
git clone
cd netbox-plugin-template
python setup.py install
python main.py
```
It will then ask you for relevant variables and create a new directory with the name of your plugin. 

To use the directory in a devcontainer you must push it to a git provider of your choosing an and clone it into a devcontainer. Only then the devcontainer will automatically create a netbox instance in which you can develop, run and test your plugin.

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin <your git provider>
git push -u origin main
```

After you have done that you can clone the repository into a devcontainer and start developing.

```bash
git clone <your git provider>/<your username>/<your plugin name>
cd <your plugin name>
code .
```
If VSCode has the Remote-Containers extension installed it will automatically ask if it should create a devcontainer for you. If not you can install it by running the following command in the terminal.

```bash
code --install-extension ms-vscode-remote.remote-containers
```

Alternatively you can also start VSCode manually in the directory that as created. However this may cause errors due to permission issues. If such an error occures, you must manually delete the container and the volume. You have been warned!
```
cd <your plugin name>
code .
```

## Features

This template creates a new folder 
This plugin provides the following models:

- Access Lists
- Access List to Interface Assignment
- Access List Rules (abstract model bassis for other rules)
- Access List Standard Rules
- Access List Extended Rules

## Origin

Based on the NetBox plugin tutorial by [jeremystretch](https://github.com/jeremystretch):

- [demo repository](https://github.com/netbox-community/netbox-plugin-demo)
- [tutorial](https://github.com/netbox-community/netbox-plugin-tutorial)

All credit should go to Jeremy.  Thanks Jeremy!

This project just looks to build on top of this framework and model presented.

## Compatibility

This plugin was first developed using 3.2.5, and tested with all of 3.2.

| NetBox Version | Plugin Version |
|----------------|----------------|
|       3.2      |      1.0.1     |
|       3.3      |      1.1.0     |

## Installing

For adding to a NetBox Docker setup see
[the general instructions for using netbox-docker with plugins](https://github.com/netbox-community/netbox-docker/wiki/Using-Netbox-Plugins).

While this is still in development and not yet on pypi you can install with pip:

```bash
pip install git+https://github.com/ryanmerolle/netbox-acls.git@dev
```

or by adding to your `local_requirements.txt` or `plugin_requirements.txt` (netbox-docker):

```bash
git+https://github.com/ryanmerolle/netbox-acls.git@dev
```

Enable the plugin in `/opt/netbox/netbox/netbox/configuration.py`,
 or if you use netbox-docker, your `/configuration/plugins.py` file :

```python
PLUGINS = [
    'netbox_acls'
]

PLUGINS_CONFIG = {
    "netbox_acls": {},
}
```

## Screenshots

Access List - List View
![Access List - List View](docs/img/access_lists.png)

Access List (Type Extended) - Individual View
![Access List Type Extended - Individual View](docs/img/access_list_type_extended.png)

Access List (Type Standard) - Individual View
![Access List Type Standard - Individual View](docs/img/access_list_type_standard.png)

Extended Access List Rules - List View
![Extended Access List Rules - List View](docs/img/acl_extended_rules.png)

Standard Access List Rules - List View
![Standard Access List Rules - List View](docs/img/acl_standard_rules.png)

Access List Interface Assignments- List View
![Access List Interface Assignments- List View](docs/img/acl_interface_assignments.png)

Host (device, virtual_chassis, virtual_machine) Access Lists - New Card
![Host Access Lists - New Card](docs/img/acl_host_view.png)

Host Interface (vminterface interface) Access Lists - New Card
![Host Interface Access Lists - New Card](docs/img/access_list_type_standard.png)
