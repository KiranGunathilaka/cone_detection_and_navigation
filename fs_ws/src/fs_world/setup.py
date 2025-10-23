from setuptools import find_packages, setup

package_name = 'fs_world'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    include_package_data=True,
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kiran_gunathilaka',
    maintainer_email='kirangunathilaka@gmail.com',
    description='Package for the formula student track world creation',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ["make_world=fsd_world.oval_track_world:main"],
    },
)
