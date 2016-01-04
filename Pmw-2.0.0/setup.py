#!/usr/bin/env python
# setup.py
from distutils.core import setup
import sys
if sys.version_info[0]<3:
    version='2.0.0' # really '1.3.3'
    packages=['Pmw', 'Pmw.Pmw_1_3_3', 'Pmw.Pmw_1_3_3.lib',]
    package_data={'Pmw': ['Pmw_1_3_3/lib/Pmw.def',
                        'Pmw_1_3_3/doc/*',
                        'Pmw_1_3_3/contrib/*',
                        'Pmw_1_3_3/demos/*',
                        'Pmw_1_3_3/tests/*',
                            'Pmw_1_3_3/bin/*',
                        ]
                    }
    development_status = 'Beta'
else:
    version='2.0.0'
    packages=['Pmw', 'Pmw.Pmw_2_0_0', 'Pmw.Pmw_2_0_0.lib',]
    package_data={'Pmw': ['Pmw_2_0_0/lib/Pmw.def',
                            'Pmw_2_0_0/doc/*',
                            'Pmw_2_0_0/contrib/*',
                            'Pmw_2_0_0/demos/*',
                            'Pmw_2_0_0/tests/*',
                            'Pmw_2_0_0/bin/*',
                            ],
                    }
    development_status = 'Alpha'


setup(name="Pmw",
      version= version,
      description = 'Python Mega Widgets',
      author="Telstra Corporation Limited, Australia",
      author_email="",
      url='http://pmw.sourceforge.net/',

      package_dir = { "Pmw":"Pmw"},

      packages=packages,

      package_data=package_data,

      license='BSD',
      long_description='''Pmw is a toolkit for building high-level compound widgets, or megawidgets,
    constructed using other widgets as component parts. It promotes consistent look and feel within
     and between graphical applications, is highly configurable to your needs and is easy to use.''',
      classifiers = [
          'Development Status :: '+development_status,
          'Environment :: Console',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'License :: BSD',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Topic :: GUI',
          ],
     )
