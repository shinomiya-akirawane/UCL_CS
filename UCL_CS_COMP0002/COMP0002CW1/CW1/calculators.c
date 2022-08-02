#include "structs.h"
#include "gridParameter.h"
#include "function.h"
#include <stdlib.h>
#include <stdio.h>
double mySqrt(int x)
{
	double ans, lastAns;
	ans = x;
	const double minorNum = 0.0000001;
	if (x <= 0)
		return 0;
	do
	{
		lastAns = ans;
		ans = (ans + x / ans) / 2;
	} while (abs(lastAns - ans) > 0.0000001);
	return ans;
}

struct Pos pos2PixelPos(struct Pos pos)
{
	struct Pos pixelPos;
	pixelPos.x = (pos.x) * SQUARE_LEN;
	pixelPos.y = (pos.y) * SQUARE_LEN;
	return pixelPos;
}

int randomNum(int min, int max)
{
	int num;
	num = rand() % (max - min) + min;
	return num;
}

double calDis(struct Pos a, struct Pos b)
{
	double dis = mySqrt((a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y));
	return dis;
}
