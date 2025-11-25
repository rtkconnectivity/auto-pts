#
# auto-pts - The Bluetooth PTS Automation Framework
#
# Copyright (c) 2018, Intel Corporation.
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

# Sample user_config file
# Apply your changes and rename it to config.py

from autopts.bot.iut_config.zephyr_rtl87x2g import iut_config

BotProjects = []

z = zephyr_rtl87x2g = {
    'name': 'zephyr'
}

# ****************************************************************************
# AutoPTS configuration
# ****************************************************************************
z['auto_pts'] = {
    'server_ip': ['172.29.79.127'],   
    'client_ip': ['127.0.0.1'],
    'cli_port': [65001],
    'srv_port': [65000],
    'project_path': r'C:\zhiyuan_tang\ws\zephyr',
    'workspace': r'C:\zhiyuan_tang\auto-pts\autopts\workspaces\zephyr\zephyr-master\zephyr-master.pqw6',
    'database_file': r'C:\zhiyuan_tang\auto-pts\autopts\ptsprojects\zephyrTestCase.db',
    'store': True,
    'board': 'rtk_rtl8762gnevb',
    "device_core": 'RTL87X2G',
    'tty_file': 'COM11',
    'debugger_snr': '69408597',
    'enable_max_logs': False,
    'retry': 2,
    #'bd_addr': 'C007E833C577',
    # 'ykush': '3',  # 1|2|3|a
    'recovery': False,
    'superguard': 15,  # minutes
}

# ****************************************************************************
# Git repositories configuration
# ****************************************************************************
z['git'] = {
    'zephyr': {
        'path': 'C:/zhiyuan_tang/ws/zephyr',
        'remote': 'rtkconnectivity',
        'branch': 'realtek-main-v3.7',
        'stash_changes': False,
        'update_repo': False,
    },
}

# ****************************************************************************
# Mailbox configuration
#
# To send an email report with test result summary
# ****************************************************************************
# z['mail'] = {

# }

# ****************************************************************************
# Github configuration
#
# To commit and push logs to Github.
# Configured ssh-agent must be started earlier.
# ****************************************************************************
# z['githubdrive'] = {
#     'path': 'C:/zhiyuan_tang/ws/zephyr',
#     'remote': 'rtkconnectivity',
#     'branch': 'realtek-main-v3.7',
#     'subdir': 'zephyr/',
#     'commit_msg': '{branch}_{timestamp}_{commit_sha}',                
# }

# ****************************************************************************
# Google Drive configuration
#
# To put the tests execution logs to Google Drive
# ****************************************************************************
z['gdrive'] = {

}

# ****************************************************************************
# IUT configuration
#
# To apply test case specific changes in IUT configuration
# ****************************************************************************

z['iut_config'] = iut_config

# ****************************************************************************
# Scheduler configuration
#
# To run the tests periodically
# ****************************************************************************
z['scheduler'] = {

}

# z['scheduler'] = {
#     'monday': '10:20',
#     'friday': '20:00',
# }

BotProjects.append(zephyr_rtl87x2g)
