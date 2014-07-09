#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Setup.py file built by William Minchin to allow use of weather as a console
script, installed on Windows machines running Python. July 8, 2014'''

''' weather utility downloaded from http://fungi.yuggoth.org/weather/ '''

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages
	
import weather
	
setup(
    name = "weather",
	version = weather.cli.weather_version,
	description = "Retrieve conditions and forecasts",
	packages = find_packages(),
	data_files=[('~/.weather',   ['weather/airports.txt',
						'weather/places.txt',
						'weather/stations.txt',
						'weather/zctas.txt',
						'weather/zones.txt',] ), ],
	entry_points={
        'console_scripts': [
            'weather = weather.cli:run',
        ],
    },
)