from setuptools import setup, find_packages
setup(
    name='pre_pre_beta_siri',
    version='0.1.0',
    packages=find_packages(include=['pre_pre_beta_siri', 'pre_pre_beta_siri.*']),
    install_requires=[
        "prompt_toolkit == 3.0.47",
        "wcwidth == 0.2.13",
        "rich == 13.7.1"
    ],
    entry_points={
        'console_scripts': ['pre_pre_beta_siri=pre_pre_beta_siri:main']
    }
)
