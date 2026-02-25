import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'Bitdefender Account Guide'
author = 'Support Documentation'
release = '1.0'

extensions = [
    'sphinx_sitemap',
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# IMPORTANT: Change if using custom domain
html_baseurl = "https://yourdomain.com/"

# If using default readthedocs domain use:
# html_baseurl = "https://bittdefender.readthedocs.io/en/latest/"
