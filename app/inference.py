import sys
import os
from pathlib import Path

# Ensure yolov7 folder is in the Python path
FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]  # KTSA_API
YOLOV7_DIR = ROOT / "yolov7"
sys.path.append(str(YOLOV7_DIR))

from yolov7.detect_count import run  # import your custom detect logic


def run_inference(
    weights_path="yolov7/KTSA_20062025_best.pt",
    source_path="inference/images",
    img_size=640,
    conf_thres=0.25,
    iou_thres=0.45,
    device="cpu",
    save_txt=False,
    save_conf=False,
    nosave=False,
    classes=None,
    agnostic_nms=False,
    augment=False,
    project="runs/detect",
    name="exp",
    exist_ok=True,
):
    result = run(
        weights=weights_path,
        source=source_path,
        img_size=img_size,
        conf_thres=conf_thres,
        iou_thres=iou_thres,
        device=device,
        view_img=False,
        save_txt=save_txt,
        save_conf=save_conf,
        nosave=nosave,
        classes=classes,
        agnostic_nms=agnostic_nms,
        augment=augment,
        update=False,
        project=project,
        name=name,
        exist_ok=exist_ok,
    )
    return result  # this is optional — depends on what your detect_count.py returns
