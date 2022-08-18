from setuptools import setup, find_packages

setup(
    name='q2-nasp2',
    version='0.0.1',
    packages=find_packages(),
    url='github.com/CRideTGen/q2-nasp2',
    license='Apache-2.0',
    author='Chase Ridenour',
    author_email='cridenour@tgen.org',
    description='',
    entry_points={
        'qiime2.plugins': ['q2-nasp2=q2_nasp2.plugin_setup:plugin']
    },
    zip_safe=False,
)
