from odoo import models, fields, api, _
from odoo.exceptions import UserError


class purchasefilter(models.TransientModel):
    _name = 'purchase.filter'

    date_from = fields.Date("From")
    date_to = fields.Date("To")    

    def purchsae_filter(self):
        a = []
        b = []
        dd = self.env['purchase.order.line'].search([])
        kk = self.env['purchase.order'].search([ '&', ('date_approve', '>=', self.date_from), ('date_approve', '<=', self.date_to)])
        for i in kk:
            b.append(i.id)

        for i in dd:   
            if i.qty_received >= 0 and  i.qty_invoiced < i.qty_received:
                a.append(i.order_id.id)

                list1_as_set = set(a)
                intersection = list1_as_set.intersection(b)
                intersection_as_list = list(intersection)

        return {
            'name': "purchase filter",
            'type': "ir.actions.act_window",
            'res_model': "purchase.order",
            'view_mode': "tree,form",
            'domain': [('id','in', intersection_as_list)],
        }
