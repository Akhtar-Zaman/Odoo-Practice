
from odoo import models, fields, api, _


class ProductGroup(models.Model):
    _inherit = 'product.template'


    group = fields.Many2one('product.group', string='Group')
    product_rating = fields.Selection([
        ('one', '☆'),
        ('two', '☆☆'),
        ('three', '☆☆☆'),
        ('four', '☆☆☆☆'),
        ('five', '☆☆☆☆☆')], default='one', string='Product Rating')


