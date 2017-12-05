from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst')) as f:
    long_description = f.read()


def get_requirements(filename):
    with open(filename) as f:
        return f.read().splitlines()


setup(name='wsceleryactivity',
      version='0.1.0',
      # Autor detauls
      author='Eugene Zyatev',
      author_email='eu@zyatev.ru',
      # Project details
      description='Real time celery active tasks monitoring using websockets',
      long_description=long_description,
      url='https://github.com/ezyatev/wsceleryactivity',
      license='MIT',

      classifiers=[
          # Project maturity
          'Development Status :: 3 - Alpha',

          # Intended audience
          'Intended Audience :: Developers',
          'Topic :: System :: Distributed Computing',

          # License
          'License :: OSI Approved :: MIT License',

          # Supported python versions
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: Implementation :: CPython',
          'Operating System :: OS Independent',
      ],
      keywords=['celery', 'websocket', 'monitoring'],
      packages=find_packages(exclude=['tests', 'tests.*']),
      install_requires=get_requirements('requirements.txt'),
      entry_points={
          'console_scripts': [
              'wsceleryactivity = wsceleryactivity.__main__:main',
          ],
          'celery.commands': [
              'wsceleryactivity = wsceleryactivity.command:WsCeleryActivityCommand',
          ]
      })
