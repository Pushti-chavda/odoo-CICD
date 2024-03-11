# -*- coding: utf-8 -*-
""" Create/Manage the Log Lines for process """

import logging
from odoo import fields, models

_LOGGER = logging.getLogger(">>> Common Process Logs <<<")


class CommonProcessLogLines(models.Model):
    """
        Create/Manage the Log Lines for process
    """
    _name = "common.process.log.lines"
    _description = "Common Process Log Lines"

    process_log_id = fields.Many2one(comodel_name='common.process.log', string='Process Log', ondelete='cascade',
                                     readonly=True)
    message = fields.Text(string="Message")
    description = fields.Text(string="Line Description")
    sale_order_line_id = fields.Many2one(comodel_name='sale.order.line', string='Sale Order Line', ondelete='cascade',
                                         copy=False)
    stock_move_id = fields.Many2one(comodel_name='stock.move', string='Stock Move', ondelete='cascade',
                                    copy=False)
    account_move_id = fields.Many2one(comodel_name='account.move', string='Invoice', ondelete='cascade',
                                      copy=False)
    response = fields.Text(string="API Response", copy=False)

    def prepare_common_process_log_line_values(self, process_log_book, **kwargs):
        values = {
            'process_log_id': process_log_book.id,
            'default_code': kwargs.get('default_code') if kwargs.get('default_code') else '',
            'description': kwargs.get('description') if kwargs.get('description') else '',
        }
        for field_name in kwargs:
            if hasattr(self, field_name):
                values.update({field_name: kwargs.get(field_name, False)})
        _LOGGER.info(f"Common Process Log Lines Values: [{values}]")
        return values
