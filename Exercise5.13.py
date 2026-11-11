
# Student Schedule Manager

schedule = [
    '07.30 - 09.10 | Kuliah',
    '09.20 - 11.00 | Praktikum',
    '13.00 - 14.45 | Mengerjakan tugas',
    '16.00 - 18.00 | Latihan organisasi'
]

print("================================")
print("       STUDENT SCHEDULE")
print("================================")

if schedule:
    print("Daftar kegiatan hari ini:\n")

    for activity in schedule:
        print(activity)

    print("\nSemangat menjalani aktivitas!")
else:
    print("Belum ada jadwal kegiatan hari ini.")
