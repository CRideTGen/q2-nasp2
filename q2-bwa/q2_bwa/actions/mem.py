from pathlib import Path

from q2_nasp2_types.formats import SAMFileDirFmt
from q2_types.feature_data import FeatureData, Sequence


def mem_single(sequences: FeatureData[Sequence]) -> SAMFileDirFmt:
    output_sams = SAMFileDirFmt()
    seq_path = Path(str(sequences))
    output_sams_path = Path(output_sams).joinpath("test.sam")

    with open(output_sams_path, 'w') as ff:
        ff.write("test1")


def mem_paired(sequences: FeatureData[Sequence]) -> SAMFileDirFmt:
    output_sams = SAMFileDirFmt()
    seq_path = Path(str(sequences))
    output_sams_path = Path(output_sams).joinpath("test.sam")

    with open(output_sams_path, 'w') as ff:
        ff.write("test2")
