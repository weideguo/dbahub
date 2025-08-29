"""
pip install nicegui
python nicegui_demo.py

# https://nicegui.io/documentation/
"""

from nicegui import ui

ui.label('Hello NiceGUI!')

ui.run(host="0.0.0.0", port=8000)
