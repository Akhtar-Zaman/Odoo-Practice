from odoo import models, fields, api, _



class product_inherited_view(models.Model):
    _inherit = 'product.template'

    product_brand = fields.Many2one('product.brand', string="Product Brand")
    dealer_name = fields.Many2one('dealer.name', string="Dealer Name")