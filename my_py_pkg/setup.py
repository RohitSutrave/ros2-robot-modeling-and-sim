from setuptools import find_packages, setup

package_name = 'my_py_pkg'

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
    maintainer='rohit',
    maintainer_email='rohit@todo.todo',
    description='Swarm Drone Python Package',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            "my_f_node = my_py_pkg.my_first_node:main",
            "pub_node = my_py_pkg.py_pub:main",
            "sub_node = my_py_pkg.py_sub:main",
            "drone_pub = my_py_pkg.drone_pub:main",
            "turtle_controller_node = my_py_pkg.turtle_controller:main",
            "number_counter_srv_node = my_py_pkg.number_counter:main",
            "reset_counter_client_node = my_py_pkg.reset_counter_client:main",
            "challange1_node = my_py_pkg.challange1:main",
        ],
    },
)