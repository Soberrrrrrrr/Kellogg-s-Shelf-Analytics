# KTSA Object Detection API

This project provides an API for object detection using YOLOv7. It enables users to upload images and receive detection results via a RESTful interface.

## Features

- FastAPI-based REST API for image inference
- YOLOv7 model integration for high-accuracy object detection
- Supports image upload and batch processing
- Results saved to `runs/detect/exp` directory

## Project Structure

```
KTSA_API/
├── main.py                # FastAPI server
├── run.py                 # Script to run the API
├── requirements.txt       # Python dependencies
├── yolov7/                # YOLOv7 source code and models
├── inference/images/      # Input images for inference
├── runs/                  # Output results
├── weights/               # Model weights
├── output/                # Additional outputs
├── models/                # Model files
├── app/                   # Application code
└── readme.md              # Project documentation
```

## Installation

1. Clone the repository.
2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```
3. Download YOLOv7 weights and place them in the `weights/` directory.

## Usage

Start the API server:
```sh
python main.py
```

Send an image for prediction using the `/predict` endpoint. Example using `curl`:
```sh
curl -X POST "http://localhost:8000/predict" -F "file=@inference/images/example.jpg"
```

## Model Training & Inference

- Training and evaluation scripts are available in `yolov7/`.
- For custom training, see the YOLOv7 documentation and scripts.

## License

This project uses YOLOv7, which is licensed under the GNU General Public License v3.0. See `yolov7/LICENSE.md` for