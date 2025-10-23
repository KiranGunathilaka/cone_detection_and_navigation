import os, cv2
from ultralytics import YOLO

best_path = "./models/best.pt"
model = YOLO(best_path)

test_path = "./dataset/Formula-Student-Cones-1/test/images/"

results = model.predict(source=test_path, conf=0.5, save=False)

out_dir = "./runs/results_got_locally/"
os.makedirs(out_dir, exist_ok=True)

for i, r in enumerate(results):
    img = r.plot(labels=True, conf=True, line_width=1, font_size=0.2)
    cv2.imwrite(os.path.join(out_dir, f"{i:04d}.jpg"), img)

print("Custom predictions saved to:", out_dir)