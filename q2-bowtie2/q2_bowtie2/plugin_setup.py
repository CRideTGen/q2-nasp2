#   Copyright 2022 Chase Ridenour
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.


from q2_nasp2_types.types import Bowtie2IndexTest
from q2_types.feature_data import FeatureData, Sequence
from qiime2.core.type import Int, Range
from qiime2.plugin import Plugin

from q2_bowtie2.actions.map_reads import bowtie2
from q2_bowtie2.actions.reference_index import bowtie2_build

plugin = Plugin(name='bowtie2',
                version='0.0.1',
                package='q2_bowtie2',
                website='https://github.com/CRideTGen/q2-readmappers')


plugin.methods.register_function(
    function=bowtie2_build,
    inputs={'sequences': FeatureData[Sequence]},
    parameters={'n_threads': Int % Range(1, None)},
    outputs=[('database', Bowtie2IndexTest)],
    input_descriptions={
        'sequences': 'Reference sequences used to build bowtie2 index.'},
    parameter_descriptions={'n_threads': 'Number of threads to launch'},
    output_descriptions={'database': 'Bowtie2 index.'},
    name='Build bowtie2 index from reference sequences.',
    description='Build bowtie2 index from reference sequences.'
)

plugin.methods.register_function(
    function=bowtie2(),
    inputs={'sequences': FeatureData[Sequence]},
    parameters={'n_threads': Int % Range(1, None)},
    outputs=[('database', Bowtie2IndexTest)],
    input_descriptions={
        'sequences': 'Reference sequences used to build bowtie2 index.'},
    parameter_descriptions={'n_threads': 'Number of threads to launch'},
    output_descriptions={'database': 'Bowtie2 index.'},
    name='Build bowtie2 index from reference sequences.',
    description='Build bowtie2 index from reference sequences.'
)
