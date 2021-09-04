#include <iostream>
using namespace std;
#include "Man.h"

void Man::setName(const string& name) { m_name = name; }
string Man::getName() const { return m_name; }

void Man::setAge(unsigned short int age) { 
    try { 
        if (age > maxAge){ throw "Incorrect age"; }
    }
    catch (const char* msg) { cerr << msg << endl; }
}
unsigned short int Man::getAge() const { return m_age; }

void Man::setGender(const string& gender) { m_gender = gender; }
string Man::getGender() const { return m_gender; }

void Man::setWeight(unsigned short int weight) {
    try {
        if (weight > maxWeight) { throw "Incorrect weight"; }
    }
    catch (const char* msg) { cerr << msg << endl; }
}
unsigned short int Man::getWeight() const { return m_weight; }

void Student::setStudyYears(const short unsigned int studyYears) {
    try {
        if (studyYears > maxStudyYears) { "Incorrect study years"; }
    }
    catch (const char* msg) { cerr << msg << endl; }
}

short unsigned int Student::getStudyYears() const { return m_studyYears; }

void Student::addStudyYears(short int num) try {
    if (num > 10) { "Incorrect value"; }
}
catch (const char* msg) { cerr << msg << endl; }

ostream& operator<< (std::ostream& out, const Man& man)
{
    out << "Name: " << man.getName() << endl 
        << "Age: " << man.getAge() << endl
        << "Gender: " << man.getGender() << endl
        << "Weight: " << man.getWeight() << endl
        << endl;
    return out;
}

istream& operator>>(istream& in, Man& man)
{
    cout << "Man: " << endl;
    in >> man.m_name;
    in >> man.m_age;
    in >> man.m_gender;
    in >> man.m_weight;

    return in;
}

ostream& operator<<(std::ostream& out, const Student& student)
{
    out << "Name: " << student.getName() << endl
        << "Age: " << student.getAge() << endl
        << "Gender: " << student.getGender() << endl
        << "Weight: " << student.getWeight() << endl
        << "Study years: " << student.getStudyYears() << endl
        << endl;
    return out;
}

istream& operator>>(istream& in, Student& student)
{
    cout << "Student: " << endl;
    in >> student.m_name;
    in >> student.m_age;
    in >> student.m_gender;
    in >> student.m_weight;
    in >> student.m_studyYears;

    return in;
}
