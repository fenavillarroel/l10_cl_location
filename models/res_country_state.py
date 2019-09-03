from odoo import fields, models, api

class ResCountryState(models.Model):
    _name = 'res.country.state'
    _description = "Res Country State"
    _inherit = 'res.country.state'
    _order = 'name asc'

    id_provincia = fields.Many2one('res.country.provincias', 'Provincia')
    
