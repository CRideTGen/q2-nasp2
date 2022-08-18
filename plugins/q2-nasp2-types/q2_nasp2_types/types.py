from qiime2.plugin import SemanticType

from q2_nasp2_types.formats import BWAIndexDirFmt, SAMFileDirFmt, BAMFileDirFmt, VCFFileDirFmt, NASPMatrixFileDirFmt
from q2_nasp2_types.plugin_setup import plugin

# Semantic Types
BWAIndex = SemanticType('BWAIndex')

MappedSequences = SemanticType('MappedSequences',
                               field_names='fastq',
                               )
SAMFile = SemanticType('SAMFile', variant_of=[MappedSequences.field['fastq']])
BAMFile = SemanticType('BAMFile', variant_of=[MappedSequences.field['fastq']])

VCFFile = SemanticType('VCFFile')
NASPMatrixFile = SemanticType('NASPMatrixFile')

# Registering Types
plugin.register_semantic_types(BWAIndex)
plugin.register_formats(BWAIndexDirFmt)
plugin.register_semantic_type_to_format(BWAIndex, artifact_format=BWAIndexDirFmt)

plugin.register_semantic_types(MappedSequences, SAMFile)
plugin.register_formats(SAMFileDirFmt)
plugin.register_semantic_type_to_format(MappedSequences[SAMFile], artifact_format=SAMFileDirFmt)

plugin.register_semantic_types(MappedSequences, BAMFile)
plugin.register_formats(BAMFileDirFmt)
plugin.register_semantic_type_to_format(MappedSequences[BAMFile], artifact_format=BAMFileDirFmt)

plugin.register_semantic_types(VCFFile)
plugin.register_formats(VCFFileDirFmt)
plugin.register_semantic_type_to_format(VCFFile, artifact_format=VCFFileDirFmt)

plugin.register_semantic_types(NASPMatrixFile)
plugin.register_formats(NASPMatrixFileDirFmt)
plugin.register_semantic_type_to_format(NASPMatrixFile, artifact_format=NASPMatrixFileDirFmt)


