Description
This project displays and animates the movements of a Rubik's Cube in 3D.
The movements are read from a text file (file.txt), and an animation is generated using matplotlib. 
The program also compiles a C file to generate these movements.


Prerequisites
To use this code, you must have the C code written by John.
This C code handles the movements of a 2x2x2 Rubik's Cube and generates the movement instructions. 
It is crucial that you have this C file, as the program relies on it to function correctly.
If you already have John's C file, rename it to mouvement.c and place it in the same directory as the Python script.
If you do not have this file, the program will not work.

In addition, you will need Python 3.x with the following libraries:Python 3.x with the following libraries:
  matplotlib
  ast
  subprocess
  
To install these libraries, use the following command : pip install matplotlib  # Example

Usage
Run the Python script: python3 cube_animation.py

The cube animation will be displayed, and to save each step, uncomment the code in the update_cube() function at line 50.
