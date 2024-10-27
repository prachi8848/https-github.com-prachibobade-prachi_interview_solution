
frappe.ui.form.on("Sales Order", {
    refresh: function(frm) {
        // Add custom button
        frm.add_custom_button(__('Custom Work Order'), function() {
            // Call the Python function using frappe.call
            frappe.call({
                method: "prachi_interview_solution.prachi_interview_solution.doctype.custom_work_order.custom_work_order.custom_work_order_function",
                args: {
                    sales_order: frm.doc.name // Pass the Sales Order name
                },
                callback: function(r) {
                    if (r.message) {
                        // Redirect to the newly created Work Order
                        frappe.set_route("Form", "Custom Work Order", r.message);
                    }
                }
            });
        }, __('Create'));
    },
});
