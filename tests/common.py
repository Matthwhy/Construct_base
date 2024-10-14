

from odoo.tests.common import TransactionCase


class TestProjectCases(TransactionCase):
    """Prepare data to test the module."""

    def setUp(self):
        """Create user, task, project as well as refre action of the user."""
        super(TestProjectCases, self).setUp()


        self.project_user = self.env["res.users"].create({
            "company_id": self.env.ref("base.main_company").id,
            "name": "matheus Project User",
            "login": "mpu",
            "email": "mpu@yourcompany.com",
            "groups_id": [(6, 0, [self.ref('project.group_project_user')])]
        })


        self.task = self.env.ref('project.project_task_2')
        self.product = self.env.ref('product.consu_delivery_03')


        self.action = self.task.sudo(self.project_user.id)
