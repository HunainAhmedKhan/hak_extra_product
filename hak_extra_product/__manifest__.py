# -*- coding: utf-8 -*-
{
    'name': "Sales Extra Product",

    'summary': """
      Extra Product""",

    'description': """
         Add Extra Product in sales order
    """,

    'author': "HAK Tehnologies",
    'website': "https://www.HAKTehnologies.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '16.0.1',
    "license": "AGPL-3",
     'images': ['static/description/banner.png'],

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ],

}
