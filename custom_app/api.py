import frappe
from frappe import _

@frappe.whitelist()
def handle_request():
    """
    Handle different HTTP methods (GET, POST, DELETE, UPDATE) on a single URL.
    """
    method = frappe.local.request.method

    if method == "GET":
        return get_tasks()
    elif method == "POST":
        return create_record()
    elif method == "PUT":
        return update_record()
    elif method == "DELETE":
        return delete_record()
    else:
        return {"error": "Invalid request method"}, 405

def get_tasks():
    """
    Fetch tasks and include child data if any.
    """
    doctype = frappe.local.form_dict.get('doctype')
    name = frappe.local.form_dict.get('name')  # Add name to get a specific document

    if not doctype:
        return {"error": "doctype is required"}, 400

    try:
        if name:
            # Fetch a specific document along with its child data
            document = frappe.get_doc(doctype, name)
            return document.as_dict()
        else:
            # Fetch all documents of a doctype
            records = frappe.get_all(doctype, fields=["name"])
            detailed_records = []

            for record in records:
                doc = frappe.get_doc(doctype, record.name)
                detailed_records.append(doc.as_dict())

            return detailed_records

    except Exception as e:
        return {"error": str(e)}, 500

def create_record():
    data = frappe.local.form_dict
    doctype = data.get('doctype')
    if not doctype:
        return {"error": "doctype is required"}, 400

    try:
        doc = frappe.get_doc({
            "doctype": doctype,
            **data
        })
        doc.insert()
        return doc.as_dict()
    except Exception as e:
        return {"error": str(e)}, 500

def update_record():
    data = frappe.local.form_dict
    doctype = data.get('doctype')
    name = data.get('name')
    if not doctype or not name:
        return {"error": "doctype and name are required"}, 400

    try:
        doc = frappe.get_doc(doctype, name)
        doc.update(data)
        doc.save()
        return doc.as_dict()
    except Exception as e:
        return {"error": str(e)}, 500

def delete_record():
    data = frappe.local.form_dict
    doctype = data.get('doctype')
    name = data.get('name')
    if not doctype or not name:
        return {"error": "doctype and name are required"}, 400

    try:
        frappe.delete_doc(doctype, name)
        return {"message": f"Record {name} deleted successfully"}
    except Exception as e:
        return {"error": str(e)}, 500