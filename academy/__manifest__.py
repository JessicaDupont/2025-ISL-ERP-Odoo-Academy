{
    'name': 'Academy',
    'version': '1.0',
    'summary': 'Module de gestion scolaire',
    'description': 'Un module Odoo pour gérer une école.',
    'author': 'Jessica Dupont, Kevin Host, Ness Gira',
    'license': 'LGPL-3',
    'category': 'Sales',
    'depends': ['base'],  # Dépendance minimale pour fonctionner avec Odoo
    'data': [
        #security
        'security/security.xml',
        'security/ir.model.access.csv',
        #data
        #wizard
        #views & report
        'views/academy.menus.xml',#last in list
    ],
    'application': True
}
