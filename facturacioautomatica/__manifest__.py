# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Ajuste_PACASA',
    'version' : '2.3',
    'author':'s',
    'category': 'Sales',
    'maintainer': '',
    'summary': """ """

        You can directly create invoice and set done to delivery order by single click

    """,
    'website': 'https://www.craftsync.com/',
    'license': 'LGPL-3',
    'support':'info@craftsync.com',
    'depends' : ['sale_management','stock'],
    'data': [
        'views/stock_warehouse.xml',
    ],
    
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': ['static/description/main_screen.png'],

}
