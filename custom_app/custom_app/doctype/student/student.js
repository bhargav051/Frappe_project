// Copyright (c) 2024, Bhargav and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Student", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on("Student", {

    refresh(frm) {
        // frappe.call({
        //     method: 'custom_app.custom_app.doctype.student.student.update_record',
        //     args: {
        //         doc_id: 'Bhargav-2024-06-13-0009',
        //         new_firstName: 'Raghav'
        //     },
        //     callback: function (res) {
        //         console.log(res);
        //     }
        // })
    },

    address: function (frm) {
        if (frm.doc.address) {
            frappe.call({
                method: "frappe.client.get",
                args: {
                    doctype: "Address",
                    name: frm.doc.address
                },
                callback: function (r) {
                    if (r.message) {

                        frm.fields_dict['combined_address'].html('<p>' + r.message.address_line1 + '<span>,</span>' +
                            r.message.address_line2 + '<span>,</span> ' +
                            r.message.city + '<span>,</span> ' +
                            r.message.state + ' <span>,</span>' +
                            r.message.country + ' <span>,</span>' +
                            r.message.pincode + '</p>');
                    }
                }
            });
        }
    },

    onload_post_render(frm) {
        if (frm.doc.joining_date === undefined) {
            var currentDate = new Date();
            var year = currentDate.getFullYear();
            var month = currentDate.getMonth() + 1;
            var day = currentDate.getDay();
            var joiningDate = year + "-" + month + "-" + day;
            frm.set_value("joining_date", joiningDate);
        }
    },
    create_user: function (frm) {
        frm.save()
            .then(() => {
                frappe.msgprint(__('Document saved successfully.'));
            })
            .catch((error) => {
                frappe.msgprint({
                    title: __('Error'),
                    indicator: 'red',
                    message: __('There was an error saving the document: ') + error.message
                });
            });
    }
})