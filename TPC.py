import streamlit as st
import random
import time

# Judul aplikasi
st.title("Game Perhitungan Total Plate Count (TPC)")

# Deskripsi game
st.write("""
Selamat datang di game perhitungan Total Plate Count (TPC)!
Hitung koloni bakteri yang muncul di layar dan masukkan jumlah koloni yang Anda hitung.
""")

# Input volume sampel
volume_sampel = st.number_input("Masukkan Volume Sampel (mL):", min_value=1.0, step=0.1)

# Fungsi untuk memulai permainan
def start_game():
    st.session_state.count = 0
    st.session_state.target = random.randint(25, 250)
    st.session_state.start_time = time.time()
    st.session_state.game_active = True

# Fungsi untuk menghentikan permainan
def stop_game():
    st.session_state.game_active = False

# Tombol untuk memulai permainan
if st.button("Mulai Permainan"):
    start_game()

# Menampilkan koloni bakteri
if 'game_active' in st.session_state and st.session_state.game_active:
    st.write(f"Hitung koloni bakteri! Target: {st.session_state.target} koloni")
    
    # Menampilkan koloni bakteri
    for _ in range(st.session_state.target):
        st.image("bacteria_icon.png", width=50)  # Ganti dengan ikon bakteri yang sesuai
        time.sleep(0.1)  # Delay untuk animasi

    # Input jumlah koloni yang dihitung
    st.session_state.count = st.number_input("Masukkan jumlah koloni yang Anda hitung:", min_value=0, step=1)

    # Tombol untuk menghitung TPC
    if st.button("Hitung TPC"):
        if volume_sampel > 0:
            tpc = st.session_state.count / volume_sampel
            st.success(f"Total Plate Count (TPC): {tpc:.2f} CFU/mL")
        else:
            st.error("Volume sampel harus lebih besar dari 0.")

    # Tombol untuk menghentikan permainan
    if st.button("Selesai"):
        stop_game()
        st.write("Permainan selesai! Terima kasih telah bermain.")
else:
    st.write("Tekan tombol 'Mulai Permainan' untuk memulai.")
