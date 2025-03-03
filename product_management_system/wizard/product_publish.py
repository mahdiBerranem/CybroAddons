# -*- coding: utf-8 -*-
################################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    Author: Cybrosys Technologies (<https://www.cybrosys.com>)
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
################################################################################
from odoo import fields, models


class ProductPublish(models.TransientModel):
    """
        Model for making products publish on website
    """
    _name = 'product.publish'
    _description = 'Publish Products'

    product_ids = fields.Many2many('product.template',
                                   string='Selected Products',
                                   readonly=True,
                                   help='Products which are selected to '
                                        'update publish detail')

    def action_publish_product(self):
        """
        Function for making selected products publish on website
        """
        for products in self.product_ids:
            products.write({'is_published': True})

    def action_not_publish_product(self):
        """
        Function for not making selected products publish on website
        """
        for products in self.product_ids:
            products.write({'is_published': False})
