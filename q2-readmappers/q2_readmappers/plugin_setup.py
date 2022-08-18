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
from q2_types.feature_data import FeatureData, Sequence
from q2_types.per_sample_sequences import SequencesWithQuality, PairedEndSequencesWithQuality
from q2_types.sample_data import SampleData
from qiime2.plugin import Plugin

from q2_nasp2_types.types import SAMFile
from q2_readmappers.actions.map_reads import bwa

plugin = Plugin(name='readmappers',
                version='0.0.1',
                package='q2_readmappers',
                website='https://github.com/CRideTGen/q2-readmappers')

plugin.pipelines.register_function(
    function=bwa,
    inputs={'sequences': SampleData[SequencesWithQuality | PairedEndSequencesWithQuality]},
    parameters={},
    outputs=[('output_sams', SAMFile)],
    input_descriptions={
        'sequences': '.'},
    parameter_descriptions={},
    output_descriptions={'output_sams': ''},
    name='',
    description=''

)
