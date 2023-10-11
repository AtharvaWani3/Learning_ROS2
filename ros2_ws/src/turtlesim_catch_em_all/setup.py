from setuptools import find_packages, setup

package_name = 'turtlesim_catch_em_all'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='atharva',
    maintainer_email='aawani@asu.edu',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'turtle_controller = turtlesim_catch_em_all.turtle_controller:main',
            'turtle_spawner = turtlesim_catch_em_all.turtle_spawner:main',
            'turtle_catcher = turtlesim_catch_em_all.turtle_catcher:main'
        ],
    },
)
