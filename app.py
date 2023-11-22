import streamlit as st
from sqlalchemy import text

list_maskapai = ['', 'Garuda Indonesia', 'Air Asia', 'Citilink', 'Emirates', 'Singapore Airlines']
list_tujuan = ['', 'Surabaya', 'Jakarta', 'Bali', 'Lombok', 'Bandung']

conn = st.connection("postgresql", type="sql", 
                     url="postgresql://pahlawanazzam:mFDM3obsLz2n@ep-rapid-violet-27339173.us-east-2.aws.neon.tech/Web")
with conn.session as session:
    query = text('CREATE TABLE IF NOT EXISTS RESERVATION (id serial, maskapai varchar, tujuan varchar, penumpang varchar, nomor_pesawat varchar, \
                                                       alamat varchar, nomor_handphone varchar, tanggal_berangkat date);')
    session.execute(query)

st.header('Sistem Pemesanan Tiket Pesawat')
page = st.sidebar.selectbox("Pilih Menu", ["Lihat Pesanan", "Buat Pesanan", "Ubah Pesanan"])

if page == "Lihat Pesanan":
    data = conn.query('SELECT * FROM reservation ORDER By id;', ttl="0").set_index('id')
    st.dataframe(data)

if page == "Buat Pesanan":
    if st.button('Pesan Tiket'):
        with conn.session as session:
            query = text('INSERT INTO reservation (maskapai, tujuan, penumpang, nomor_pesawat, alamat, nomor_handphone, tanggal_berangkat) \
                          VALUES (:1, :2, :3, :4, :5, :6, :7);')
            session.execute(query, {'1':'', '2':'', '3':'', '4':'', '5':'', '6':'', '7':None})
            session.commit()

    data = conn.query('SELECT * FROM reservation ORDER By id;', ttl="0")
    for _, result in data.iterrows():        
        id = result['id']
        maskapai_lama = result["maskapai"]
        tujuan_lama = result["tujuan"]
        penumpang_lama = result["penumpang"]
        nomor_pesawat_lama = result["nomor_pesawat"]
        alamat_lama = result["alamat"]
        nomor_handphone_lama = result["nomor_handphone"]
        tanggal_berangkat_lama = result["tanggal_berangkat"]

        with st.expander(f'Pesanan {penumpang_lama}'):
            with st.form(f'data-{id}'):
                maskapai_baru = st.selectbox("Maskapai", list_maskapai, list_maskapai.index(maskapai_lama))
                tujuan_baru = st.selectbox("Tujuan", list_tujuan, list_tujuan.index(tujuan_lama))
                penumpang_baru = st.text_input("Penumpang", penumpang_lama)
                nomor_pesawat_baru = st.text_input("Nomor Pesawat", nomor_pesawat_lama)
                alamat_baru = st.text_input("Alamat", alamat_lama)
                nomor_handphone_baru = st.text_input("Nomor Handphone", nomor_handphone_lama)
                tanggal_berangkat_baru = st.date_input("Tanggal Berangkat", tanggal_berangkat_lama)
                
                col1, col2 = st.columns([1, 6])

                with col1:
                    if st.form_submit_button('Konfirmasi Pesanan'):
                        with conn
