from setuptools import find_packages, setup
from glob import glob

package_name = 'fs_bringup'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ("share/fs_bringup/launch", ["fs_bringup/launch/sim_bringup.launch.py"]),
        ("share/fs_bringup", ["package.xml"]),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kiran_gunathilaka',
    maintainer_email='kirangunathilaka@gmail.com',
    description='TODO: Package description',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)