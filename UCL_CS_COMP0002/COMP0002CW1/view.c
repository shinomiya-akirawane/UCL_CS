#include "structs.h"
#include "gridParameter.h"
#include "function.h"
#include "graphics.h"
extern struct Robot robot;
void drawGrip(struct Pos *blocksPos, struct Pos markPos)
{
	setWindowSize(350, 400);
	background();
	setColour(black);
	drawRect(GRID_LEFT_CONRNER, GRID_LEFT_CONRNER, GRID_WIDTH, GRID_LEN);
	for (int i = GRID_LEFT_CONRNER + SQUARE_LEN; i <= GRID_WIDTH + GRID_LEFT_CONRNER; i += SQUARE_LEN)
		drawLine(i, SQUARE_LEN, i, GRID_LEN + GRID_LEFT_CONRNER);
	for (int i = GRID_LEFT_CONRNER + SQUARE_LEN; i <= GRID_LEN + GRID_LEFT_CONRNER; i += SQUARE_LEN)
		drawLine(SQUARE_LEN, i, GRID_WIDTH + GRID_LEFT_CONRNER, i);
	setColour(red);
	for (int i = 0; i < 8; i++)
		fillRect((blocksPos[i].x * SQUARE_LEN), (blocksPos[i].y * SQUARE_LEN), SQUARE_LEN, SQUARE_LEN);
	setColour(gray);
	fillRect(pos2PixelPos(markPos).x, pos2PixelPos(markPos).y, SQUARE_LEN, SQUARE_LEN);
}
void drawRobot()
{
	int robotVertexesX[3];
	int robotVertexesY[3];
	foreground();
	switch (robot.dir)
	{
	case 1:
		robotVertexesX[0] = pos2PixelPos(robot.pos).x;
		robotVertexesX[1] = pos2PixelPos(robot.pos).x;
		robotVertexesX[2] = pos2PixelPos(robot.pos).x + SQUARE_LEN;
		robotVertexesY[0] = pos2PixelPos(robot.pos).y;
		robotVertexesY[1] = pos2PixelPos(robot.pos).y + SQUARE_LEN;
		robotVertexesY[2] = pos2PixelPos(robot.pos).y + SEMI_SQUARE_LEN;
		break;
	case 2:
		robotVertexesX[0] = pos2PixelPos(robot.pos).x;
		robotVertexesX[1] = pos2PixelPos(robot.pos).x + SQUARE_LEN;
		robotVertexesX[2] = pos2PixelPos(robot.pos).x + SEMI_SQUARE_LEN;
		robotVertexesY[0] = pos2PixelPos(robot.pos).y;
		robotVertexesY[1] = pos2PixelPos(robot.pos).y;
		robotVertexesY[2] = pos2PixelPos(robot.pos).y + SQUARE_LEN;
		break;
	case 3:
		robotVertexesX[0] = pos2PixelPos(robot.pos).x + SQUARE_LEN;
		robotVertexesX[1] = pos2PixelPos(robot.pos).x;
		robotVertexesX[2] = pos2PixelPos(robot.pos).x + SQUARE_LEN;
		robotVertexesY[0] = pos2PixelPos(robot.pos).y;
		robotVertexesY[1] = pos2PixelPos(robot.pos).y + SEMI_SQUARE_LEN;
		robotVertexesY[2] = pos2PixelPos(robot.pos).y + SQUARE_LEN;
		break;
	case 4:
		robotVertexesX[0] = pos2PixelPos(robot.pos).x;
		robotVertexesX[1] = pos2PixelPos(robot.pos).x + SEMI_SQUARE_LEN;
		robotVertexesX[2] = pos2PixelPos(robot.pos).x + SQUARE_LEN;
		robotVertexesY[0] = pos2PixelPos(robot.pos).y + SQUARE_LEN;
		robotVertexesY[1] = pos2PixelPos(robot.pos).y;
		robotVertexesY[2] = pos2PixelPos(robot.pos).y + SQUARE_LEN;
		break;
	default:
		drawString("something wrong with robot direction", 125, 125);
	}

	setColour(green);
	fillPolygon(3, robotVertexesX, robotVertexesY);
}