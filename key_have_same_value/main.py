import json

# Đọc dữ liệu từ file input1.json và input2.json
with open('input1.json', 'r', encoding='utf-8') as file1, open('input2.json', 'r', encoding='utf-8') as file2:
    data1 = json.load(file1)
    data2 = json.load(file2)

# Tìm các cặp key có cùng giá trị trong cả hai file
common_key_value_pairs = []

for key1, value1 in data1.items():
    for key2, value2 in data2.items():
        if value1 == value2 and key1 != key2:
            common_key_value_pairs.append((key2, key1, value1))


# # Ghi các khóa giống nhau vào tệp output2.txt
# with open('output2.txt', 'w', encoding='utf-8') as output_file:
#     for key1, key2, value1 in common_key_value_pairs:
#         output_file.write(f"{key1} = {key2} : {value1}\n")

# Tạo một dictionary để lưu trữ kết quả theo định dạng bạn mong muốn
output_data = {}
count = 1

for key1, key2, value1 in common_key_value_pairs:
    output_data[count] = [key1, key2, value1]
    count += 1

# Ghi dictionary kết quả vào file output.json
with open('output.json', 'w') as output_file:
    json.dump(output_data, output_file, indent=2)

