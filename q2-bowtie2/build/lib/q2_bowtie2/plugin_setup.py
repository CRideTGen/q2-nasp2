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


from q2_types.feature_data import FeatureData, Sequence, PairedEndSequence
from qiime2.core.type import Int, Range
from qiime2.plugin import Plugin

# from q2_nasp2_types._formats import Bowtie2IndexDirFmtTest, BWAIndexDirFmt, SAMFileDirFmt, SAMFileFileFormat
# from q2_bowtie2._types import BWAIndexTest, Bowtie2IndexTest, MappedSequences, SAMFile
# from q2_bowtie2.actions.reference_index import bwa_build, bowtie2_build
# from q2_bowtie2.actions.map_reads import bwa, bowtie2

plugin = Plugin(name='bowtie2',
                version='0.0.1',
                package='q2_bowtie2',
                website='https://github.com/CRideTGen/q2-readmappers')

# plugin.register_semantic_types(Bowtie2IndexTest)
# plugin.register_formats(Bowtie2IndexDirFmtTest)
# plugin.register_semantic_type_to_format(Bowtie2IndexTest, Bowtie2IndexDirFmtTest)
#
# plugin.register_semantic_types(BWAIndexTest)
# plugin.register_formats(BWAIndexDirFmt)
# plugin.register_semantic_type_to_format(BWAIndexTest, BWAIndexDirFmt)
#
# plugin.register_semantic_types(MappedSequences, SAMFile)
# plugin.register_formats(SAMFileDirFmt)
# plugin.register_semantic_type_to_format(MappedSequences[SAMFile], SAMFileDirFmt)
#
# # importlib.import_module("q2_samtools.transformers")
#
#
# # TODO add citations
# # plugin.register_views()
#
#
# plugin.methods.register_function(
#     function=bwa_build,
#     inputs={'sequences': FeatureData[PairedEndSequence]},
#     parameters={},
#     outputs=[('database', BWAIndexTest)],
#     input_descriptions={
#         'sequences': 'Reference sequences used to build bwa index.'},
#     parameter_descriptions={},
#     output_descriptions={'database': 'BWA index.'},
#     name='Build bwa index from reference sequences.',
#     description='Build bwa index from reference sequences.',
#     citations=[]
# )
#
# plugin.methods.register_function(
#     function=bowtie2_build,
#     inputs={'sequences': FeatureData[Sequence]},
#     parameters={'n_threads': Int % Range(1, None)},
#     outputs=[('database', Bowtie2IndexTest)],
#     input_descriptions={
#         'sequences': 'Reference sequences used to build bowtie2 index.'},
#     parameter_descriptions={'n_threads': 'Number of threads to launch'},
#     output_descriptions={'database': 'Bowtie2 index.'},
#     name='Build bowtie2 index from reference sequences.',
#     description='Build bowtie2 index from reference sequences.'
# )
#
# plugin.methods.register_function(
#     function=bwa(),
#     inputs={'sequences': FeatureData[Sequence]},
#     parameters={},
#     outputs=[('aligned_reads', SAMFileFileFormat)],
#     input_descriptions={
#         'sequences': 'Reference sequences used to build bowtie2 index.'},
#     parameter_descriptions={'n_threads': 'Number of threads to launch'},
#     output_descriptions={'database': 'Bowtie2 index.'},
#     name='Build bowtie2 index from reference sequences.',
#     description='Build bowtie2 index from reference sequences.'
# )
#
# plugin.methods.register_function(
#     function=bowtie2(),
#     inputs={'sequences': FeatureData[Sequence]},
#     parameters={'n_threads': Int % Range(1, None)},
#     outputs=[('database', Bowtie2IndexTest)],
#     input_descriptions={
#         'sequences': 'Reference sequences used to build bowtie2 index.'},
#     parameter_descriptions={'n_threads': 'Number of threads to launch'},
#     output_descriptions={'database': 'Bowtie2 index.'},
#     name='Build bowtie2 index from reference sequences.',
#     description='Build bowtie2 index from reference sequences.'
# )
