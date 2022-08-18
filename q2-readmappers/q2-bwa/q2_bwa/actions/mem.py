from pathlib import Path

from q2_nasp2_types.formats import SAMFileDirFmt
from q2_types.per_sample_sequences import PairedEndSequencesWithQuality, SequencesWithQuality, \
    SingleLanePerSampleSingleEndFastqDirFmt, SingleLanePerSamplePairedEndFastqDirFmt
from q2_types.sample_data import SampleData


def mem_single(sequences: SingleLanePerSampleSingleEndFastqDirFmt) -> SAMFileDirFmt:
    output_sams = SAMFileDirFmt()
    seq_path = Path(str(sequences))
    output_sams_path = Path(output_sams.path).joinpath("test.sam")

    with open(output_sams_path, 'w') as ff:
        ff.write("test1")
    return output_sams


def mem_paired(sequences:  SingleLanePerSamplePairedEndFastqDirFmt) -> SAMFileDirFmt:
    output_sams = SAMFileDirFmt()
    seq_path = Path(str(sequences))
    output_sams_path = Path(output_sams.path).joinpath("test.sam")

    with open(output_sams_path, 'w') as ff:
        ff.write("test2")

    return output_sams
