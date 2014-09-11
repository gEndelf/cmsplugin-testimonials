from setuptools import setup, find_packages

version = __import__('cmsplugin_testimonials').__version__
readme = open('README.md').read()
requirements = open('requirements.txt').read().split('\n')

setup(
    name='cmsplugin_testimonials',
    version=version,
    description='Testimonials plugin for the django CMS.',
    long_description=readme,
    author='Alex Padalka, Danilo Bargen',
    author_email='alex.com.ua@gmail.com',
    url='https://github.com/gEndelf/cmsplugin-testimonials',
    license='MIT',
    keywords='django django-cms cms plugin testimonials',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requirements
)
