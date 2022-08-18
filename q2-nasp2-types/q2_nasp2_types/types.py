from qiime2.plugin import SemanticType
from q2_types.feature_data import AlignedSequence

from q2_nasp2_types.formats import BWAIndexDirFmt, Bowtie2IndexDirFmtTest, SAMFileDirFmt
from q2_nasp2_types.plugin_setup import plugin

BWAIndex = SemanticType('BWAIndex')
Bowtie2IndexTest = SemanticType('Bowtie2IndexTest')

MappedSequences = SemanticType('MappedSequences',
                               field_names='fastq',
                               )

SAMFile = SemanticType('SAMFile', variant_of=[MappedSequences.field['fastq']])
BAMFile = SemanticType('BAMFile', variant_of=[MappedSequences.field['fastq']])

plugin.register_semantic_types(Bowtie2IndexTest)
plugin.register_formats(Bowtie2IndexDirFmtTest)
plugin.register_semantic_type_to_format(Bowtie2IndexTest, artifact_format=Bowtie2IndexDirFmtTest)

plugin.register_semantic_types(BWAIndex)
plugin.register_formats(BWAIndexDirFmt)
plugin.register_semantic_type_to_format(BWAIndex, artifact_format=BWAIndexDirFmt)

plugin.register_semantic_types(MappedSequences, SAMFile)
plugin.register_formats(SAMFileDirFmt)
plugin.register_semantic_type_to_format(MappedSequences[SAMFile], artifact_format=SAMFileDirFmt)
