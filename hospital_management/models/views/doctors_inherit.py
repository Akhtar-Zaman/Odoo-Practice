from odoo import models, fields, api, _



class DoctorInherit(models.Model):
    _inherit = 'hospital.doctors'


    Specialization = fields.Many2one('hospital.doctor.category', string='Specialized In')
