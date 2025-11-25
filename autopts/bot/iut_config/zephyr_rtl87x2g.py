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

# Stable Zephyr IUT config

iut_config = {
    "prj.conf": {
    },  # Default config file name
     "rpa_timeout.conf": {
        "overlay": {
            'CONFIG_TINYCRYPT': 'y',
            'CONFIG_TINYCRYPT_ECC_DH': 'y',
            'CONFIG_BT_TINYCRYPT_ECC': 'y',            
            'CONFIG_BT_PRIVACY': 'y',
            'CONFIG_BT_RPA_TIMEOUT': '28',
        },
        "test_cases": [
            'GAP/PRIV/CONN/BV-10-C',
            'GAP/CONN/UCON/BV-06-C',
        ]
    },    
    "enforce_mitm.conf": {
        "overlay": {
            'CONFIG_BT_SMP_ENFORCE_MITM': 'y',
            'CONFIG_TINYCRYPT': 'y',
            'CONFIG_TINYCRYPT_ECC_DH': 'y',
            'CONFIG_BT_TINYCRYPT_ECC': 'y',           
        },
        "test_cases": [
            'GAP/SEC/SEM/BV-58-C',            
            'GAP/SEC/SEM/BV-21-C',
            'GAP/SEC/SEM/BV-38-C',
            'GAP/SEC/SEM/BV-22-C',
            'GAP/SEC/SEM/BV-40-C',
            'GAP/SEC/SEM/BV-61-C',
            'GAP/SEC/SEM/BV-26-C',
            'GAP/SEC/SEM/BV-42-C',
            'GAP/SEC/SEM/BV-44-C',
            'GAP/SEC/SEM/BV-27-C',
        ]
    },
    "le_sc_only.conf": {
        "overlay": {
            'CONFIG_TINYCRYPT': 'y',
            'CONFIG_TINYCRYPT_ECC_DH': 'y',
            'CONFIG_BT_TINYCRYPT_ECC': 'y',            
            'CONFIG_BT_SMP_SC_ONLY': 'y'
        },
        "test_cases": [
            'GAP/SEC/SEM/BV-28-C',
            'GAP/SEC/SEM/BV-29-C',
            'GAP/SEC/SEM/BI-09-C',
            'GAP/SEC/SEM/BV-24-C',
            'GAP/SEC/SEM/BV-23-C',
        ]
    },
    "smp_min_enc_key_size.conf": {
        "overlay": {
            'CONFIG_TINYCRYPT': 'y',
            'CONFIG_TINYCRYPT_ECC_DH': 'y',
            'CONFIG_BT_TINYCRYPT_ECC': 'y',            
            'CONFIG_BT_SMP_MIN_ENC_KEY_SIZE': '16'
        },
        "test_cases": [
            'GAP/SEC/SEM/BI-10-C',
            'GAP/SEC/SEM/BI-20-C',
            'GAP/SEC/SEM/BI-21-C',
            'GAP/SEC/SEM/BI-22-C',
            'GAP/SEC/SEM/BI-23-C',
        ]
    },
    "enable_bt_privacy.conf": {
        "overlay": {
            'CONFIG_TINYCRYPT': 'y',
            'CONFIG_TINYCRYPT_ECC_DH': 'y',
            'CONFIG_BT_TINYCRYPT_ECC': 'y',           
            'CONFIG_BT_PRIVACY': 'y'
        },
        "test_cases": [
            'GAP/BROB/BCST/BV-03-C',
            'GAP/BROB/BCST/BV-05-C',
            'GAP/CONN/DCON/BV-04-C',
            'GAP/GAT/BV-18-C',
        ]
    },    
}

retry_config = {
}
