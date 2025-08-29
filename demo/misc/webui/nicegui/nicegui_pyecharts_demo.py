from nicegui import ui
from pyecharts.charts import Bar
from pyecharts.commons.utils import JsCode
from pyecharts.options import AxisOpts
from random import random

ratio_data = [1, 2, 4]

# 通过 @ui.refreshable 实现重新渲染
@ui.refreshable
def echart_ui():
    ui.echart.from_pyecharts(
        Bar()
        .add_xaxis(['A', 'B', 'C'])
        .add_yaxis('ratio', ratio_data)
        .set_global_opts(
            xaxis_opts=AxisOpts(axislabel_opts={
                ':formatter': r'(val, idx) => `group ${val}`',
            }),
            yaxis_opts=AxisOpts(axislabel_opts={
                'formatter': JsCode(r'(val, idx) => `${val}%`'),
            }),
        )
    )

def update():
    ratio_data[0] = int(random()*10)
    echart_ui.refresh()

echart_ui()
ui.button('Update', on_click=update)

ui.run(host="0.0.0.0", port=8000)