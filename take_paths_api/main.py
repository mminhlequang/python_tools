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

string1 = "{"
string2 = "}"

# Tạo đoạn mã cho output.json
output_code1 = ''
output_code2 = ''
output_code3 = ''
output_code4 = ''
for path in paths:
    output_code1 += f'static const String {convert_to_variable_name(path)} = "{path}";\n'
    output_code2 += f'Future<NetworkResponse> {convert_to_variable_name(path)}(params);\n'
    
    method = list(data['paths'][path].keys())[0]
    output_code3 += f"@override \nFuture<NetworkResponse> {convert_to_variable_name(path)}(params) async {string1} \n return await handleNetworkError( \n proccess: () async  {string1} \nResponse response = await AppClient( \nrequiredToken: false, \n ).{method}(ApiRoutess.{convert_to_variable_name(path)} , queryParameters: params);\nreturn NetworkResponse.fromResponse(response,\n converter: (json) =>\n (json as List).map((e) => UserModel.fromJson(e)).toList());  {string2} ,); {string2} \n\n"

    output_code4 += f"Future<bool> {convert_to_variable_name(path)}([params]) async {string1} NetworkResponse response = await _api.{convert_to_variable_name(path)}(params); return response.data ?? false; {string2} \n\n"

# Ghi vào file output.json
with open('output1.json', 'w') as outfile:
    outfile.write(output_code1)
with open('output2.json', 'w') as outfile:
    outfile.write(output_code2)
with open('output3.json', 'w') as outfile:
    outfile.write(output_code3)
with open('output4.json', 'w') as outfile:
    outfile.write(output_code4)

print('Xuất ra output json thành công.')
