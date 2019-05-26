from setuptools import setup,find_packages

setup(
    name="typeidea",
    version='0.3',
    description='Blog System base on Django',
    author='qmy',
    author_email='qiaomy_shou@sina.com',
    license='MIT',
    packages=find_packages('typeidea'),
    package_dir={'':'typeidea'},
    package_data={
        '':['themes/*/*/*/*',]
    },
    install_requires=['django~=1.11'],
    extras_require={
        'ipyhton':['ipython==6.2.1']
    },
    scripts=[
        'typeidea/manage.py'
    ],
    entry_points={
        'console_scripts':[
            'typeidea_manage=manage:main'
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic::Software Development :: Libraries',
        'Licence::OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ]

)