
#--------------------------------------------------------------------
#Setup code for splittimer module

#Language   : Python3
#Input      : NA
#Output     : NA
#Author     : Surja Sanyal
#Mail       : hi.surja06@gmail.com
#Created    : 16 JUN 2021
#Modified   : 16 JUN 2021
#--------------------------------------------------------------------


from setuptools import setup

setup(
    name='splittimer',
    version='1.0',    
    description='A splittimer Python package',
    url='https://github.com/Surja-Sanyal/Python3-Tools/splittimer',
    author='Surja Sanyal',
    author_email='hi.surja06@gmail.com',
    license='BSD 2-clause',
    packages=['splittimer'],
    install_requires=['atexit',
                      'datetime',                     
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3',
    ],
)

