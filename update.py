#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Update the time and memory used by each CodeEval's challenge solution.

Get that information for challenge and write them to the README file.

"""
__author__ = "joe di castro <joe@joedicastro.com>"
__license__ = "MIT"
__date__ = "2014-01-26"
__version__ = "0.1"

import glob
import sys
import os
import re
from subprocess import check_output
from time import time


def get_git_files(repository, staged=False):
    """Get a list of files under a git repository.

    :repository: the git repository
    :staged: if false return all files, else return only the staged ones
    :returns: the files under git control

    """
    os.chdir(repository)
    if staged:
        git_command = "git diff --cached --name-only".split()
    else:
        git_command = "git ls-files".split()
    git_output = check_output(git_command).split(os.linesep)
    files = [os.path.join(repository, line) for line in git_output if line]

    return files


def get_processor_info():
    """Get the name of the computer's processor.

    :returns: the computer's processor name

    """
    with open('/proc/cpuinfo') as cpuinfo:
        processor = re.findall(r'model name\s+: (.+)\n', cpuinfo.read())[0]
    return processor.replace('(R)', '').replace('(TM)', '')


def get_time(script):
    """Get the time taken to execute a script.

    :script: the python script used to solve a challenge
    :returns: the time taken to execute the script

    """
    start_time = time()
    check_output(
        'python2 {0} {1}'.format(
            script['script'],
            script.get('input', '')
        ).split()
    )
    stop_time = time()
    return stop_time - start_time


def get_memory(script):
    """Get the memory taken to execute a script.

    This function uses the external utility "memory profiler" to get the data.
    https://github.com/fabianp/memory_profiler

    :script: the python script used to solve a challenge
    :returns: the memory taken to execute the script (in MiB)

    """
    check_output(
        'mprof run -T 0.0001 {0} {1}'.format(
            script['script'],
            script.get('input', '')
        ).split()
    )
    data_file = glob.glob('*.dat')[0]

    with open(data_file) as data_input:
        memory_data = data_input.read()

    consumptions = (
        float(i) for i in re.findall(
            'MEM (\d+.\d+) \d+.\d+',
            memory_data,
            re.MULTILINE
        )
    )
    os.remove(data_file)
    return max(consumptions)


def write_readme(challenges):
    """Write the README.md document.

    :challenges: the challenges dictionary

    """
    easy, moderate, hard = (
        sorted(
            [
                '     {0:40}    {1:.5f} s {2:>12.3f} MiB'.format(
                    i,
                    challenges[i]['time'],
                    challenges[i]['memory']
                ) for i in challenges if challenges[i]['level'] == level
            ]
        )
        for level in ('easy', 'moderate', 'hard')
    )

    string = """
    # Code Eval Solutions
    
    ## About Code Eval
    
    [Code Eval](https://www.codeeval.com) is a website to challenge programmers
    with programming problems intended to help you to improve your programming
    skills.
    
    ## About this repository
    
    There is my attempt to solve some challenge of this project, using the
    Python language. The target is to solve as many as I can, and keep the time
    consumed by each script below 10 seconds (at that point the script is
    interrupted by Code Eval).
    
    ### Contents:
    
    There are 3 directories, `easy/`, `moderate/` and `hard/` corresponding
    with the level of the challenges in the website. Inside of each hone are
    two types of files, the `*.py2` files are the ones with the code and the
    `*.txt` files are those which contains the inputs to test the code.
    
    ## About Cheating
    
    Don't cheat! If you cheat, you only fool yourself! If you can't do it, you
    can not do it, that's all! Almost you tried, and if you keep learning and
    studying, maybe one day you can solve those challenge that seemed so hard a
    few early.
    
    Be proud of what you have achieved instead, even if is little. Especially
    if your math and programming skills or education is not so vast (as in my
    case). I'm very proud to have solved all of this challenge without cheating
    or copy another else's solutions. That's the right attitude.
    
    But, once you have a solution, you can learn a lot from the solutions of
    others.  That's the purpose of this repository too. Maybe you couldn't
    learn a lot from my solutions, maybe even you can laugh of the most naive
    ones, but doesn't matter, be humble and remember that even the most idiot
    can teach you always something. The second purpose is to have a online
    backup of this code, some challenge were hard to break and I would hate to
    loose this code.
    
    __The most important thing isn't the Code Eval's rank that you achieve or
    the number of challenge that you solved, the most important thing is what
    you have learned in the process!__
    
    ## Solved Challenges
    
    Times computed in a {0} processor.
    
    ### Easy
    
    Solved {1} challenges
    
    {2}
    
    ### Moderate
    
    Solved {3} challenges
    
    {4}
    
    ### Moderate
    
    Solved {5} challenges
    
    {6}
    
    """.format(
        get_processor_info(),
        len(easy),
        os.linesep.join(easy),
        len(moderate),
        os.linesep.join(moderate),
        len(hard),
        os.linesep.join(hard)
    ).replace(' ', '').lstrip()

    with open('README.md', 'w') as readme:
        readme.write(string)


def main():
    """Main section."""
    git_files = get_git_files(os.getcwd())

    # get challenges info
    challenges = {}
    for f in git_files:
        level = os.path.split(os.path.dirname(f))[-1]
        challenge, filetype = os.path.splitext(os.path.basename(f))
        challenge = challenge.replace('_', ' ').title()
        if filetype in ('.txt', '.py2'):
            if not challenges.get(challenge, None):
                challenges[challenge] = {}

            key = {'.txt': 'input', '.py2': 'script'}.get(filetype)
            challenges[challenge][key] = f
            challenges[challenge]['level'] = level

    # get time and memory data
    for c in challenges:
        challenges[c]['time'] = get_time(challenges[c])
        challenges[c]['memory'] = get_memory(challenges[c])

    write_readme(challenges)

if __name__ == '__main__':
    main()
