import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

def run():
    
    # Membuat Title
    st.title('SortirSampahVision')

    # Membuat Sub Header
    st.subheader('Exploratory Data Analysis')

    # Menambahkan Gambar
    image = Image.open('trash.jpg')
    st.image(image, caption='classification trash')

    # Menambahkan text
    st.write('page dibuat oleh ***Suartina Sitanggang***')

    # Menambahkan text
    st.write('# EDA')

    # Menambahkan text
    st.write('### Visualisasi distribusi')

    # Menambahkan Gambar
    image = Image.open('output.png')
    st.image(image, caption='visualisasi class')

    # Menambahkan text
    st.write('### Analisis Distribusi Data Training per Kelas')

    # Menambahkan text
    st.write('1. **Kelas `paper`** memiliki jumlah gambar terbanyak, menunjukkan representasi yang kuat di dalam dataset.')
    st.write('2. **Kelas `glass`, `metal`, dan `plastic`** memiliki jumlah data yang relatif seimbang, sehingga model berpeluang belajar cukup baik dari ketiganya.')
    st.write('3 **Kelas `trash`** memiliki jumlah data yang paling sedikit secara signifikan, jauh di bawah kelas lainnya.')

    # Menambahkan text
    st.write('### Visualisasi Contoh Gambar per Kelas')

    # Menambahkan Gambar
    image = Image.open('output glass.png')
    st.image(image, caption='visualisasi class glass')

    # Menambahkan Gambar
    image = Image.open('output trash.png')
    st.image(image, caption='visualisasi class trash')

    # Menambahkan Gambar
    image = Image.open('output metal.png')
    st.image(image, caption='visualisasi class metal')

    # Menambahkan Gambar
    image = Image.open('output paper.png')
    st.image(image, caption='visualisasi class paper')

    # Menambahkan Gambar
    image = Image.open('output plastic.png')
    st.image(image, caption='visualisasi class plastic')


    # Menambahkan text
    st.write('### Analisis Visualisasi Contoh Gambar per Kelas')

    # Menambahkan text
    st.write('1. **Glass**: Berisi botol dan benda-benda kaca, biasanya bening atau mengilap.')
    st.write('2. **Metal**: Didominasi oleh kaleng minuman dan benda logam kecil, kadang dalam kondisi penyok.')
    st.write('3. **Paper**: Terdiri dari koran, selebaran, karton, dan kertas cetak lainnya.')
    st.write('4. **Plastic**: Berisi botol plastik, tutup botol, dan kemasan plastik lain yang umum ditemukan.')
    st.write('5. **Trash**: Objek yang tidak termasuk kategori daur ulang, seperti tisu bekas, plastik kusut, dan potongan sampah tidak teridentifikasi')

if __name__== '__main__':
    run()