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


from q2_nasp2_types.formats import SAMFileFormat
from q2_nasp2_types.types import BWAIndex, SAMFile
from q2_types.feature_data import FeatureData, Sequence, PairedEndSequence
from q2_types.per_sample_sequences import SequencesWithQuality, PairedEndSequencesWithQuality
from q2_types.sample_data import SampleData
from qiime2.plugin import Plugin

from q2_bwa.actions.mem import mem_single, mem_paired
from q2_bwa.actions.reference_index import index

plugin = Plugin(name='bwa',
                version='0.0.1',
                package='q2_bwa',
                website='https://github.com/CRideTGen/q2-readmappers')

plugin.methods.register_function(
    function=index,
    inputs={'sequences': FeatureData[PairedEndSequence]},
    parameters={},
    outputs=[('database', BWAIndex)],
    input_descriptions={
        'sequences': 'Reference sequences used to build bwa index.'},
    parameter_descriptions={},
    output_descriptions={'database': 'BWA index.'},
    name='Build bwa index from reference sequences.',
    description='Build bwa index from reference sequences.',
    citations=[]
)

plugin.methods.register_function(
    function=mem_single,
    inputs={'sequences': SampleData[SequencesWithQuality]},
    parameters={},
    outputs=[('output_sams', SAMFile)],
    input_descriptions={
        'sequences': 'Reference sequences used to build bowtie2 index.'},
    parameter_descriptions={},
    output_descriptions={'output_sams': 'Bowtie2 index.'},
    name='Build bowtie2 index from reference sequences.',
    description='Build bowtie2 index from reference sequences.'
)

plugin.methods.register_function(
    function=mem_paired,
    inputs={'sequences': SampleData[PairedEndSequencesWithQuality]},
    parameters={},
    outputs=[('output_sams', SAMFileFormat)],
    input_descriptions={
        'sequences': 'Reference sequences used to build bowtie2 index.'},
    parameter_descriptions={},
    output_descriptions={'output_sams': 'Bowtie2 index.'},
    name='Build bowtie2 index from reference sequences.',
    description='Build bowtie2 index from reference sequences.'
)
