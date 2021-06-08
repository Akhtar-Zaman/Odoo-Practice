
{
    'name' : 'Bista Exam Test',
    'version' : '14.0',
    'summary': '',
    'sequence': 2,
    'description': '',
    'category': '',
    'website': 'https://www.odoo.com',
    'depends' : ['base','stock','purchase','contacts','sale_management'],
    'data': [
        'security/ir.model.access.csv',

        
        'reports/report.xml',        
        'views/product_group.xml',
        'views/product_inherited_view.xml',
        'views/purchase_inherited_view.xml',
        # 'views/sale_inherit.xml',

    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
