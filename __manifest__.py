# -*- coding: utf-8 -*-
{
    'name': "Phones selling module",

    'summary': """
        This module provides features for mobile phone sale""",

    'description': """
        This module adds Manufacturer and PhoneModel models and provides two step wizard for convenient quick product creating  
    """,

    'author': "Georgy Temerev",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Sales',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['sale_management'],

    # always loaded
    'data': [
        'views/views.xml',
        'views/menus.xml',
        'views/templates.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/manufacturers.xml'
    ],
}