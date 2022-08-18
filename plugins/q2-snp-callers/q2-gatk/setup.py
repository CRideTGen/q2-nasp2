from setuptools import setup, find_packages

setup(
    name='q2-gatk',
    version='0.0.1',
    packages=find_packages(),
    url='github.com/CRideTGen/q2-gatk',
    license='Apache-2.0',
    author='Chase Ridenour',
    author_email='cridenour@tgen.org',
    description='',
    entry_points={
        'qiime2.plugins': ['q2-gatk=q2_gatk.plugin_setup:plugin']
    },
    zip_safe=False,
)
