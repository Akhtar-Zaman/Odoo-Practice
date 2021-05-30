from odoo import models, fields, api, _


class DoctorsPrescription(models.Model):
    _name = 'doctors.prescription'
    _rec_name = 'Patient_name'


    Patient_name = fields.Char("Patinet Name", readonly=True)
    Patient_email = fields.Char("Patinet Email", readonly=True)
    Patient_doctor = fields.Char("Patinet Doctor", readonly=True)

    Patient_medicines = fields.One2many('doctors.prescription.line', 'Prescription_id')



    

class DoctorsPrescriptionLine(models.Model):
    _name = 'doctors.prescription.line'

    medicines = fields.Many2one('hospital.medicines')
    morning = fields.Boolean('Morning')
    afternoon = fields.Boolean('Afternoon')
    evening = fields.Boolean('Evening')
    days = fields.Char('Days')
    notes = fields.Text('notes')


    medicine_price = fields.Integer('price', related='medicines.mdcn_price')
    # doc_group = fields.Integer('Group', related='medicines.mdcn_price')

    Prescription_id = fields.Many2one('doctors.prescription')