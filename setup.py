from setuptools import setup


setup(
    name='My flaskr',
    packages=['flaskr'],
    include_package_data=True,
    install_requires=[
        'flask',
        'pylint',
    ],
)