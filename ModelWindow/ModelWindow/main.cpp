#include "ModelWindow.h"
#include <iostream>
using namespace std;


int main()
{
	ModelWindow window("window", "black", 20, 30, 40, 0, 0);

	window.windowInfo();

	window.setTitle("Browser");
	window.setColor("Blue");
	window.move(50);
	window.setSize(100, 100);
	window.setVisibility(1);
	window.setFrame(1);

	window.windowInfo();
}