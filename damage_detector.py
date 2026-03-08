from ultralytics import YOLO

# Load trained YOLO model
model = YOLO("best.pt")

def detect_damage(image):

    results = model(image)

    damages = []

    for r in results:
        for c in r.boxes.cls:
            damage_type = model.names[int(c)]
            damages.append(damage_type)

    return damages
