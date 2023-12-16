from setuptools import setup

package_name = 'my_py_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
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
            'py_node = my_py_pkg.my_first_node:main',
            'robot_news_station = my_py_pkg.robot_news_station:main',
            'smartphone = my_py_pkg.smartphone:main',
            'number_publisher = my_py_pkg.number_publisher:main',
            'number_counter = my_py_pkg.number_counter:main',
            'add_two_ints_server = my_py_pkg.add_two_ints_server:main',
            'add_two_ints_client_no_oop = my_py_pkg.add_two_ints_client_no_oop:main',
            'add_two_ints_client = my_py_pkg.add_two_ints_client:main',
            'number_counter_server = my_py_pkg.number_counter_server:main',
            'number_counter_reset = my_py_pkg.number_counter_reset:main',
            'hw_status_publisher = my_py_pkg.hw_status_publisher:main',
            'rectangle_area_server = my_py_pkg.rectangle_area_server:main',
            'rectangle_area_client = my_py_pkg.rectangle_area_client:main',
            'led_panel = my_py_pkg.led_panel:main',
            'battery = my_py_pkg.battery:main'
        ],
    },
)

