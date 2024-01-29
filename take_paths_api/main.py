import json
import re

def convert_to_variable_name(api_path):
    # Loại bỏ ký tự đặc biệt và thay thế "/" bằng "_"
    cleaned_path = re.sub(r'[^a-zA-Z0-9]', '_', api_path)
    
    # Chuyển đổi sang chữ thường và loại bỏ dấu "_" ở đầu và cuối
    variable_name = cleaned_path.lower().strip('_')
    
    # Chuyển đổi sang dạng camelCase
    words = variable_name.split('_')
    camel_case_name = words[0] + ''.join(word.title() for word in words[1:])
    
    return camel_case_name


# Đọc từ file input.json
with open('input.json', 'r') as infile:
    data = json.load(infile)

# Lấy danh sách các key trong paths
paths = list(data['paths'].keys())

# Tạo đoạn mã cho output.json
output_code = ''
for path in paths:
    output_code += f'static const String {convert_to_variable_name(path)} = "{path}";\n'

# Ghi vào file output.json
with open('output.json', 'w') as outfile:
    outfile.write(output_code)

print('Xuất ra output.json thành công.')
