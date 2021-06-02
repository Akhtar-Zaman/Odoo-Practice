
from odoo import models, fields, api, _
from odoo.exceptions import UserError

class Purchse_Inher(models.Model):
    _inherit = 'purchase.order'

    Dealers = fields.Many2one('dealer.name', string="Dealer")





##################################################################################################
class Purchase_Inherited_line(models.Model):    
    _inherit = 'purchase.order.line'
    Brand = fields.Many2one('product.brand', string="Brand", readonly=True)
    Dealer = fields.Many2one('dealer.name', string="Dealer")


    Brand_name = fields.Many2one('product.brand', string="Brand Name", related='product_id.product_brand')

    # @api.onchange('product_id')
    # def onchange_test(self):
    #     if self.product_id:
    #         self.Brand = self.product_id.product_brand.id

    # def write(self, values):
    #     values['Brand'] = self.product_id.product_brand.id
    #     return super(Purchase_Inherited_line, self).write(values)










  