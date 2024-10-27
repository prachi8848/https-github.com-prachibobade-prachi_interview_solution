frappe.ui.form.on("Custom Work Order", {
    refresh: function(frm) {
        // Adding a custom button to get items from Sales Order using custom_management app
        frm.add_custom_button(__('Sales Order'), function() {
            erpnext.utils.map_current_doc({
                method: "prachi_interview_solution.prachi_interview_solution.doctype.custom_work_order.custom_work_order.make_sales_invoice",
                source_doctype: "Sales Order",
                target: frm,
                setters: {
                    customer: frm.doc.customer || undefined,
                },
                get_query_filters: {
                    docstatus: 1,
                    status: ["not in", ["Closed", "On Hold"]],
                    company: frm.doc.company
                }
            });
        }, __("Get Items From"));
    }
});

