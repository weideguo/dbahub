from nicegui import ui


m = ui.leaflet(center=(23.100, 113.296))
ui.label().bind_text_from(m, 'center', lambda center: f'Center: {center[0]:.3f}, {center[1]:.3f}')
ui.label().bind_text_from(m, 'zoom', lambda zoom: f'Zoom: {zoom}')

with ui.grid(columns=2):
    ui.button('guangzhou', on_click=lambda: m.set_center((23.100, 113.296)))
    ui.button('shenzhen', on_click=lambda: m.set_center((22.551, 114.000)))
    ui.button(icon='zoom_in', on_click=lambda: m.set_zoom(m.zoom + 1))
    ui.button(icon='zoom_out', on_click=lambda: m.set_zoom(m.zoom - 1))



ui.run(host="0.0.0.0", port=8000)
