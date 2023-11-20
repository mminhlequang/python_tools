import json

# Đọc tệp JSON từ en.json
with open('en.json', 'r', encoding='utf-8') as input_file:
    data = json.load(input_file)

# Loại bỏ các key trùng lặp
def remove_duplicates(data):
    seen = set()
    result = {}
    for key, value in data.items():
        if key not in seen:
            seen.add(key)
            result[key] = value
    return result

# Gọi hàm loại bỏ key trùng lặp
cleaned_data = remove_duplicates(data)

# Lưu kết quả vào output.json
with open('output.json', 'w', encoding='utf-8') as output_file:
    json.dump(cleaned_data, output_file, indent=4, ensure_ascii=False)

print("Đã loại bỏ key trùng lặp và lưu vào output.json")
