import subprocess

from q2_types.feature_data import DNAFASTAFormat
from pathlib import Path

from .._formats import BWAIndexDirFmt, Bowtie2IndexDirFmtTest


def _run_command(cmd, verbose=True, stdout=None, stdin=None, cwd=None):
    if verbose:
        print('Running external command line application. This may print '
              'messages to stdout and/or stderr.')
        print('The commands to be run are below. These commands cannot '
              'be manually re-run as they will depend on temporary files that '
              'no longer exist.')
        print('\nCommand:', end=' ')
        print(' '.join(cmd), end='\n\n')
    subprocess.run(cmd, check=True, stdout=stdout, stdin=stdin, cwd=cwd)


def bwa_build(sequences: DNAFASTAFormat) -> BWAIndexDirFmt:
    database = BWAIndexDirFmt()
    seq_path = Path(str(sequences))
    db_path = Path(database.path)
    seq_sym_link = db_path.joinpath(seq_path.name)
    seq_sym_link.symlink_to(seq_path)


    build_cmd = ['bwa', 'index', str(seq_sym_link)]

    subprocess.run(build_cmd, check=True, stdout=None, stdin=None, cwd=None)
    seq_sym_link.unlink()

    return database

def bowtie2_build(sequences: DNAFASTAFormat,
                  n_threads: str = 1) -> Bowtie2IndexDirFmtTest:
    database = Bowtie2IndexDirFmtTest()
    build_cmd = ['bowtie2-build', '--threads', str(n_threads),
                 str(sequences), str(database.path / 'db')]
    _run_command(build_cmd)
    return database