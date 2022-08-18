import subprocess


def run_command(cmd, verbose=True, stdout=None, stdin=None, cwd=None):
    if verbose:
        print('Running external command line application. This may print '
              'messages to stdout and/or stderr.')
        print('The commands to be run are below. These commands cannot '
              'be manually re-run as they will depend on temporary files that '
              'no longer exist.')
        print('\nCommand:', end=' ')
        print(' '.join(cmd), end='\n\n')
    subprocess.run(cmd, check=True, stdout=stdout, stdin=stdin, cwd=cwd)