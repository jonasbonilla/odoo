# -*- coding: utf-8 -*-
{
    'name': 'Website Policies',
    'version': '1.0',
    'summary': 'Ajustes báscicos para clientes stándar',
    'author': 'Jonas Bonilla',
    'website': 'https://www.linkedin.com/in/jonasbonilla/',
    'category': 'Website',
    'depends': [
        'base',
        'mail',
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/rules.xml',
        'data/data.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
