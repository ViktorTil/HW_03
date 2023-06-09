from setuptools import setup

setup(
    name='get_birthdays_per_week',
    version='1.0.0',
    description='get_birthdays_per_week from user_list',
    url='https://github.com/ViktorTil/HW_03',
    author='Tilnyak Viktor',
    author_email='tilnyakviktor@gmail.com',
    license='MIT',
    packages=['get_birthdays_per_week'],
    entry_points={'console_scripts': [
        'get_birthdays_per_week = get_birthdays_per_week.get_birthdays_per_week: main']}
    )
