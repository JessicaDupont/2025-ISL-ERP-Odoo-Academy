{
    'name': 'Academy',
    'version': '1.0',
    'summary': 'Module de gestion scolaire',
    'description': 'Un module Odoo pour gérer une école.',
    'author': 'Jessica Dupont, Kevin Host, Ness Gira',
    'license': 'LGPL-3',
    'category': 'Sales',
    'depends': [
        'base',
        'hr',
    ],  # Dépendance minimale pour fonctionner avec Odoo
    'data': [
        #security
        'security/security.xml',
        'security/ir.model.access.csv',
        #data
        'data/hr.department.csv',
        'data/academy.employee.role.csv',
        #wizard
        #views & report
        'views/academy_employee_views.xml',
        'views/academy_employee_role_views.xml',
        'views/academy_student_views.xml',
        'views/academy.menus.xml',#last in list
    ],
    'demo': [
        'demo/res.partner.csv',
        'demo/res.users.csv',
        'demo/hr.employee.csv',
        'demo/academy.employee.csv',
        'demo/academy.student.csv',
    ],
    'application': True
}
