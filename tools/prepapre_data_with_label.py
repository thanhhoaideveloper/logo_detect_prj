import os
import shutil

# Đường dẫn đến thư mục chứa các file label
path_datasets = '../data/DatasetV1/DatasetV1'
path_target = '../data/DataFilter'

def find_txt_with_label(path):
    # Duyệt qua tất cả các tệp trong đường dẫn đã cho
    for root, dirs, files in os.walk(path):
        for file_name in files:
            # Kiểm tra nếu là tệp txt
            if file_name.endswith(".txt"):
                path_file = os.path.join(root, file_name)
                with open(path_file, 'r') as file:
                    for line in file:
                        # Tách các giá trị trên mỗi dòng bằng khoảng trắng và chuyển sang kiểu float
                        values = [float(x) for x in line.split()]

                        # Kiểm tra cột đầu tiên của dòng hiện tại
                        if values[0] == 6:
                            shutil.copy(path_file, path_target)
                            file_name_not_extension = os.path.splitext(file_name)[0]
                            image_format = ['.jpg', '.jpeg', '.png']
                            for ext in image_format:
                                path_image = os.path.join(root, file_name_not_extension + ext)
                                path_image = path_image.replace('labels', 'images')
                                if os.path.exists(path_image):
                                    shutil.copy(path_image, path_target)

# Tạo thư mục đích nếu nó chưa tồn tại
os.makedirs(path_target, exist_ok=True)     
   
find_txt_with_label(path_datasets)