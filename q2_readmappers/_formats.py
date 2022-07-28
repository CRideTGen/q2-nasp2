from qiime2.plugin import model

class BWAIndexFileFormat(model.BinaryFileFormat):
    def _validate(self, level):
        pass

class BWAIndexDirFmt(model.DirectoryFormat):
    amb = model.File(r'.+(?<!\.rev)\.1\.bt2l?', format=BWAIndexFileFormat)
    ann = model.File(r'.+(?<!\.rev)\.2\.bt2l?', format=BWAIndexFileFormat)
    bwt = model.File(r'.+\.3\.bt2l?', format=BWAIndexFileFormat)
    pac = model.File(r'.+\.4\.bt2l?', format=BWAIndexFileFormat)
    sa = model.File(r'.+\.rev\.1\.bt2l?', format=BWAIndexFileFormat)