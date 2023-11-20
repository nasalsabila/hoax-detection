import streamlit as st
import re
import numpy as np
import requests
import pandas as pd
import shlex
import subprocess
import json
import os


def jelang_pilpres():
    st.write('# :blue[10 Hoax Terkait Pilpres]')
    st.write('_Pemilu sebentar lagi, cek dulu hoax yang bertebaran di sini!_')


    def call_curl(curl):
        args = shlex.split(curl)
        process = subprocess.Popen(args, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return json.loads(stdout.decode('utf-8'))


    # search_text = st.text_input("Masukkan keyword", "")

    # st.write('The current movie title is', search_text)

    curl = "curl --request POST \
    --url 'https://yudistira.turnbackhoax.id/api/antihoax/search/' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --header 'Accept: application/json' \
    --data 'key=123456&method=content&value=pilpres&limit=20&total=0'"

    output = call_curl(curl)

    # data = response.json()

    df = pd.DataFrame.from_dict(output)

    df = df[df['classification'].isin(['Manipulated Content',
            'Misleading Content',
            'False Context',
            'Impostor Content',
            'False Connection',
            'Fabricated Content',
            'Satire'])].reset_index(drop=True)
    
    df = df.head(10).reset_index(drop=True)

    df['title'] = df['title'].str.replace(r"\[.*\]","")
    # df['title'] = df['title'].str.replace(r"\(.*\)","")
    # df['title'] = df['title'].apply(lambda x: re.sub(r'[^\w\s]','',x))

    for i in range(10):
        st.subheader(str(i+1) + '. ' + df['title'].loc[i], divider='rainbow')
        st.caption('Kategori: ' + df['classification'].loc[i])

        st.markdown(df['conclusion'].loc[i])
jelang_pilpres()