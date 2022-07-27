from qiime2.plugin import SemanticType, model
from plugin_setup import plugin

BWAIndex = SemanticType('BWAIndex')



class BWAIndexFileFormat(model.BinaryFileFormat):
    def _validate(self, level):
        pass

class BWAIndexDirFmt(model.DirectoryFormat):
    amb = model.File(r'.+(?<!\.rev)\.1\.bt2l?', format=BWAIndexFileFormat)
    ann = model.File(r'.+(?<!\.rev)\.2\.bt2l?', format=BWAIndexFileFormat)
    bwt = model.File(r'.+\.3\.bt2l?', format=BWAIndexFileFormat)
    pac = model.File(r'.+\.4\.bt2l?', format=BWAIndexFileFormat)
    sa = model.File(r'.+\.rev\.1\.bt2l?', format=BWAIndexFileFormat)


plugin.register_semantic_types(BWAIndex)
plugin.register_semantic_type_to_format(BWAIndex, BWAIndexDirFmt)

#TODO add citations
plugin.register_views()
