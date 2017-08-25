try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'name': 'Docx Property Reassigner',
	'version': '0.1',
	'url': 'https://github.com/parnellj/docx_property_assigner',
	'download_url': 'https://github.com/parnellj/docx_property_assigner',
	'author': 'Justin Parnell',
	'author_email': 'parnell.justin@gmail.com',
	'maintainer': 'Justin Parnell',
	'maintainer_email': 'parnell.justin@gmail.com',
	'classifiers': [],
	'license': 'GNU GPL v3.0',
	'description': 'Reassigns the properties of Office documents according to specified parameters',
	'long_description': 'Reassigns the properties of Office documents according to specified parameters',
	'keywords': '',
	'install_requires': ['nose'],
	'packages': ['docx_property_assigner'],
	'scripts': []
}
	
setup(**config)
