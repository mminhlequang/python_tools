import re
import json

# Hàm để tìm và trích xuất các chuỗi từ file input.txt
def extract_localization_keys(input_file):
    localization_keys = {}
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            match = re.search(r'Localization key \[(.*?)\] not found', line)
            
            if match:
                key_content = match.group(1)
                # Split và xử lý nội dung cần lấy ra thành các cặp key-value
                items = key_content.split(',')
                localization_keys.update({key_content: key_content})

    # Remove duplicate keys
    unique_data = {value: value for key, value in localization_keys.items()}
    return unique_data

# Hàm để lưu các chuỗi vào file output.json
def save_to_json(output_file, localization_keys):
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(localization_keys, file, ensure_ascii=False, indent=4)

# File đầu vào và đầu ra
input_file = 'input.txt'
output_file = 'output.json'

# Trích xuất và lưu các chuỗi vào file output.json
localization_keys = extract_localization_keys(input_file)
save_to_json(output_file, localization_keys)

print("Các chuỗi đã được trích xuất và lưu vào file output.json.")
