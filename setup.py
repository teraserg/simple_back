from setuptools import setup, find_packages

setup(
    name='simple_back',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'aiohttp==3.5.4',
        'aiohttp-swagger==1.0.5',
        'gunicorn==19.9.0',
        'aiohttp_swagger'
    ],

    extras_require={
        'dev': [
        ]
    }
)
