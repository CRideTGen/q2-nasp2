from q2_types.feature_data import FeatureData, Sequence
from q2_types.per_sample_sequences import PairedEndSequencesWithQuality, SequencesWithQuality, FastqManifestFormat
from q2_types.sample_data import SampleData


def bwa(ctx, sequences):

    if sequences.type.equals(SampleData[PairedEndSequencesWithQuality]):
        mem = ctx.get_action('mem_paired', 'bwa')

    elif sequences.type.equals(SampleData[SequencesWithQuality]):
        mem = ctx.get_action('mem_single', 'bwa')
    else:
        raise ValueError("Unknown sequence type")

    results = list()

    output_sams = mem(sequences=sequences)

    results += output_sams

    return tuple(results)


def bowtie2():
    pass

