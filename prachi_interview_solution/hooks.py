from . import __version__ as app_version

app_name = "prachi_interview_solution"
app_title = "prachi_interview_solution"
app_publisher = "prachi_interview_solution"
app_description = "prachi_interview_solution"
app_email = "prachibobade09@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/prachi_interview_solution/css/prachi_interview_solution.css"
# app_include_js = "/assets/prachi_interview_solution/js/prachi_interview_solution.js"

# include js, css files in header of web template
# web_include_css = "/assets/prachi_interview_solution/css/prachi_interview_solution.css"
# web_include_js = "/assets/prachi_interview_solution/js/prachi_interview_solution.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "prachi_interview_solution/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "prachi_interview_solution.utils.jinja_methods",
#	"filters": "prachi_interview_solution.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "prachi_interview_solution.install.before_install"
# after_install = "prachi_interview_solution.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "prachi_interview_solution.uninstall.before_uninstall"
# after_uninstall = "prachi_interview_solution.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "prachi_interview_solution.utils.before_app_install"
# after_app_install = "prachi_interview_solution.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "prachi_interview_solution.utils.before_app_uninstall"
# after_app_uninstall = "prachi_interview_solution.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "prachi_interview_solution.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"prachi_interview_solution.tasks.all"
#	],
#	"daily": [
#		"prachi_interview_solution.tasks.daily"
#	],
#	"hourly": [
#		"prachi_interview_solution.tasks.hourly"
#	],
#	"weekly": [
#		"prachi_interview_solution.tasks.weekly"
#	],
#	"monthly": [
#		"prachi_interview_solution.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "prachi_interview_solution.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "prachi_interview_solution.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "prachi_interview_solution.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["prachi_interview_solution.utils.before_request"]
# after_request = ["prachi_interview_solution.utils.after_request"]

# Job Events
# ----------
# before_job = ["prachi_interview_solution.utils.before_job"]
# after_job = ["prachi_interview_solution.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"prachi_interview_solution.auth.validate"
# ]

doctype_js = {
	
	"Sales Order": "public/js/doctype_js/sales_order.js",
	
}

fixtures = [
	{"dt": "Workflow", "filters": [
            [
                "name", "in", [
                    "Timesheet Workflow",
                    ]
            ]
        ]
    },
    {"dt": "Role", "filters": [
            [
                "name", "in", [
                    "Timesheet User","Timesheet Manager",
                    ]
            ]
        ]
    },
    
    {"dt": "Workflow State", "filters": [
			[
				"name", "in", [
					"Draft","Pending Approval","Need Modification",
				]
			]
    	]},

        
    
    ]