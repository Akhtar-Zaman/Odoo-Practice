from odoo import models, fields, api, _
from datetime import date




class HospitalDoctors(models.Model):
    _name = 'hospital.doctors'
    _rec_name = 'doc_name'

    doc_name = fields.Char('Name')
    doc_age = fields.Integer('Age')


    doc_patients = fields.One2many('hospital.patients', 'pat_doctor', string="Patients")
    doc_category = fields.Many2one('hospital.doctor.category', string='Department')


    def Patient_Appointments(self):

        return {
            'name': "Appointments",
            'type': "ir.actions.act_window",
            'res_model': "patient.filter",
            'view_mode': "form",
            'target': "new",
            'context': {'default_doc_namee': self.id}
        }

