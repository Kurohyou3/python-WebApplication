import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

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

st.write('Display Image')

img = Image.open('data\DSC_0292.JPG')
st.image(img,caption='Naonao',use_column_width=True)



video_file = open('F:\Adobe\はむた\\2021_05_10\\01_project\P1000131.mp4','rb')
video_bytes = video_file.read()
st.video(video_bytes)