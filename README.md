# DRIVERLESS SUBSYSTEM -  Cone Detection and Navigation 

**Candidate:** Kiran Gunathilaka

## 1. Training a Model & Evaluation

### 1.1. Model Overview (Perception)

A **YOLOv8** model was trained for the cone detection task, which is responsible for detecting **blue cones** and **yellow cones** with class labels and 2D bounding boxes. An additional class, 'big orange', was included from the dataset, though the primary focus remained on blue and yellow cones for track boundary identification.

**Architecture:** Ultralytics YOLOv8

**Input Size:** $1024 \times 1024$ resolution.

**Training Epochs:** 50.

**Hardware:** GPU (Tesla T4) on colab

### 1.2. Dataset

The model was trained on a **publicly available dataset** specifically, the Formula Student Cones dataset but had to clone it and re-export it in a way that the images are not stretched(resized) and distorted. 

The dataset comprises images of cones under various lighting and pose conditions to ensure the model is robust.

### 1.3. Performance Metrics

The model's performance was evaluated using standard object detection metrics, specifically $\text{mAP}_{50}$ and $\text{mAP}_{50-95}$ (mean Average Precision).

| Metric | All Classes | Big Orange | Blue Cone | Yellow Cone |
| :--- | :---: | :---: | :---: | :---: |
| **mAP@0.5** | $0.786$ | $0.821$ | $0.741$ | $0.797$ |
| **mAP@0.5:0.95** | $0.525$ | $0.519$ | $0.495$ | $0.562$ |

**Test Dataset Validation Results:**

The final model was validated on a separate test set, yielding the following performance:

| Metric | All Classes | Big Orange | Blue Cone | Yellow Cone |
| :--- | :---: | :---: | :---: | :---: |
| **mAP@0.5** | $0.783$ | $0.873$ | $0.702$ | $0.774$ |
| **mAP@0.5:0.95** | $0.512$ | $0.543$ | $0.460$ | $0.532$ |
| **Precision** | $0.897$ | $0.839$ | $0.906$ | $0.947$ |
| **Recall** | $0.677$ | $0.829$ | $0.575$ | $0.629$ |

**Runtime/Latency:**

  * **Inference Speed:** $6.5 \text{ms}$ per image (on validation set)

  * **Inference FPS:** $\approx 153$ FPS ($1000 \text{ms} / 6.5 \text{ms}$)

## 1.4.  Testing the model

Open the `./cone_detection_model/notebooks/inference.ipynb` and run it.

Or run the `./cone_detection_model/scripts/predict.py` after changing the input data directory


### 1.5. Training Visualizations

Training progress plots are included in the `./cone_detection_model/training_results/` directory.

### 1.6 Special Notes
The weights of the final model(.pt files) that was trained for the 3 classes is available in the `./cone_detection_model/models` directory.

The notebook that was used for the entire training and testing is available in the notebooks directory

Results from predictions are in the `./cone_detection_model/runs/` directory