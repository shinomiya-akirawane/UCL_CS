Description of the program:
    The program can display a grid with a robot inside and the robot can 
    find mark by itself. 
    The inital position and inital direction of robot should be 
    include in complier commands.
    The positions of marks and blocks are generated randomly.

complier commands:
    gcc -std=c99 -o robot main.c calculators.c view.c controller.c graphics.c
    ./robot (startX) (startY) (direction(1-4))| java -jar drawapp-2.0.jar
    e.g.
        ./robot 4 5 2| java -jar drawapp-2.0.jar
    1 means east
    2 means south
    3 means west
    4 means north
