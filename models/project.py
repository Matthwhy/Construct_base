from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class Task(models.Model):
    """Added Material and Equipment Used in the Project Task."""

    _inherit = "project.task"


    material_ids = fields.One2many(
        comodel_name='project.task.material', inverse_name='task_id',
        string='Material Used'
    )

    
    equipment_ids = fields.One2many(
        comodel_name='project.task.equipment', inverse_name='task_id',
        string='Equipments Used'
    )

    collaborator_ids = fields.Many2many(
        comodel_name='hr.employee',
        string='Collaborators'
    )


class ProjectTaskMaterial(models.Model):
    """Added Product and Quantity in the Task Material Used."""

    _name = "project.task.material"
    _description = "Task Material Used"

    task_id = fields.Many2one(
        comodel_name='project.task', string='Task', ondelete='cascade',
        required=True
    )
    product_id = fields.Many2one(
        comodel_name='product.product', string='Product', required=True
    )
    quantity = fields.Float(string='Quantity')

    @api.constrains('quantity')
    def _check_quantity(self):
        for material in self:
            if not material.quantity > 0.0:
                raise ValidationError(
                    _('Quantity of material consumed must be greater than 0.')
                )


class ProjectTaskEquipment(models.Model):
    """Added Equipment and Quantity in the Task Equipment Used."""

    _name = "project.task.equipment"
    _description = "Task Equipment Used"

    task_id = fields.Many2one(
        comodel_name='project.task', string='Task', ondelete='cascade',
        required=True
    )
    equipment_id = fields.Many2one(
        comodel_name='product.product', string='Equipment', required=True
    )
    quantity = fields.Float(string='Quantity')
    usage_date = fields.Date(string="Usage Date", required=True)
    operator_id = fields.Many2one(
        comodel_name='hr.employee', string='Operator', required=True)

    @api.constrains('quantity')
    def _check_quantity(self):
        for equipment in self:
            if not equipment.quantity > 0.0:
                raise ValidationError(
                    _('Quantity of equipment used must be greater than 0.')
                )
