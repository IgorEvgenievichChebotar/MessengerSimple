#include <cmath>
#include <iostream>
#include "Figures.h"
using namespace std;

int main() {

	Rhombus rhomb(2, 4);
	cout << rhomb.calcPerimetr() << endl;
	cout << rhomb.calcArea() << endl;

	Parallelepiped par(1, 2, 3);
	cout << par.calcArea() << endl;
	cout << par.calcVolume() << endl;

	Ellipse el(4, 8);
	cout << el.calcPerimetr() << endl;
	cout << el.calcArea() << endl;

	

}