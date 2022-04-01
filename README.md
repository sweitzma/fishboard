# fishboard

Simple http server for visualizing videos and images.

fishboard launches a http server which recursively searches directories and shows all videos and images grouped by directory.
It supports videos and images with extensions `mp4`, `png`, `jpg`, `jpeg`, and `gif`.

![Screenshot: fishboard](screenshot.png)

> This repo is initiated to check training and testing results for Reinforcement Learning research. <br>
> Using Python's SimpleHTTPServer requires me to navigate forward and backward. 
> It is especially annoying when multiple experiments are running. <br>
> fishboard makes visualizing videos from multiple directories much easier.


## Usage

1. Run fishboard:
```
$ fishboard
```

Options:

* `--logdir`           : Directory where fishboard will look for videos and images recursively
* `--port`             : Port number
* `--height`           : Maximum height of image/video
* `--width`            : Maximum width of image/video
* `--file_name_length` : Maximum length of file name shown in fishboard
* `--recursive`        : Search files recursively
* `--display`          : Display videos and images

2. Check the website at `http://127.0.0.1:8000` or `http://[server]:[port]`.
Whenever click a directory, videos and images inside will be reloaded.


## Installation
*Only work on Python3*

Install from pip:
```
pip install fishboard
# or pip3 install fishboard
```

Install from the latest code:
```
git clone https://github.com/sweitzma/fishboard.git
cd fishboard
pip install -e .
```

## License

[MIT License](LICENSE)

