# Copyright (c) 2024, Bhargav and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Test(Document):
	def before_save(self):
		self.full_name=f'{self.first_name} {self.last_name}'
		frappe.throw(f'{self.first_name} {self.last_name}')

# In your_app/your_app/doctype/your_doctype/your_doctype.py

@frappe.whitelist()
def get_greeting():
    return f"Hello!"
