# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: JANISH BABU (<https://www.cybrosys.com>)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
from odoo import api, models


class MrpBom(models.Model):
    """Class for inherited model mrp.bom.
    Methods:
        get_views(self, views, options=None):
            Function to make print button invisible according to the boolean
            field in res.users.
    """
    _inherit = 'mrp.bom'

    @api.model
    def get_views(self, views, options=None):
        """ Function to make print button invisible according to the
            boolean field in res.users.
            views(list): List of views and ids
            options(dict): Dictionary of action_id,load_filters,and toolbar
            boolean:returns true.
        """
        res = super().get_views(views, options)
        if self.env.user.hide_mrp_print and self.env.user.hide_mrp_bom_print:
            for view in ['form', 'list']:
                if res['views'].get(view, {}) and res['views'].get(
                        view, {}).get('toolbar').get('print', []):
                    res['views'].get(view, {}).get('toolbar').get('print',
                                                                  []).clear()
        return res
