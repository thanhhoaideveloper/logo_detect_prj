from ultralytics import YOLO


model = YOLO("./model/bestV5.pt")

predict_path = "assets/target"
test_path = "assets/test"
result = model(test_path, save = True, project=predict_path, conf=0.5)