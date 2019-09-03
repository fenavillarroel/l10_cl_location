# -*- coding: utf-8 -*-
{
    'name': "Localización Geografica Chile",

    'summary': """
        Distribución Gegrafica Chile. Comunas, Provincias, Región""",

    'description': """
        Agrega Datos Chilenos:
            - Código de Región Nombre de la Región
            - Código de Provincia Nombre de la Provincia
            - Código de la Comuna Nombre de la Comuna
        Actualiza estos datos a Partners, Company y Employee
    """,

    'author': "Fernando Villarroel N",
    'website': "http://uaysen.cl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Account',
    'version': '0.1',
    'depends': ['base','account','hr'],
    # any module necessary for this one to work correctly
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner.xml',
        'views/res_company.xml',
        'views/hr_employee.xml',
        'views/res_country_region.xml',
        'views/res_country_provincias.xml',
        'views/res_country_state.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application':True,
}