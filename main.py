"""
Aplikasi Deteksi Gempa terkini
MODULARISASI DENGAN FUNCTION
"""


def ekstraksi_data():
    """
    Tanggal: 09 Maret 2022,
    Waktu:08:49:18 WIB
    Magnitudo: 5.2
    Lokasi: LS=2.57  BT=128.43 BT
    Kedalaman: 14 km
    Pusat Gempa: Pusat gempa berada di Laut 60 km TimurLaut Daruba Dirasakan (Skala MMI): II-III Morotai
    :return:
    """

    hasil = dict()
    hasil['tanggal'] = '09 Maret 2022'
    hasil['waktu'] = '08:49:18 WIB'
    hasil['magnitudo'] = 5.2
    hasil['lokasi'] = {'LS': 1.48, 'BT': 13}
    hasil['pusat'] = 'Pusat gempa berada di Laut 60 km TimurLaut Daruba'
    hasil['dirasakan'] = 'Pusat gempa berada di Laut 60 km TimurLaut Daruba Dirasakan (Skala MMI): II-III Morotai'

    return hasil


def tampilkan_data(result):
    print('Gempa Terakhir berdasarkan BMKG')
    print(f"'Tanggal' {result['tanggal']}")
    print(f"'Waktu' {result['waktu']}")
    print(f"'Magnitudo' {result['magnitudo']}")
    print(f"'Lokasi': LS={result['lokasi']['LS']}, BT={result['lokasi']['BT']}")
    print(f"'Pusat' {result['pusat']}")
    print(f"'Dirasakan' {result['dirasakan']}")


if __name__ == '__main__':
    print('Aplikasi Utama')
    result = ekstraksi_data()
    tampilkan_data(result)
