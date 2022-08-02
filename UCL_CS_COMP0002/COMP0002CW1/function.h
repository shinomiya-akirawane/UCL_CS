#ifndef FUNCTION_H
#define FUNCTION_H
double mySqrt(int x);
struct Pos pos2PixelPos(struct Pos pos);
int randomNum(int min, int max);
double calDis(struct Pos a, struct Pos b);
void drawGrip(struct Pos *blocksPos, struct Pos markPos);
void drawRobot();
struct Pos *randomBlocksPos();
struct Pos randomMarkPos();
void updateFuturePos();
int canMoveForward(struct Pos *blocksPos);
int atMarker(struct Pos markPos);
void forward(struct Pos *blocksPos, struct Pos markPos);
void left();
void right();
void findMark(struct Pos *blocksPos, struct Pos markPos);
#endif