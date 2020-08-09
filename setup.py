from setuptools import setup

package_name = 'cifar_cnn'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ("lib/python3.6/site-packages/cifar_cnn/",
         ["cifar_cnn/my_model.h5"])
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hema',
    maintainer_email='ibrahim.essam1995@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'cifar = cifar_cnn.cifar:main'
        ],
    },
)
