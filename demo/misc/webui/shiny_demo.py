"""
pip install shiny
shiny create --template template_type

template_type:
basic-app


shiny create --template basic-app
cd basic-app
pip install -r requirements.txt

shiny run app.py
--host
--port

# 不使用模板
shiny run shiny_demo.py


# 组件参考 
https://shiny.posit.co/py/components/
"""


from shiny.express import input, render, ui

ui.input_slider("n", "N", 0, 100, 20)


@render.code
def txt():
    return f"n*2 is {input.n() * 2}"







