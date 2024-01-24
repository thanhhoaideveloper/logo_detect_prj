from ultralytics import YOLO

predict_folder = "assets/target"
test_folder = "assets/test"

model = YOLO("./model/bestV1.pt")
result = model(test_folder, save = True, project=predict_folder, name='')