# Copyright (c) 2024, Bhargav and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class LibraryMember(Document):
	def before_save(self):
		self.full_name= f'{Self.first_name} {self.last_name or ""}'
