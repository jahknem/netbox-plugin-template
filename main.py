from jinja2 import Environment, FileSystemLoader
import click
from colorama import Fore, Back, Style
from shutil import rmtree
import os


@click.group()
def cli():
    pass

@cli.command()
@click.option('--name', prompt='Your name', help='The person to greet.')
def hello(name):
    click.echo('Hello %s!' % name)

@cli.command()
@click.option('--directory', help='The directory in which the new project should be placed')
@click.option('--plugin_name', prompt='Plugin Name', help='The name of the plugin.')
@click.option('--netbox_version', prompt='Netbox Version', help='The version of Netbox the plugin is compatible with.')
@click.option('--author_name', prompt='Author Name', help='The name of the author of the plugin.')
@click.option('--author_email', prompt='Author Email', help='The email of the author of the plugin.')
@click.option('--version', prompt='Version', help='The version of the plugin.')
@click.option('--plugin_url', prompt='Plugin URL', help='The URL of the plugin.')
@click.option('--git_plugin_url', prompt='Git Plugin URL', help='The URL of the git repository of the plugin.')
@click.option('--plugin_description', prompt='Plugin Description', help='The description of the plugin.')
def build(directory, plugin_name, netbox_version, author_name, author_email, version, plugin_url, git_plugin_url, plugin_description):
    """
    This function creates the plugin directory, and then creates the files in the plugin directory using the templates in the templates directory.
    :param directory: The directory where the plugin will be created. If no directory is specified, the plugin will be created in the current directory.
    :param plugin_name: The name of the plugin.
    :param netbox_version: The version of NetBox that the plugin is compatible with.
    :param author_name: The name of the author of the plugin.
    :param author_email: The author's email address.
    :param version: The version of the plugin.
    :param plugin_url: The URL of the plugin.
    :param git_plugin_url: The URL of the plugin's Git repository.
    :param plugin_description: A description of the plugin.
    """
    env = Environment(loader=FileSystemLoader('templates/'))
    if not directory:
        directory = '.'
    path = directory + "/" + plugin_name
    class_name = plugin_name.replace("_", " ").title().replace(" ", "")
    if not os.path.exists(path):
        os.mkdir(path)
    for template in env.list_templates():
        filename_template = env.from_string(path + "/" + template)
        filename = filename_template.render(plugin_name=plugin_name, netbox_version=netbox_version, author_name=author_name, author_email=author_email, version=version, plugin_url=plugin_url, git_plugin_url=git_plugin_url, plugin_description=plugin_description, class_name=class_name)
        print(Fore.GREEN + "Creating: " + filename)
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        template = env.get_template(template)
        output = template.render(plugin_name=plugin_name, netbox_version=netbox_version, author_name=author_name, author_email=author_email, version=version, plugin_url=plugin_url, git_plugin_url=git_plugin_url, plugin_description=plugin_description, class_name=class_name)
        with open(filename, "w") as f:
            f.write(output)

    if directory is '.':
        print(Fore.GREEN + "Plugin created in current directory. Deleting the template files...")
        template_dir = os.path.dirname(os.path.abspath(__file__)) + "/templates"
        rmtree(template_dir)
        os.remove(os.path.dirname(os.path.abspath(__file__)) + "/main.py")
        os.remove(os.path.dirname(os.path.abspath(__file__)) + "/requirements.txt")
        # Rename the current Dir to the plugin name
        current_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(current_dir)
        os.rename(current_dir, parent_dir + "/" + plugin_name)



if __name__ == '__main__':
    cli()