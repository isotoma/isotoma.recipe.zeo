import sys
from setuptools import setup, find_packages

version = '2.0.4'

additional_install_requires = []

if sys.platform[:3].lower() == "win":
    additional_install_requires += ['nt_svcutils']


setup(
    name = "isotoma.recipe.zeo",
    version = version,
    description = "Custom version of plone.recipe.zeoserver",
    long_description = open('README.txt').read() + '\n' +
                       open('CHANGES.txt').read(),
    license = "ZPL 2.1",
    keywords = "zope2 zeo zodb buildout",
    url='http://pypi.python.org/pypi/isotoma.recipe.zeo',
    classifiers=[
        "License :: OSI Approved :: Zope Public License",
        "Framework :: Buildout",
        "Framework :: Zope2",
        "Programming Language :: Python",
    ],
    include_package_data = True,
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages = ['isotoma', 'isotoma.recipe'],
    install_requires = [
        'zc.buildout',
        'setuptools',
        'zc.recipe.egg',
        'zope.mkzeoinstance',
        'ZODB3 >= 3.8',
        'ZopeUndo',
    ] + additional_install_requires,
    zip_safe=False,
    entry_points = {
        'zc.buildout': ['default = isotoma.recipe.zeo.recipe:Recipe'],
    },
    )
