# -*- coding: utf-8 -*-
#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
{
    'name': 'Charts of Accounts MSFO',
    'name_ru_RU': 'План счетов по международному стандарту отчетности',
    'version': '1.8.0',
    'author': 'Dmitry Klimanov',
    'email': 'k-dmitry2@narod.ru',
    'website': 'http://www.delfi2000.ru/',
    'description': '''Chart of MSFO
''',
    'description_ru_RU': '''План счетов по международному страндарту
''',
    'depends': [
        'ekd_account',
    ],
    'xml': [
         'xml/account_types.xml',
         'xml/account_chart.xml',
    ],
    'translation': [
#        'fr_FR.csv',
    ],
}
