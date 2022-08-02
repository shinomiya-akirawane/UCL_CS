#ifndef STRUCTS_H
#define STRUCTS_H
struct Pos
{
	int x;
	int y;
};
struct Robot
{
	struct Pos pos;
	/* the position will be reached if robot move one step forward*/
	struct Pos futurePos;
	int dir;
};
#endif