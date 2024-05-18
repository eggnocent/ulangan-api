import json

def tambah_likes(data, judul_lagu, jumlah_likes):
    for lagu in data["lagu"]:
        if lagu["judul"] == judul_lagu:
            lagu["likes"] += jumlah_likes
            lagu["played"] += 1
            print(f"Likes untuk lagu {judul_lagu} berhasil ditambahkan. Total likes sekarang: {lagu['likes']}")
            return True
    print(f"Lagu dengan judul {judul_lagu} tidak ditemukan.")
    return False

def hitung_popularitas(likes, played):
    return likes / played * 100 

def main():
    with open("lagu.json", "r+") as file:
        data_lagu = json.load(file)

        print("Daftar Lagu:")
        for lagu in data_lagu["lagu"]:
            popularitas = hitung_popularitas(lagu["likes"], lagu["played"])
            print(f"{lagu['judul']} - {lagu['artist']} (Likes: {lagu['likes']}, Played: {lagu['played']}, Popularitas: {popularitas:.2f}%)")

        judul_lagu = input("Masukkan lagu yang ingin ditambahkan likenya: ")
        jumlah_likes = 1

        if tambah_likes(data_lagu, judul_lagu, jumlah_likes):
            file.seek(0)
            json.dump(data_lagu, file, indent=2)
if __name__ == "__main__":
    main()
