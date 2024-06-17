# Copyright (c) 2024, Bhargav and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime	


class Student(Document):

	def before_save(self):
		self.full_name = f'{self.first_name} {self.middle_name or ""} {self.last_name or ""}'
		dob = datetime.strptime(self.date_of_birth, "%Y-%m-%d")
		joining = datetime.strptime(self.joining_date, "%Y-%m-%d")
		today = datetime.today()
		if dob>today :
			frappe.throw("Date of Birth cannot be in future")	
		if joining<dob : 
			frappe.throw("Joining Date cannot be before Date of Birth")	

@frappe.whitelist()
def update_record(doc_id,new_firstName):
	doc = frappe.get_doc('Student',doc_id)
	doc.first_name = new_firstName
	return doc

# def update_record(doc_id,new_firstName):
# 	doc = frappe.get_doc('Student',doc_id)
# 	doc.first_name = new_firstName
# 	return doc



		
		