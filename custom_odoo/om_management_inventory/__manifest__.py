# -*- coding: utf-8 -*-
{
    'name': "Management Inventory",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Vinh PL",
    'website': "http://www.yourcompany.com",
    'category': 'Extra Tools',
    'version': '0.1',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_view.xml',
        'views/inventory.xml',
        'wizard/change_product_qty_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
