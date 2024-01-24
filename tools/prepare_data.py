import os
import random
import shutil

def split_dataset(input_folder, output_folder, train_ratio=0.7, test_ratio=0.1, valid_ratio=0.2):
    assert train_ratio + test_ratio + valid_ratio == 1.0, "Tổng tỉ lệ phải là 1"

    # Tạo thư mục output nếu chưa tồn tại
    train_folder = os.path.join(output_folder, 'train')
    test_folder = os.path.join(output_folder, 'test')
    valid_folder = os.path.join(output_folder, 'valid')

    for folder in [train_folder, test_folder, valid_folder]:
        os.makedirs(os.path.join(folder, 'labels'), exist_ok=True)
        os.makedirs(os.path.join(folder, 'images'), exist_ok=True)

    # Lấy danh sách tất cả các tệp trong thư mục input
    all_files = [f.split('.')[0] for f in os.listdir(input_folder) if f.endswith('.jpg')]

    # Tính toán số lượng tệp trong mỗi tập
    num_files = len(all_files)
    num_train = int(train_ratio * num_files)
    num_test = int(test_ratio * num_files)
    num_valid = int(valid_ratio * num_files)

    # Chọn ngẫu nhiên các tệp cho mỗi tập
    train_files = random.sample(all_files, num_train)
    remaining_files = set(all_files) - set(train_files)
    test_files = random.sample(list(remaining_files), num_test)
    valid_files = list(remaining_files - set(test_files))

    # Di chuyển tệp vào các thư mục tương ứng
    move_files(input_folder, train_folder, 'labels', 'images', train_files)
    move_files(input_folder, test_folder, 'labels', 'images', test_files)
    move_files(input_folder, valid_folder, 'labels', 'images', valid_files)

def move_files(input_folder, output_folder, labels_subfolder, images_subfolder, file_list):
    for file_name in file_list:
        image_source_path = os.path.join(input_folder, f'{file_name}.jpg')
        label_source_path = os.path.join(input_folder, f'{file_name}.txt')

        image_destination_path = os.path.join(output_folder, images_subfolder, f'{file_name}.jpg')
        label_destination_path = os.path.join(output_folder, labels_subfolder, f'{file_name}.txt')

        shutil.move(image_source_path, image_destination_path)
        shutil.move(label_source_path, label_destination_path)

# Thực hiện chia tập dữ liệu
split_dataset('../data/DataNam/', '../data/')