
#--------------------------------------------------------------------
#Setup code for timer module

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
    name='timer',
    version='1.0',    
    description='A timer Python package',
    url='https://github.com/Surja-Sanyal/Python3-Tools/timer',
    author='Surja Sanyal',
    author_email='hi.surja06@gmail.com',
    license='BSD 2-clause',
    packages=['timer'],
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

