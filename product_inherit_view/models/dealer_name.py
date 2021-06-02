from odoo import models, fields, api, _

class Dealer_Name(models.Model):
    _name = 'dealer.name'
    _descrption = 'Dealer name for Products in sale'
    _rec_name = 'Dealer_Name'


    Dealer_Name = fields.Char(string="Dealer Name")           


