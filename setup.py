from setuptools import setup
import os

version = '1.1'

setup(name='foobar',
      version=version,
      include_package_data=True,
      packages=['foobar',],
      zip_safe=False,
      entry_points={
      'paste.app_factory':[
        "foobie=foobar.fooapp:mainfactory",
        ],
      'paste.filter_factory':[
        "upperware=foobar.fooapp:getmemiddleware",
                          ],
      },
      )
