"""
实现在web页面数据展示

运行
streamlit run streamlit_demo.py 

api参考文档
https://docs.streamlit.io/library/api-reference
"""

import streamlit as st

st.markdown("""
# 可以使用markdown
> 可以跨行
""")

st.text("可以用latex")
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')
    
st.divider()

# 滑块选择
age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

st.divider()

# 按钮
st.button("Reset", type="primary")
if st.button('Say hello'):
    st.write('Why hello there')
    st.balloons()
else:
    st.write('Goodbye')
    st.snow()
    

#st.image 图像
#st.audio 音频
#st.video 视频
