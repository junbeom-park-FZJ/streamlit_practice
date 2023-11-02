import streamlit as st
from datetime import datetime
import os

st.title('Memo')

memo_list=['New memo']+os.listdir('memo/')
memo_file=st.selectbox('Select memo', memo_list)

content='Please write a memo'

if memo_file!='New memo':
    with open(f'memo/{memo_file}','r',encoding='utf-8') as f:
        content=f.read()
    fn=memo_file
else:
    fn=datetime.now().strftime('%Y_%m_%d__%H_%M_%S')+'.txt' 

txt=st.text_area('Please write a memo', value=content)

left,right=st.columns(2)
with left:
    save_button=st.button('Save',use_container_width=True)
with right:
    download_button=st.download_button('Download', data=txt, file_name=fn, use_container_width=True)

if save_button:
    try:
        #fn=datetime.now().strftime('%Y_%m_%d__%H_%M_%S')+'.txt'
        
        #fn = 'memo.txt'
        with open(f'memo/{fn}', 'w', encoding='utf-8') as f:
            f.write(txt)
        st.success('The memo is saved')
    except:
        st.error('The saving function is failed')


