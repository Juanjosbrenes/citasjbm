# -*- coding: utf-8 -*-
{
    'name': "Citas",

    'summary':'Creacion de citas' """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
       Este modulo nos permitira crear citas, recordatorios y otros eventos que nos ayude a organizar
	   nuestro dia a dia o nuestro entorno laboral
    """,

    'author': "Juan Jose Brenes Macias",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'utility',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
		# 'views/citasjbm_views.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
	'installable': True,
	'application': True,
	'auto_install': False,
}