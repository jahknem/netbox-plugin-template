# NetBox Plugin Template

This is a template for creating a new plugin for [NetBox](https://github.com/netbox-community/netbox)
The template is based on the devcontainer setup from [NetBox ACL Plugin](https://github.com/ryanmerolle/netbox-acls) by [ryanmerolle](https://github.com/ryanmerolle)

It uses devcontainers used by VSCode to create a devcontainer environment in which one can develop and test netbox plugins. To use it VSCode and Docker have to be installed. This Repo has been tested with Docker Desktop using WSL2 on Windows 10. Other Installations may or may not work.
To use this template, simply clone it, run the setup.py and run the main.py. This will create a new plugin structure with the name of your plugin in the current directory. The existing template files will be deleted during this process. 


```bash
git clone
cd netbox-plugin-template
pip3 install -r requirements.txt
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
