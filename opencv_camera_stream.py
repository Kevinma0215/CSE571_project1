import cv2
from lerobot.cameras.opencv.camera_opencv import OpenCVCamera
from lerobot.cameras.opencv.configuration_opencv import OpenCVCameraConfig
from lerobot.cameras.configs import ColorMode, Cv2Rotation


config = OpenCVCameraConfig(
    index_or_path=2,
    fps=10,
    width=1280,
    height=720,
    color_mode=ColorMode.RGB,
    rotation=Cv2Rotation.NO_ROTATION
)

camera = OpenCVCamera(config)
camera.connect()

while True:
    frame = camera.read()  # numpy array (H, W, C)
    cv2.imshow("LeRobot Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.disconnect()
cv2.destroyAllWindows()
