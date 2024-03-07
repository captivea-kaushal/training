from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    product_tmpl_ids = fields.Many2many('product.template', string='Product Template Tags')

    @api.onchange('product_tmpl_ids')
    def add_product_variants(self):
        product_templates = self.env['product.template'].search([('id', 'in', self.product_tmpl_ids.ids)])
        print('product_templates :',product_templates)
        product_variants = self.env['product.product'].search([('product_tmpl_id', 'in', product_templates.ids)])
        print('product_variants :', product_variants)

        if self.ids and product_variants:
            existing_variants = self.order_line.filtered(lambda x: x.product_id.id in product_variants.ids)
            print('existing_variants :', existing_variants)
            existing_variant_ids = existing_variants.mapped('product_id.id')
            print('existing_variant_ids :', existing_variant_ids)

            for variant in product_variants:
                print('variant :', variant)
                if variant.qty_available != 0 and variant.id not in existing_variant_ids:
                    self.order_line.create({'order_id': self.ids[0],
                                            'product_id': variant.id,
                                            'name': variant.display_name,
                                            'product_uom_qty': 1,
                                            'price_unit': variant.list_price,})