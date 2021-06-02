from odoo import models, fields, api, _

class Dealer_Name(models.Model):
    _name = 'product.brand'
    _descrption = 'Product brandfor Products in sale'
    _rec_name = 'Product_brand'


    Product_brand = fields.Char(string="Product Brand")  