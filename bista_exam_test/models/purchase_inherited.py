
from odoo import models, fields, api, _

class Purchse_Inher(models.Model):
    _inherit = 'purchase.order'

    product_group = fields.Many2one('product.group', string="Product Group")
    active_product_group = fields.Boolean('Active Group Filter')

class Purchase_Inherited_line(models.Model):    
    _inherit = 'purchase.order.line'

    product_ratings = fields.Many2one('product.template')
    ratings = fields.Selection('Ratingssssssssss', related='product_id.product_rating')
    


class purchasefilter(models.TransientModel):
    _name = 'purchase.filter'

    # customers = fields.Many2one('res.partner', string='Customers')
    customers = fields.Many2many('res.partner', string='Customers')

    def purchsae_filter(self):

        return {
            'name': "purchase filter",
            'type': "ir.actions.act_window",
            'res_model': "purchase.order",
            'view_mode': "tree,form",
            'domain': [('partner_id.id','in', self.customers.ids)],
        }
  