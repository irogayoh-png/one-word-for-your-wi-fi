#!/usr/bin/env python3
"""One Word for Your Wi-Fi.

Program ini menulis tepat satu kata ke /output/entry.txt.

Kata: gaslighting

Wi-Fi di rumah bilang "Connected", bar sinyal penuh, tapi tak satu pun
halaman yang terbuka -- dan kau yang merasa gila. Itulah gaslighting:
jaringanmu bersikeras semuanya baik-baik saja sementara tidak ada
internet yang benar-benar masuk. Semua orang yang pernah menatap bar
penuh sambil menunggu halaman yang tak kunjung dimuat langsung mengenal
momen itu, tanpa perlu penjelasan.

Kata ini dipilih lewat arena berpasangan dua arah melawan lima kata
shortlist lainnya (peekaboo, houdini, barhopping, situationship,
onebarwonder) dan melawan gold set (snollygoster, knowitall,
hazel-tapir-72, laggy, buffering): gaslighting menang konsisten di
kedua urutan pada setiap duel. Ia on-topik, lucu seketika, benar soal
cara kerja Wi-Fi rumah, segar karena memakai sudut yang tak dipakai
kata klise seperti slow/laggy/buffering, dan ejaannya langsung dipahami.

Sebagai nama jaringan sponsor pun kata ini bekerja sendiri: SSID-nya
adalah leluconnya.

Gate yang dipenuhi program ini:
  - berkas berisi teks UTF-8 sepanjang 1-20 karakter, bukan hanya spasi;
  - tepat satu kata, tanpa spasi dan tanpa baris baru di akhir, supaya
    isi berkas byte-per-byte sama dengan kata itu sendiri;
  - deterministik: tanpa jaringan, tanpa acak, tanpa masukan luar.
"""

import os

WORD = "gaslighting"


def output_path():
    """Lokasi berkas keluaran.

    Di dalam sandbox penilai, /output sudah tersedia. Untuk uji lokal,
    MAKEFUN_OUTPUT_DIR mengarahkan keluaran ke direktori aman (misalnya
    /tmp) supaya tidak pernah menulis /output bersama sesi lain; bila
    variabel itu diset, ia selalu menang atas /output.
    """
    override = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if override:
        return os.path.join(override, "entry.txt")
    if os.path.isdir("/output"):
        return "/output/entry.txt"
    return os.path.join(os.getcwd(), "output", "entry.txt")


def main():
    word = WORD
    # Satu kata saja: huruf kecil a-z, tanpa spasi, tanpa baris baru.
    assert word.islower() and word.isalpha(), "kata harus huruf kecil a-z"
    assert word.strip() == word, "kata harus tanpa spasi di ujung"
    assert len(word.split()) == 1, "harus tepat satu kata"
    data = word.encode("utf-8")
    # Gate: 1 sampai 20 karakter.
    assert 1 <= len(data) <= 20, "panjang kata di luar gate 1-20"

    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "wb") as handle:
        handle.write(data)


if __name__ == "__main__":
    main()
