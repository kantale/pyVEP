
import sys

try:
	from setuptools import setup
except ImportError as e:
	print 'setuptools package is not installed'
	print 'On linux install with the following command:'
	print 'wget https://bootstrap.pypa.io/ez_setup.py -O - | sudo python '
	print 'For more info please visit: https://pypi.python.org/pypi/setuptools'
	sys.exit(1)


setup(name='pyVEP',
      version='0.0.1',
      description='Python interface to Variant Effect Predictor',
      url='https://github.com/kantale/pyVEP',
      author='Alexandros Kanterakis',
      author_email='alexandros.kanterakis@gmail.com',
      license='MIT',
      # https://pypi.python.org/pypi?%3Aaction=list_classifiers 
      classifiers=[
            'Topic :: Scientific/Engineering :: Bio-Informatics',
      ],
      install_requires=[
            'requests',
      ],
      # http://stackoverflow.com/questions/3472430/how-can-i-make-setuptools-install-a-package-thats-not-on-pypi 
      # dependency_links=['https://github.com/counsyl/hgvs/tarball/master#egg=pyhgvs-2.0.0',],
      packages=['pyVEP'],
)


