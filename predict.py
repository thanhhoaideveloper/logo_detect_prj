from ultralytics import YOLO


model = YOLO("./model/bestV2.pt")

predict_path = "assets/target"
test_path = "assets/test"
results = model(test_path, save = True, project=predict_path, conf=0.5, show_conf=True, save_conf=True)
