#
# auto-pts - The Bluetooth PTS Automation Framework
#
# Copyright (c) 2021, Intel Corporation.
# Copyright (c) 2021, Codecoup.
# Copyright (c) 2023, NXP.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms and conditions of the GNU General Public License,
# version 2, as published by the Free Software Foundation.
#
# This program is distributed in the hope it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#
import os
import sys
import logging
import shutil
from subprocess import CalledProcessError

from autopts.ptsprojects.boards import Jlink
from autopts.bot.common import check_call

log = logging.debug

DEVICE_NAME = 'RTL8752H'
supported_projects = ['zephyr']
board_type = 'rtl8752h_evb/rtl8752htv'


def reset_cmd(iutctl):
    return Jlink(iutctl.debugger_snr, iutctl.device_core).reset_command


def build_and_flash(zephyr_wd, board, debugger_snr, conf_file=None, project_repos=None,
                    env_cmd=None, *args):
    """Build and flash Zephyr binary
    :param zephyr_wd: Zephyr source path
    :param board: IUT
    :param debugger_snr serial number
    :param conf_file: configuration file to be used
    :param project_repos: a list of repo paths
    :param env_cmd: a command to for environment activation, e.g. source /path/to/venv/activate
    """
    logging.debug("%s: %s %s %s", build_and_flash.__name__, zephyr_wd,
                  board, conf_file)

    if env_cmd:
        env_cmd = env_cmd.split() + ['&&']
    else:
        env_cmd = []

    tester_dir = os.path.join(zephyr_wd, 'tests', 'bluetooth', 'tester')
    build_dir = os.path.join(tester_dir, 'build')

    if os.path.exists(build_dir):
        shutil.rmtree(build_dir)

    bttester_overlay = os.path.abspath(os.path.join(tester_dir, 'boards', 'rtl8752h_evb_rtl8752htv.conf'))

    if conf_file and conf_file != 'default' and conf_file != 'prj.conf':
        bttester_overlay += f';{conf_file}'

    cmd = ['west', 'build', '--sysbuild', '-b', board, '--', f'-DEXTRA_CONF_FILE=\'{bttester_overlay}\'']
    print("cmd:", cmd)
    check_call(env_cmd + cmd, cwd=tester_dir)
    try:
        check_call(env_cmd + ['west', 'flash', '--skip-rebuild', '-i', debugger_snr], cwd=tester_dir)       
    except CalledProcessError:
       print("Flash failed. Please check JLink connection and ic status")
       raise