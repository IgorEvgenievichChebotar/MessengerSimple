#include <iostream>
using namespace std;
#include "Man.h"

void printMan(const Man& man);
void printStud(const Student& student);

int main() {

	Man man("Igor", 19, "getero", 70);
	cout << man;
	
	man.setName("Ivan");
	man.setAge(25);
	man.setGender("gomo");
	man.setWeight(100);
	cout << man;

	Man copyMan;
	copyMan = man;
	cout << copyMan;

	Student student(5);
	
	student.setStudyYears(10);
	student.addStudyYears(5);
	cout << student;

	Student copyStudent;
	copyStudent = student;
	cout << copyStudent;

	student.setName("Anatoly"); // Демонстрация принципа подстановки
	cout << student;

	Student student2;
	cin >> student2;
	cout << student2;

}

void printMan(const Man& man) {
	cout << endl;
	cout << "Name: " << man.getName() << endl;
	cout << "Age: " << man.getAge() << endl;
	cout << "Gender: " << man.getGender() << endl;
	cout << "Weight: " << man.getWeight() << endl;
	cout << endl;
}

void printStud(const Student& student) {
	cout << endl;
	cout << "Name: " << student.getName() << endl;
	cout << "Age: " << student.getAge() << endl;
	cout << "Gender: " << student.getGender() << endl;
	cout << "Weight: " << student.getWeight() << endl;
	cout << "Study years: " << student.getStudyYears() << endl;
	cout << endl;
}
