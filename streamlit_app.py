import streamlit as st
import pandas as pd

# Judul aplikasi
st.title("Visualisasi Kolom Dataset dengan Checkbox dan Jenis Grafik")

# Memungkinkan pengguna untuk mengunggah dataset
uploaded_file = st.file_uploader("Unggah dataset CSV Anda", type=["csv"])

# Jika file diunggah, baca dan tampilkan datanya
if uploaded_file is not None:
    # Membaca dataset yang diunggah
    data = pd.read_csv(uploaded_file)

    # Menampilkan dataset
    st.write("Dataset yang diunggah:")
    st.dataframe(data)

    # Pilih kolom yang ingin divisualisasikan melalui combo box
    selected_columns = st.multiselect("Pilih kolom untuk ditampilkan", data.columns.tolist())

    # Pilih jenis grafik
    chart_type = st.selectbox("Pilih jenis grafik", ["Line Chart", "Bar Chart", "Area Chart"])

    # Menampilkan grafik sesuai dengan kolom yang dipilih
    if selected_columns:
        for column in selected_columns:
            # Tambahkan checkbox untuk mengontrol apakah grafik kolom tertentu ditampilkan atau tidak
            show_chart = st.checkbox(f"Tampilkan grafik untuk kolom: {column}", value=True)

            if show_chart:
                st.subheader(f"Grafik untuk kolom: {column}")

                # Menampilkan grafik berdasarkan pilihan jenis grafik
                if chart_type == "Line Chart":
                    st.line_chart(data[[column]])
                elif chart_type == "Bar Chart":
                    st.bar_chart(data[[column]])
                elif chart_type == "Area Chart":
                    st.area_chart(data[[column]])

                # Garis pemisah antar grafik
                st.write("---")
    else:
        st.write("Silakan pilih setidaknya satu kolom untuk divisualisasikan.")
else:
    st.write("Silakan unggah file CSV untuk memulai.")
