# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from odoo.exceptions import UserError

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    is_created = fields.Boolean()

class SaleOder(models.Model):
    _inherit = 'sale.order'

    @api.onchange('order_line')
    def onchange_product_id(self):
        for rec in self.order_line:
            if not rec.is_created:
                if rec.product_id.additional_product:
                    rec_list = []
                    rec_list.append((0, 0, {
                        'product_id': rec.product_id.additional_product.id,
                         'name': rec.product_id.additional_product.name,
                         'product_uom': rec.product_id.additional_product.uom_id.id,
                         'product_uom_qty': 1,
                         'price_unit': rec.product_id.additional_product.lst_price,
                        'is_created': True,
                    }))
                    rec.is_created = True
                    self.order_line = rec_list

class ProductTemplateInh(models.Model):
    _inherit = 'product.template'

    additional_product = fields.Many2one('product.product', string="Extra Product")
