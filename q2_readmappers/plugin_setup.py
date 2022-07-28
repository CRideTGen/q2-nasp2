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

import importlib

from q2_types.feature_data import FeatureData, Sequence
from qiime2.core.type import Int, Range
from qiime2.plugin import Plugin, Str
from actions.paired_end_align import paired_end_align
from actions.reference_index import bwa_build
from q2_readmappers._types import BWAIndex

plugin = Plugin(name='samtools',
                version='0.0.1',
                package='q2_samtools',
                website='https://github.com/CRideTGen/q2-samtools')

# importlib.import_module("q2_samtools.transformers")



plugin.methods.register_function(
    function=bwa_build,
    inputs={'sequences': FeatureData[Sequence]},
    parameters={},
    outputs=[('database', BWAIndex)],
    input_descriptions={
        'sequences': 'Reference sequences used to build bwa index.'},
    parameter_descriptions={'n_threads': 'Number of threads to launch'},
    output_descriptions={'database': 'BWA index.'},
    name='Build bwa index from reference sequences.',
    description='Build bwa index from reference sequences.',
    citations=[]
)


plugin.methods.register_function(
    function=paired_end_align,
    inputs={},
    outputs=[('test_seq', FeatureData[Sequence])],
    parameters={'ref_seq_file': Str},
    input_descriptions=None,
    parameter_descriptions=None,
    name='',
    description=''
)
