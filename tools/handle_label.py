import os
import re

def get_all_txt_files(directory_path):
    txt_files = []

    # Lặp qua tất cả các thư mục và file trong thư mục chính
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            # Kiểm tra nếu đuôi của file là '.txt'
            if file.endswith('.txt'):
                # Nếu là file '.txt', thêm vào danh sách
                txt_files.append(os.path.join(root, file))

    return txt_files

# Thay thế '/path/to/your/directory/' bằng đường dẫn thực tế của bạn
directory_path = '../data/NikeAuth'
txt_files = get_all_txt_files(directory_path)

# In danh sách các file '.txt'
print("List of txt files:")
for file_path in txt_files:
    # Đọc dữ liệu từ file
    new_value = 10
    with open(file_path, 'r') as file:
        content  = file.read()
    # Cập nhật giá trị trong cột đầu tiên của mỗi dòng
    updated_content = re.sub(r'(^|\s)(\d+)(\s|$)', fr'\g<1>{new_value}\g<3>', content)
    # Ghi lại dữ liệu đã cập nhật vào file
    with open(file_path, 'w') as file:
        file.write(updated_content)