# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Common Process',
    'version': '15.0.0.1',
    'category': 'Tools',
    'sequence': 11,
    'summary': """
            The Common Process Log module is a versatile tool designed to handle log management for applications. 
            Its primary features and functionalities include
            
            - Log Collection
            - Log Storage
            - Log Analysis
            - Integration
    """,

    'author': 'Reliution Consulting Services',
    'website': 'https://www.reliution.com/',
    'maintainer': 'Reliution Consulting Services',

    'depends': ['base', 'mail', 'portal'],

    'data': [
        'data/ir_sequence_data.xml',
        'security/ir.model.access.csv',
        'views/common_process_log.xml',
    ],

    'demo': [
        
    ],

    'qweb': [
        
    ],

    'installable': True,
    'application': False,
    'auto_install': False,

    'license': 'OPL-1',
    'price': 0.00,
    'currency': 'EUR',
}
