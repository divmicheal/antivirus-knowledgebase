import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'bitdefender-helpdpcs'
author = 'Documentation Team'
release = '1.0'

extensions = [
    'sphinx_sitemap',
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# VERY IMPORTANT FOR DEFAULT READTHEDOCS URL
html_baseurl = "https://bittdefender.readthedocs.io/en/latest/"
