from odoo import models, fields, api


class home_work(models.Model):
    _name = 'home_work.home_work'
    _description = 'home_work.home_work'
    name = fields.Char()
    description = fields.Text()
    Ner = fields.Char()
    value = fields.Integer()
    time = fields.Datetime()
    teme = fields.Datetime()
    image = fields.Binary(string="Image")
    days = fields.Text(compute="_value_pc", store=True)
    hours = fields.Text(compute="_value_pc", store=True)
    minutes = fields.Text(compute="_value_pc", store=True)

    @api.depends('time', 'teme')
    def _value_pc(self):
        for record in self:
            record.days = (record.teme-record.time).days
            record.hours = (record.teme-record.time).seconds / 3600
            record.minutes = (record.teme-record.time).seconds % 3600 / 60
