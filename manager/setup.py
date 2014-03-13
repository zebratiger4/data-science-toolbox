from setuptools import setup
setup(
    name='dst',
    version='0.1.4',
    author='Jeroen Janssens',
    author_email='jeroen@jeroenjanssens.com',
    packages=['dst'],
    url='http://pypi.python.org/pypi/dst/',
    license='BSD',
    description='Start doing data science in minutes.',
    long_description=open('README.txt').read(),
    install_requires=[
        "ansible >= 1.5",
    ],
    entry_points={
        'console_scripts': ['dst = dst.dst:main']
    },
)
