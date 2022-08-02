#include "function.h"
#include "structs.h"
#include "gridParameter.h"
#include <time.h>
#include <stdlib.h>
#include <stdio.h>
#include "graphics.h"
extern struct Robot robot;
struct Pos *randomBlocksPos()
{
	struct Pos *BlocksPos = (struct Pos *)malloc(8 * sizeof(struct Pos));
	srand(time(0) * 10);
	for (int i = 0; i < 8; i++)
	{
		BlocksPos[i].x = randomNum(3, 13);
		BlocksPos[i].y = randomNum(1, 14);
	}
	return BlocksPos;
}
struct Pos randomMarkPos()
{
	struct Pos pos;
	srand(time(0) * 10);
	pos.x = randomNum(3, 13);
	pos.y = randomNum(3, 14);
	return pos;
}
void updateFuturePos()
{
	switch (robot.dir)
	{
	case 1:
		robot.futurePos.x = robot.pos.x + 1;
		robot.futurePos.y = robot.pos.y;
		break;
	case 2:
		robot.futurePos.x = robot.pos.x;
		robot.futurePos.y = robot.pos.y + 1;
		break;
	case 3:
		robot.futurePos.x = robot.pos.x - 1;
		robot.futurePos.y = robot.pos.y;
		break;
	case 4:
		robot.futurePos.x = robot.pos.x;
		robot.futurePos.y = robot.pos.y - 1;
		break;
	default:
		drawString("something wrong with robot direction", 125, 125);
	}
}


int canMoveForward(struct Pos *blocksPos)
{
	if (robot.futurePos.x >= 13 || robot.futurePos.x < 1 || robot.futurePos.y >= 14 || robot.futurePos.y < 1)
		return 0;
	else
	{
		for (int i = 0; i < 8; i++)
			if (robot.futurePos.x == blocksPos[i].x && robot.futurePos.y == blocksPos[i].y)
				return 0;
		return 1;
	}
}
int atMarker(struct Pos markPos)
{
	if (robot.pos.x == markPos.x && robot.pos.y == markPos.y)
		return 1;
	else
		return 0;
}
void forward(struct Pos *blocksPos, struct Pos markPos)
{
	foreground();
	clear();
	if (canMoveForward(blocksPos) == 1)
	{
		switch (robot.dir)
		{
		case 1:
			robot.pos.x += 1;
			break;
		case 2:
			robot.pos.y += 1;
			break;
		case 3:
			robot.pos.x -= 1;
			break;
		case 4:
			robot.pos.y -= 1;
			break;
		default:
			drawString("something wrong with robot direction", 125, 125);
		}
		updateFuturePos();
		drawRobot();
	}
	sleep(100);
}
void left()
{
	foreground();
	clear();

	robot.dir = robot.dir - 1;
	if (robot.dir == 0)
		robot.dir = -1;
	robot.dir = robot.dir % 5;
	if (robot.dir < 0)
		robot.dir += 5;
	updateFuturePos();
	drawRobot();
	sleep(100);
}
void right()
{
	foreground();
	clear();

	robot.dir = (robot.dir + 1) % 5;
	updateFuturePos();
	drawRobot();
	sleep(100);
}

void findMark(struct Pos *blocksPos, struct Pos markPos)
{
	while (atMarker(markPos) == 0)
	{
		double distance = calDis(robot.pos, markPos);
		for (int i = 0; i < 3; i++)
		{
			double Newdistance = calDis(robot.futurePos, markPos);
			if (Newdistance >= distance)
				left();
			else
				break;
		}
		if (canMoveForward(blocksPos) == 1)
			forward(blocksPos, markPos);
		else
		{
			for (int i = 0; i < 3; i++)
			{
				if (canMoveForward(blocksPos) == 1)
					forward(blocksPos, markPos);
				else
					right();
			}
		}
	}
	if (atMarker(markPos) == 1)
	{
		setColour(red);
		drawString("Find Mark!", 200, 200);
		return;
	}
}