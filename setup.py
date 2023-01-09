from setuptools import setup

setup(
    name='netbox_templater',
    version='0.1.0',
    py_modules=['netbox_templater'],
    install_requires=[
        'Click',
        'Jinja2',
        'colorama',
        'os',
    ],
    entry_points={
        'console_scripts': [
            'netbox_templater = netbox_templater:cli',
        ],
    },
)