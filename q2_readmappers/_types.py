from qiime2.plugin import SemanticType, model
from plugin_setup import plugin
from ._formats import BWAIndexDirFmt

BWAIndex = SemanticType('BWAIndex')


plugin.register_semantic_types(BWAIndex)
plugin.register_semantic_type_to_format(BWAIndex, BWAIndexDirFmt)

#TODO add citations
plugin.register_views()
