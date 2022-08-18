from qiime2.plugin import model


class BWAIndexFileFormat(model.BinaryFileFormat):
    def _validate_(self, level):
        pass


class BWAIndexDirFmt(model.DirectoryFormat):
    amb = model.File(r'.*\.amb', format=BWAIndexFileFormat)
    ann = model.File(r'.*\.ann', format=BWAIndexFileFormat)
    bwt = model.File(r'..*\.bwt', format=BWAIndexFileFormat)
    pac = model.File(r'.*\.pac', format=BWAIndexFileFormat)
    sa = model.File(r'.*\.sa', format=BWAIndexFileFormat)


class SAMFileFormat(model.TextFileFormat):
    def _validate_(self, level):
        pass

class SAMFileDirFmt(model.DirectoryFormat):
    sam_files = model.FileCollection(r'*.sam', format=SAMFileFormat)


class BAMFileFormat(model.TextFileFormat):
    def _validate_(self, level):
        pass

class BAMFileDirFmt(model.DirectoryFormat):
    sam_files = model.FileCollection(r'*.sam', format=BAMFileFormat)



class VCFFileFormat(model.TextFileFormat):
    def _validate_(self, level):
        pass

class VCFFileDirFmt(model.DirectoryFormat):
    sam_files = model.FileCollection(r'*.sam', format=VCFFileFormat)


class NASPMatrixFileFormat(model.TextFileFormat):
    def _validate_(self, level):
        pass

class NASPMatrixFileDirFmt(model.DirectoryFormat):
    sam_files = model.FileCollection(r'*.sam', format=NASPMatrixFileFormat)


