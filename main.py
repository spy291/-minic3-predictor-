import streamlit as st
import pandas as pd
import numpy as np
import sklearn

st.set_page_config(page_title="测试页面", page_icon="✅")
st.title("✅ 部署测试成功")
st.write("如果能看见这行字，说明环境配置正确！")

# 显示版本信息
st.write(f"Streamlit版本: {st.__version__}")
st.write(f"Pandas版本: {pd.__version__}")
st.write(f"NumPy版本: {np.__version__}")
st.write(f"Scikit-learn版本: {sklearn.__version__}")

# 测试导入
from sklearn.ensemble import RandomForestClassifier
st.success("所有包导入成功！")
