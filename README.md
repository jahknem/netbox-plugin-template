# NetBox Plugin Template

This is a template for creating a new plugin for [NetBox](https://github.com/netbox-community/netbox)
The template is based on the great [NetBox ACL Plugin](https://github.com/ryanmerolle/netbox-acls) by [ryanmerolle](https://github.com/ryanmerolle)

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

Have fun developing Netbox plugins!