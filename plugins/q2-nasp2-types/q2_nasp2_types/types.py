from q2_nasp2_types.formats import BWAIndexDirFmt, SAMFileDirFmt, BAMFileDirFmt, VCFFileDirFmt, NASP2MatrixFileDirFmt, \
    YAMLFileDirFmt, XMLFileDirFmt
from q2_nasp2_types.plugin_setup import plugin
from qiime2.plugin import SemanticType

# Semantic Types
BWAIndex = SemanticType('BWAIndex')

MappedSequences = SemanticType('MappedSequences',
                               field_names='type',
                               )
SAMFile = SemanticType('SAMFile', variant_of=[MappedSequences.field['type']])
BAMFile = SemanticType('BAMFile', variant_of=[MappedSequences.field['type']])

VCFFile = SemanticType('VCFFile')
NASP2MatrixFile = SemanticType('NASPMatrixFile')

Config = SemanticType('Config', field_names='type')
YAMLFile = SemanticType('YAMLFile', variant_of=[Config.field['type']])
XMLFile = SemanticType('XMLFile', variant_of=[Config.field['type']])

# Registering Types
plugin.register_semantic_types(MappedSequences, SAMFile, BAMFile, BWAIndex)
plugin.register_formats(SAMFileDirFmt, BAMFileDirFmt, BWAIndexDirFmt)
plugin.register_semantic_type_to_format(BWAIndex, artifact_format=BWAIndexDirFmt)
plugin.register_semantic_type_to_format(MappedSequences[SAMFile], artifact_format=SAMFileDirFmt)
plugin.register_semantic_type_to_format(MappedSequences[BAMFile], artifact_format=BAMFileDirFmt)

plugin.register_semantic_types(NASP2MatrixFile, VCFFile)
plugin.register_formats(NASP2MatrixFileDirFmt, VCFFileDirFmt)
plugin.register_semantic_type_to_format(NASP2MatrixFile, artifact_format=NASP2MatrixFileDirFmt)
plugin.register_semantic_type_to_format(VCFFile, artifact_format=VCFFileDirFmt)

plugin.register_semantic_types(Config, YAMLFile, XMLFile)
plugin.register_formats(YAMLFileDirFmt, XMLFileDirFmt)

plugin.register_semantic_type_to_format(Config[XMLFile], artifact_format=XMLFileDirFmt)
plugin.register_semantic_type_to_format(Config[YAMLFile], artifact_format=YAMLFileDirFmt)
