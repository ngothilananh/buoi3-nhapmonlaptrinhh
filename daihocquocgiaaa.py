# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 16:09:38 2024

@author: Student
"""


chuoi = "Đại học Quốc gia, Khu phố 6, P. Linh Trung, Q. Thủ Đức, Tp. HCM"
sub_strings = chuoi.split(", ")
print("Danh sách 1:")
for part in sub_strings:
    print(part)
sub_strings_2 = [part.replace("P. ", "").replace("Q. ", "").replace("Tp. ", "") for part in sub_strings]
print("\nDanh sách 2:")
for part in sub_strings_2:
    print(part)
