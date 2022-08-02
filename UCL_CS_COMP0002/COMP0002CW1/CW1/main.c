#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "structs.h"
#include "function.h"

struct Robot robot = {5, 6, 6, 6, 1};


int main(int argc, char **argv)
{
	struct Pos *blocksPos = randomBlocksPos();
	struct Pos markPos = randomMarkPos();
	if (argc == 4)
	{
		robot.pos.x = atoi(argv[1]);
		robot.pos.y = atoi(argv[2]);
		robot.dir = atoi(argv[3]);
	}
	drawGrip(blocksPos, markPos);
	drawRobot();
	findMark(blocksPos, markPos);
	return 0;
}
