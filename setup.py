from setuptools import setup, find_packages

setup(
    name='flask_minimal',
    version='1.0.0',
    description='Template to build Flask-based APIs',
    license='',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ]
)

