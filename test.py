import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('DataFrame')

df = pd.DataFrame({
    '1列目' : [1,2,3,4],
    '2列目' : [10,20,30,40]
})

st.dataframe(df.style.highlight_max(axis=0))

# st.table(df.style.highlight_max(axis=0))

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
```

"""

df1 = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']
)

st.dataframe(df1.style.highlight_max(axis=0))

st.line_chart(df1)

df2 = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [34.64,133.90],
    columns=['lat','lon']
)

st.map(df2)

# st.write('Display Image')
#
# if st.checkbox('Show Image'):
#     img = Image.open('data\DSC_0292.JPG')
#     st.image(img,caption='Naonao',use_column_width=True)

option = st.selectbox(
    'あなたが好きな数字を教えてください、',
    list(range(1,11))
)

'あなたの好きな数字は、',option,'です。'


st.write('Interactive Widgets')

left_column,right_column = st.beta_columns(2)

button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.beta_expander('問い合わせ')
expander.write('問い合わせ内容を書く')

#
# text = st.text_input('あなたの趣味を教えてください')
# condition = st.slider('あなたの今の調子は？',0,100,50)
#
# 'あなたの趣味：',text
# 'コンディション：',condition

#
# video_file = open('F:\Adobe\はむた\\2021_05_10\\01_project\P1000131.mp4','rb')
# video_bytes = video_file.read()
# st.video(video_bytes)


st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i + 1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!'