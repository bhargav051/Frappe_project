// Copyright (c) 2024, Bhargav and contributors
// For license information, please see license.txt

frappe.ui.form.on("Program", {
    validate: function (frm) {
        let total_credit = 0;
        arrDatas = frm.doc["course_connection"];
        for (data of arrDatas) {
            total_credit += parseFloat(data['course_credit']);
        }
        console.log(total_credit);
        frm.doc.total_credits = total_credit;
        console.log(frm.doc)
    }
});
