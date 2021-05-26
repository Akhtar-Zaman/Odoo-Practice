from odoo import models, fields, api, _

class Datewise_Patients_Filter(models.TransientModel):
    _name = 'wizard.patients.filter'

    doc_id = fields.Many2one('hospital.doctors')
    date_from = fields.Date("From")
    date_to = fields.Date("To")  
 

    def patients_filter(self):
        return {
            'name': "Patients",
            'type': "ir.actions.act_window",
            'res_model': "hospital.patients",
            'view_mode': "tree,form",
            'domain': ['&', ('appointment_date', '>=', self.date_from), ('appointment_date', '<=', self.date_to),('pat_doctor', '=', self.doc_id.id)]
        }

