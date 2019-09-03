from odoo import fields, models, api

class ResCountryRegion(models.Model):
    _name = 'res.country.region'
    _description = "Res Country Regiones"
    _order = 'name asc'

    name = fields.Char(string='Nombre',size=128)
    code = fields.Char(string='Código',size=28) 
