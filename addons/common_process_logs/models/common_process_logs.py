# -*- coding: utf-8 -*-
""" Create/Manage the Logs for process """
import logging
from odoo import fields, models, _

_LOGGER = logging.getLogger(">>> Common Process Logs <<<")

OPERATION_TYPE = [('import', 'Import'),
                  ('export', 'Export'), ]


class CommonProcessLogs(models.Model):
    """
        Create/Manage the Logs for process
    """
    _name = "common.process.log"
    _description = "Common Process Logs"
    _order = 'id desc'

    name = fields.Char(string='Name', required=True, copy=False, readonly=True, index=True,
                       default=lambda self: _('New'))
    line_ids = fields.One2many(comodel_name='common.process.log.lines', inverse_name='process_log_id',
                               string='Log Lines')
    message = fields.Text(string="Message")
    res_model = fields.Selection(string="Model", selection=[('none', "No Model Set")], default='none', required=True)
    account_move_id = fields.Many2one('account.move', string='Invoice')

    def prepare_common_process_log_values(self, operation_type='import', message="", **kwargs):
        values = {
            'operation_type': operation_type,
            'name': self.env['ir.sequence'].sudo().next_by_code('common.process.log') or _('New'),
            'message': message
        }
        for field_name in kwargs:
            if hasattr(self, field_name):
                values.update({field_name: kwargs.get(field_name, False).id})
        _LOGGER.info(f"Common Process Log Values: [{values}]")
        return values
