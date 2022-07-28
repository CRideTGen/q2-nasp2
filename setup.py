from setuptools import setup, find_packages

setup(
    name='q2-readmappers',
    version='0.0.1',
    packages=find_packages(),
    url='github.com/CRideTGen/q2-readmappers',
    license='Apache-2.0',
    author='Chase Ridenour',
    author_email='cridenour@tgen.org',
    description='',
    entrypoints ={
        'qiime2.plugins': ['q2-readmappers=q2_read_mappers.plugin_setup:plugin']
                  },
    zip_safe=False,
)
