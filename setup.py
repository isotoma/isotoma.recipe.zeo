import sys
from setuptools import setup, find_packages

version = '2.0.2'

additional_install_requires = []

if sys.platform[:3].lower() == "win":
    additional_install_requires += ['nt_svcutils']


setup(
    name = "isotoma.recipe.zeo",
    version = version,
    description = "Custom version of isotoma.recipe.zeoserver",
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
#    packages = find_packages(),
    include_package_data = True,
#    package_dir = find_packages(exclude=['ez_setup']),
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
