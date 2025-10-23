from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'fs_vehicle'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ("share/fs_vehicle", ["package.xml"]),
        ("share/fs_vehicle/urdf", [os.path.join("fs_vehicle","ackermann_car.urdf.xacro")]),
        ("share/fs_vehicle/config", [os.path.join("fs_vehicle","config","controllers.yaml")]),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kiran_gunathilaka',
    maintainer_email='kirangunathilaka@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)