
{
    'name' : 'Requisition Module',
    'version' : '14.0',
    'summary': '',
    'sequence': 2,
    'description': '',
    'category': '',
    'website': 'https://www.odoo.com',
    'depends' : ['base','sale','hr'],
    'data': [

        # Security
        'security/requisition_Groups.xml',
        'security/ir.model.access.csv',

        
        'views/requisition.xml',


    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
