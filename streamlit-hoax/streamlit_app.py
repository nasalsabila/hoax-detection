# Copyright 2018-2022 Streamlit Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="CekDulu!",
        page_icon="🧐",
    )

    st.write("# CekDulu! 🧐")

    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        CekDulu adalah website yang dapat kamu manfaatkan untuk memprediksi kemungkinan suatu informasi dapat dipercaya kebenarannya atau tidak.
        
        
        _Bijak menyikapi, cek dulu sebelum sebar!_

    """
    )
    st.write("### Dapat informasi? Cek dulu kebenarannya!")
    txt = st.text_area(
    "Tuliskan di sini 👇",
    "",
    )

    # st.write(f'You wrote {len(txt)} characters.')
    # st.button("Cek", type="primary")
    if st.button('Cek', type="primary"):
        if len(txt) > 0:
            st.write(f'You wrote {len(txt)} characters.')
        else:
            st.write('Oooppss! Kamu belum menuliskan informasinya.')


if __name__ == "__main__":
    run()