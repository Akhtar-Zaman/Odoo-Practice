from odoo import models, fields, api, _


class ProductRequisition(models.Model):
    _name = 'product.requisition'
    _rec_name = 'id'


    employee = fields.Many2one('hr.employee', string="Employee")
    requisition_date = fields.Date('Date')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('approved', 'Approved'),
        ('ready', 'Ready'),
        ('received', 'Received')], default='draft', string='Status', readonly=True)

    requisition_order = fields.One2many('product.requisition.line', 'product_requisition_id')


    def action_confirm(self):
        for i in self:
            i.state= 'confirm'

    def action_approved(self):
        for i in self:
            i.state= 'approved'

    def action_ready(self):
        for i in self:
            i.state= 'ready'

    def action_received(self):
        for i in self:
            i.state= 'received'


class ProductRequisitionLine(models.Model):
    _name = 'product.requisition.line'


    product= fields.Many2one('product.template', string="Product")
    product_requisition_id = fields.Many2one('product.requisition')
    quantity = fields.Float('Quantity')