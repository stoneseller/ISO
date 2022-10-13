import streamlit as st
from PIL import Image

st.set_option('deprecation.showfileUploaderEncoding', False) # deprecation 표시 안함
st.write("made by. 임기택")
st.title("머신러닝 이용 표준화 분류 시스템")
st.markdown("""
머신러닝을 통해 포쥰화 된 것을 분류하고,
표준화된 것은 어떤 표준을 따르고 있는지 알려줍니다.""")

image2 = Image.open('standard.gif')
st.image(image2, caption='ISO 로고',use_column_width=True)


st.text("***이미지 분류를 위해 이미지를 업로드 해 주세요***")
#Streamlit 파일 처리 및 결과
#https://stackoverflow.com/questions/50906123/nameerror-name-image-is-not-defined/50906222
from PIL import Image, ImageOps

from img_classification import ISO
uploaded_file = st.file_uploader("아래에 업로드 해주세요.", type=['jpeg', 'png', 'jpg', 'webp'])
if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded ISO.', use_column_width=True)
        st.write("")
        st.write("처리중입니다...")
        label = ISO(image, 'keras_model.h5')
        if label==0:
            st.write("***결과 : 220V 콘센트 입니다.***")
            st.write(label)
        elif label==1:
            st.write("***결과 : 110V 콘센트 입니다.***")
            st.write(label)
        else:
            st.write("***표준화 되지 않은 물건입니다***")
            st.write(label)



