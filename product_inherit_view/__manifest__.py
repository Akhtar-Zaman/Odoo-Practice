
{
    'name' : 'Product Extension',
    'version' : '14.0',
    'summary': '',
    'sequence': 1,
    'description': '',
    'category': '',
    'website': 'https://www.odoo.com',
    'depends' : ['base','sale','purchase'],
    'data': [
        'views/product_inherited_view.xml',
        'views/product_brand.xml',
        'views/dealer_name.xml',
        'views/purchase_inherited_view.xml',
        'reports/report.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
