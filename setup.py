from setuptools import setup,find_packages

setup(
    name="typeidea",
    version='0.1',
    description='Blog System base on Django',
    author='qmy',
    author_email='qiaomy_shou@sina.com',
    license='MIT',
    packages=find_packages('typeidea'),
    package_dir={'':'typeidea'},
    package_data={
        '':['themes/*/*/*/*',]
    },
    install_requires=[
        'django~=1.11',
        'asn1crypto==0.24.0',
        'backcall==0.1.0',
        'bcrypt==3.1.6',
        'certifi==2019.3.9',
        'cffi==1.12.3',
        'chardet==3.0.4',
        'colorama==0.4.1',
        'coreapi==2.3.3',
        'coreschema==0.0.4',
        'cryptography==2.6.1',
        'decorator==4.4.0',
        'Django==1.11.8',
        'django-rest-framework==0.1.0',
        'djangorestframework==3.9.3',
        'Fabric3==1.14.post1',
        'gunicorn==19.9.0',
        'idna==2.8',
        'ipython==7.5.0',
        'ipython-genutils==0.2.0',
        'itypes==1.1.0',
        'jedi==0.13.3',
        'Jinja2==2.10.1',
        'MarkupSafe==1.1.1',
        'meld3==1.0.2',
        'mistune==0.8.4',
        'mysqlclient==1.4.2',
        'paramiko==2.4.2',
        'parso==0.4.0',
        'passlib==1.7.1',
        'pickleshare==0.7.5',
        'prompt-toolkit==2.0.9',
        'pyasn1==0.4.5',
        'pycparser==2.19',
        'Pygments==2.4.1',
        'PyMySQL==0.7.11',
        'PyNaCl==1.3.0',
        'pypiserver==1.3.0',
        'pytz==2019.1',
        'requests==2.21.0',
        'six==1.12.0',
        'sqlparse==0.3.0',
        'traitlets==4.3.2',
        'uritemplate==3.0.0',
        'urllib3==1.24.3',
        'wcwidth==0.1.7',
    ],
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