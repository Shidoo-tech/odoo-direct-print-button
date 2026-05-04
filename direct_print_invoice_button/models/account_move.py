# -*- coding: utf-8 -*-
from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    def action_open_invoice_tab(self):
        """هذه الدالة تفتح تقرير الفاتورة في تبويب جديد كملف PDF"""
        self.ensure_one()
        # الرابط المباشر لتقرير PDF مع منع التحميل التلقائي
        report_url = f'/report/pdf/account.report_invoice_with_payments/{self.id}?download=false'
        
        return {
            'type': 'ir.actions.act_url',
            'url': report_url,
            'target': 'new',
        }