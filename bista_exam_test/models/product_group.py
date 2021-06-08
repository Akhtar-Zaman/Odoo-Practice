
from odoo import models, fields, api, _
from odoo.exceptions import UserError


class ProductGroup(models.Model):
    _name = 'product.group'
    _rec_name = 'name'


    name = fields.Char('Name', required=True)
    short_code = fields.Char('Short Code', required=True)

    parent_group = fields.Many2one('product.group', string='Parent Group')


#######################  Code Validation Check ###################################################
    @api.onchange('short_code')
    def onchange_code(self):
        exist = self.env['product.group'].search([])
        if self.short_code:
            for i in exist:
                if self.short_code == i.short_code:
                    raise UserError(_("This short_code Already exist"))


    def write(self, values):
        short_code_exist = self.env ['product.group'].search([('short_code', '=', values['short_code'])])
        if short_code_exist:
            raise UserError(_("This short_code Already exist"))
        result = super(ProductGroup, self).write(values)
        return result

    @api.model 
    def create(self, values):
        short_code_exist = self.env ['product.group'].search([('short_code', '=', values['short_code'])])
        if short_code_exist:
            raise UserError(_("This short_code Already exist"))
        result = super(ProductGroup, self).create(values)
        return result


