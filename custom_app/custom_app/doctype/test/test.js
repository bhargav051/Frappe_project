// Copyright (c) 2024, Bhargav and contributors
// For license information, please see license.txt

frappe.ui.form.on("Test", {
    refresh(frm) {
        frappe.call({
            method: 'custom_app.custom_app.doctype.test.test.get_greeting',
            callback: function (response) {
                console.log(response);
            }
        })
    }
});

