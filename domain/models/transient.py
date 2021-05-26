
from odoo import models, fields, api, _



class PatientTransient(models.TransientModel):
    _name = 'patient.filter'

    doc_namee = fields.Char('h')
    date_from = fields.Date('From')
    date_to = fields.Date('To')


    def object(self):  
        print("##############khan################", self.doc_namee)  
        return {
            'name': "Appointments",
            'type': "ir.actions.act_window",
            'res_model': "hospital.patients",
            'view_mode': "tree,form",
            #'domain': ['&', ('appointment_date', '>=', self.date_from), ('appointment_date', '<=', self.date_to), ('pat_doctor','=', self.doc_namee.id)], 
        }
