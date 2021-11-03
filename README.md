
<!-- PROJECT LOGO -->
<br />
<div align="center">
    <h3 align="center">Sorting Algorithms Visualizer</h3>

  <p align="center">
    A Pygame app that shows in a graphical way 3 popular sorting algorithms 
  </p>
</div>

<!-- ABOUT THE PROJECT -->
## About The Project

This app is built using the Pygame module. Even though it is usually used for small, 2d game development, it proves to be very easy to use for small scale GUI apps like this one. The user runs the app with the 2 necessary parameters: algorithm and color theme (i made it so that you can change the main color on each run of the script). The code has a Object Oriented approach and uses the argparse library for a more user-friendly command line experience.

## Demo
For more information take a look at the Demo video down below



https://user-images.githubusercontent.com/46849514/140015646-b38433d7-fc98-47c2-b628-3eb36437a99c.mp4



### Built With

This project is entirely developed in Python. The only library used was Pygame

* [Python]
* [Pygame]


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

Everything we need is in the Python Package Index (PyPi).
1. Install virtualenv
  ```sh
  pip install virtualenv
  ```
  
2. Create virtual environment
  ```sh
  virtualenv sorting_visualizer_venv
  
  ```
3. Activate virtualenv & Install dependencies
  ```sh
  source sorting_visualizer_venv/bin/activate
  pip install -r requirements.txt
  ```


<!-- USAGE EXAMPLES -->
## Usage

After installing all the dependencies all we need to do is run the command as follows
  Long Version
  ```sh
  python3 visualizer.py --algorithm bubble_sort -color blue 
  ```
  Short Version
  ```sh
  python3 visualizer.py --a bubble_sort -c blue 
  ```

For any clarifications regarding the script type:
  ```sh
  python3 visualizer.py --help
  ```
