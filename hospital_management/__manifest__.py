
{
    'name' : 'Hospital Management System',
    'version' : '14.0',
    'summary': '',
    'sequence': 1,
    'description': '',
    'category': '',
    'website': 'https://www.odoo.com',
    'depends' : [
    ],
    'data': [
        # Security
        'security/Hospital_Groups.xml',
        'security/ir.model.access.csv',

        # Views
        'views/Doctors.xml',
        'views/Patients.xml',
        'views/Doctors_Category.xml',
        'views/Medicines.xml',
        'views/Prescription.xml',
        #'views/Doctors_Inherit.xml',

        # Wizard
        'views/wizard/wizard_patient_filter_doctor.xml',
        
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
