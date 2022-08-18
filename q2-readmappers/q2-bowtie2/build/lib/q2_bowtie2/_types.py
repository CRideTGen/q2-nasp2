# from qiime2.plugin import SemanticType
# from q2_types.feature_data import AlignedSequence
#
# BWAIndexTest = SemanticType('BWAIndex')
# Bowtie2IndexTest = SemanticType('Bowtie2IndexTest')
#
# MappedSequences = SemanticType('MappedSequences',
#                                field_names=['fasta', 'fastq'],
#                                field_members={
#                                    'fasta': (AlignedSequence),
#                                    'fastq': (AlignedSequence)
#                                               })
#
# SAMFile = SemanticType('SAMFile', variant_of=[MappedSequences.field['fastq']])
# BAMFile = SemanticType('BAMFile', variant_of=[MappedSequences.field['fastq']])
