<h1 align="center"> pykinect-recorder </h1>

<div align="center">
  <a href="https://pypi.python.org/pypi/pykinect-recorder"><img src="https://img.shields.io/pypi/v/pykinect-recorder.svg"></a>
  <a href="https://pypi.org/project/pykinect-recorder"><img src="https://img.shields.io/pypi/pyversions/pykinect-recorder.svg"></a>
</div>

<br>
<div>
The pykinect-recorder is an educational/industrial library that provides sensor recording (including audio), playback, and computer vision soultions through a python wrapper of the Azure Kinect Sensor SDK.
</div>

<br>

<div display="flex;">
<img src="https://github.com/unerue/pykinect-recorder/assets/78347296/d875ad2c-03e3-4762-a0a1-80df63ea49fc">
</div>

<br>

##  Features<hr>

- [x] See RGB, IR, Depth, IMU and Audio data when recoding.
- [x] Control Recording option (FPS, brightness, ...).
- [x] Change layout with drag and drop.
- [x] Playback Recorded video.
- [ ] Recording Audio.
- [ ] 3D Viewer with streaming/recording.
- [ ] Deep Learning Inference with streaming/recorded video.
- [ ] Sync multi camera.

<br>

## Prerequisites<hr>

### Azure kinect SDK 

- Make sure you download Azure Kinect SDK before using this repo. 
- SDK version '1.4.1' supported in release 1.0.0.
- You can download Azure Kinect SDK [here](https://github.com/microsoft/Azure-Kinect-Sensor-SDK/blob/develop/docs/usage.md).
    
### Anaconda
- Make sure you download Anaconda before using this repo.
- You can download Miniconda [here](https://docs.conda.io/en/latest/miniconda.html).

<br>

## Installation<hr>
 
There are two options:
- Run with cli (anaconda).
- Run with poetry.

### Anaconda (Recommended)
```bash
conda create -n azure python=3.8 -y
conda activate azure
pip install pykinect-recorder

pykinect
```

### Poetry
```bash
Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py

$Env:Path += ";C:\Users\{user_name}\AppData\Roaming\Python\Scripts"; setx PATH "$Env:Path"

# In root directory
poetry install
poetry run python main.py
```

- To use poetry, git clone our repository first. you can install poetry with above command.
- If error occured, See Poetry [official document](https://python-poetry.org/docs/).

<br>

## Features<hr>

ML Solutions: native, mediapipe, torchvision