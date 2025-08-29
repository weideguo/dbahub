from nicegui import ui


continents = [
    "Asia",
    "Africa",
    "Antarctica",
    "Europe",
    "Oceania",
    "North America",
    "South America",
]


#select = ui.select(options=continents, with_input=True, on_change=lambda e: update_select_item(e.value))
select = ui.select(options=continents, with_input=True)


date_input = ui.input("开始日期")

with ui.menu().props("no-parent-event") as menu:
    with ui.date().bind_value(date_input):
        with ui.row().classes("justify-end"):
            ui.button("确定", on_click=menu.close).props("flat")

with date_input.add_slot("append"):
    ui.icon("edit_calendar").on("click", menu.open).classes("cursor-pointer")



def update():
    ui.notify(select.value)
    ui.notify(date_input.value)


ui.button("刷新", on_click=update)


ui.run(host="0.0.0.0", port=8000)
