# avocado_system/config/desktop.py
from frappe import _

def get_data():
    return [
        {
            "module_name": "Avocado Procurement",
            "type": "module",
            "label": _("Avocado Procurement"),
            "icon": "octicon octicon-package",
            "color": "#63d3ff",
            "link": "modules/Avocado Procurement",
            "description": "Track farmers, deliveries, quality, and more.",
        }
    ]
