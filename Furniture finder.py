from detectron2.utils.logger import setup_logger
from PIL import Image

# import some common libraries
import numpy as np
import cv2
import urllib

# import some common detectron2 utilities
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog


setup_logger()

resp = urllib.request.urlopen('http://farm5.staticflickr.com/4060/4694300446_25328b68c6_z.jpg')
im = np.asarray(bytearray(resp.read()), dtype="uint8")
im = cv2.imdecode(im, cv2.IMREAD_COLOR)


cfg = get_cfg()
# add project-specific config (e.g., TensorMask) here if you're not running a model in detectron2's core library
cfg.merge_from_file(model_zoo.get_config_file("LVIS-InstanceSegmentation/mask_rcnn_X_101_32x8d_FPN_1x.yaml"))
cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5  # set threshold for this model
# Find a model from detectron2's model zoo. You can use the https://dl.fbaipublicfiles... url as well
cfg.MODEL.DEVICE='cpu'
cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("LVIS-InstanceSegmentation/mask_rcnn_X_101_32x8d_FPN_1x.yaml")
predictor = DefaultPredictor(cfg)
outputs = predictor(im)

# We can use `Visualizer` to draw the predictions on the image.
v = Visualizer(im[:, :, ::-1], MetadataCatalog.get(cfg.DATASETS.TRAIN[0]), scale=1.2)
out = v.draw_instance_predictions(outputs["instances"].to("cpu"))
cv2.imwrite('/mnt/c/pycharm-community-2020.1.2/image2.jpg', out.get_image()[:, :, ::-1])




