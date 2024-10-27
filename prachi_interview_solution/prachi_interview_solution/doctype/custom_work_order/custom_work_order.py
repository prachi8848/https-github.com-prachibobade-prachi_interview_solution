# Copyright (c) 2024, Prachi and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc
from frappe.utils import flt, cint  # Import flt and cint for float and integer conversions
from erpnext.stock.doctype.item.item import get_item_defaults
from erpnext.setup.doctype.item_group.item_group import get_item_group_defaults


class CustomWorkOrder(Document):
	pass
	


@frappe.whitelist()
def custom_work_order_function(sales_order):
    # Fetch Sales Order details
    sales_order_doc = frappe.get_doc("Sales Order", sales_order)

    # Create a new Custom Work Order linked to the Sales Order
    work_order = frappe.get_doc({
        "doctype": "Custom Work Order", 
        "sales_order": sales_order,  # Link to the Sales Order
        "customer": sales_order_doc.customer,  # Fetch customer from Sales Order
        "order_type": sales_order_doc.order_type,  # Fetch order_type from Sales Order
        "transaction_date": sales_order_doc.transaction_date,  # Fetch transaction_date from Sales Order
        "status": "Draft"
    })
    
    # Loop through the Sales Order Items and append to Custom Work Order Items
    for item in sales_order_doc.items:
        work_order.append("items", {
            "item_code": item.item_code,
            "customer_item_code": item.customer_item_code,
            "delivery_date": item.delivery_date,
            "item_name": item.item_name,
            "item_group": item.item_group,
            "qty": item.qty,
            "uom": item.uom,
            "rate": item.rate,
            "amount": item.amount,
            "description": item.description,  # Add description
            "conversion_factor": item.conversion_factor  # Add conversion_factor
        })

    # Insert the Work Order into the database
    work_order.insert()  
    frappe.db.commit()  # Ensure the transaction is saved

    # Return the name of the new Work Order so that it can be opened
    return work_order.name





@frappe.whitelist()
def make_sales_invoice(source_name, target_doc=None, ignore_permissions=False):
    def update_item(source, target, source_parent):
        target.amount = flt(source.amount) - flt(source.billed_amt)
        target.base_amount = target.amount * flt(source_parent.conversion_rate)
        target.qty = (
            target.amount / flt(source.rate)
            if (source.rate and source.billed_amt)
            else source.qty - source.returned_qty
        )

        if source_parent.project:
            target.cost_center = frappe.db.get_value("Project", source_parent.project, "cost_center")
        if target.item_code:
            item = get_item_defaults(target.item_code, source_parent.company)
            item_group = get_item_group_defaults(target.item_code, source_parent.company)
            cost_center = item.get("selling_cost_center") or item_group.get("selling_cost_center")

            if cost_center:
                target.cost_center = cost_center

    doclist = get_mapped_doc(
        "Sales Order",
        source_name,
        {
            "Sales Order": {
                "doctype": "Custom Work Order",
                "field_map": {
                    "party_account_currency": "party_account_currency",
                    "payment_terms_template": "payment_terms_template",
                },
                "field_no_map": ["payment_terms_template"],
                "validation": {"docstatus": ["=", 1]},
            },
           "Sales Order Item" : {
                "doctype": "Custom Work Order Item",
                "field_map": {
                    "name": "so_detail",
                    "parent": "sales_order",
                },
                "postprocess": update_item,
                "condition": lambda doc: doc.qty
                and (doc.base_amount == 0 or abs(doc.billed_amt) < abs(doc.amount)),
            },
            
        },
        target_doc,
        ignore_permissions=ignore_permissions,
    )

    
    return doclist

import json
@frappe.whitelist()
def accept_sample_json(sample_json):
    sample_json = json.loads(sample_json)
    
    if frappe.request.method == "POST":
        address = frappe.new_doc("Address")
        address.update({
            "address_title": sample_json.get("customer_name"),
            "address_line1": sample_json.get("address_line1"),
            "address_line2": sample_json.get("address_line2"),
            "pincode": sample_json.get("pincode"),
            "city": sample_json.get("city"),
            "state": sample_json.get("state"),
            "country": sample_json.get("country"),
            "email_id": sample_json.get("email_address"),
            "phone": sample_json.get("mobile_number"),
        })
        address.save()

        # Create  Customer
        customer = frappe.new_doc("Customer")
        customer.update({
            "customer_name": sample_json.get("customer_name"),
            "customer_type": "Company",
            "customer_group": "Commercial",
            "territory": "All Territories",
        })
        customer.save()
		
       
        address.append("links", {"link_doctype": "Customer", "link_name": "Prachi"})
        address.save()
        return address.as_dict()
        return customer.as_dict()
    if frappe.request.method == "PUT":
        address = frappe.db.get_value("Dynamic Link", {"link_doctype": "Customer", "link_name": sample_json.get("customer_name"), "parenttype": "Address"}, "parent")
        if address:
            address = frappe.get_doc("Address", address)
            address.update({
                "address_title": sample_json.get("customer_name"),
                "address_line1": sample_json.get("address_line1"),
                "address_line2": sample_json.get("address_line2"),
                "pincode": sample_json.get("pincode"),
                "city": sample_json.get("city"),
                "state": sample_json.get("state"),
                "country": sample_json.get("country"),
                "email_id": sample_json.get("email_address"),
                "phone": sample_json.get("mobile_number"),
            })
            address.save()
            return address.as_dict()
           