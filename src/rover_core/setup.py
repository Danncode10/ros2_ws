from setuptools import find_packages, setup

package_name = 'rover_core'

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
    maintainer='dann',
    maintainer_email='lesterdannlopez7@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'rover_heartbeat_minimal = rover_core.rover_heartbeat_minimal:main',
            'rover_status_beacon = rover_core.rover_status_beacon:main',
        ],
    },
)
