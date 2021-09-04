#pragma once

/*
* \brief ������� ����� ������������
*/
class Triangles {
protected:

    double _side1;
    double _side2;
    double _corner;

public:

    /*
    * \brief ������ ����������� ������� ��� ���������� ������� ������
    */
    virtual double calcArea() = 0;

    /*
    * \brief ������ ����������� ������� ��� ���������� ��������� ������
    */
    virtual double calcPerimetr() = 0;

    /*
    * \brief ����������� ����������
    */
    virtual ~Triangles() = 0;

    Triangles(double side1, double side2, double corner) 
        : _side1(side1), _side2(side2), _corner(corner) 
    {}

};

/*
* \brief �������� ����� ����
*/
class Rhombus : public Triangles {
public:

    /*
* \brief ����������� �� ���������
*/
    Rhombus(double side1, double side2) : _side1(side1), _side2(side2)
    {}

    /*
    * \brief ����������� ����������� �� ���������
    */
    Rhombus(const Rhombus& rhomb) = default;

    /*
    * \brief ����������
    */
    ~Rhombus() = default;

    /*
    * \brief ����� ���������� ���������
    */
    double calcPerimetr() {
        return (_side1 + _side2 + _side3);
    };

    /*
    * \brief ����� ���������� �������
    */
    double calcArea() override {
        return _a * _h;
    };

};

/*
* \brief �������� ����� ��������������
*/
class Parallelepiped : public Triangles {
private:

    /*
    * \brief �������
    */
    double _a;

    /*
    * \brief �������
    */
    double _b;

    /*
    * \brief �������
    */
    double _c;

public:

    /*
    * \brief ����������� �� ���������
    */
    Parallelepiped(double a, double b, double c) : _a(a), _b(b), _c(c)
    {}

    /*
    * \brief ����������� ����������� �� ���������
    */
    Parallelepiped(const Parallelepiped& parped) = default;

    /*
    * \brief ����������
    */
    ~Parallelepiped() = default;

    /*
    * \brief ����� ���������� �������
    */
    double calcArea() override {
        return 2 * _a * _b + 2 * _a * _c + 2 * _b * _c;
    };

    /*
    * \brief ����� ���������� ������
    */
    double calcVolume() {
        return _a * _b * _c;
    };

};

/*
* \brief �������� ����� ������
*/
class Ellipse : public Triangles {
private:

    /*
    * \brief �������
    */
    double _a;

    /*
    * \brief �������
    */
    double _b;

    /*
    * \brief ��������� ��
    */
    const double pi = 3.14159;

public:

    /*
    * \brief ����������� �� ���������
    */
    Ellipse(double a, double b) : _a(a), _b(b)
    {}

    /*
    * \brief ����������� ����������� �� ���������
    */
    Ellipse(const Ellipse &el) = default;

    /*
    * \brief ����������
    */
    ~Ellipse() = 0;

    /*
    * \brief ����� ���������� ���������
    */
    double calcPerimetr() {
        return 4 * (pi * _a * _b + pow(_a - _b, 2)) / (_a + _b);
    };

    /*
    * \brief ����� ���������� �������
    */
    double calcArea() override {
        return _a * _b * pi;
    };

};