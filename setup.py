from setuptools import setup

setup(name='instapoem',
      version='0.1',
      description='Takes a text poem and turns it into an Instagram square PNG',
      url='http://github.com/kamiel79/instapoem',
      author='Kamiel Choi',
      author_email='kamiel@creativechoice.org',
      license='MIT',
      packages=['instapoem'],
      install_requires=['time','selenium','autoit','PIL','calendar','datetime','glob','os','sys','shutil'
      ],
      zip_safe=False)