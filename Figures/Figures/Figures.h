#pragma once

/*
* \brief Базовый класс Треугольники
*/
class Triangles {
protected:

    double _side1;
    double _side2;
    double _corner;

public:

    /*
    * \brief Чистая виртуальная функция для вычисления площади фигуры
    */
    virtual double calcArea() = 0;

    /*
    * \brief Чистая виртуальная функция для вычисления периметра фигуры
    */
    virtual double calcPerimetr() = 0;

    /*
    * \brief Виртуальный деструктор
    */
    virtual ~Triangles() = 0;

    Triangles(double side1, double side2, double corner) 
        : _side1(side1), _side2(side2), _corner(corner) 
    {}

};

/*
* \brief Дочерний класс ромб
*/
class Rhombus : public Triangles {
public:

    /*
* \brief Конструктор по умолчанию
*/
    Rhombus(double side1, double side2) : _side1(side1), _side2(side2)
    {}

    /*
    * \brief Конструктор копирования по умолчанию
    */
    Rhombus(const Rhombus& rhomb) = default;

    /*
    * \brief Деструктор
    */
    ~Rhombus() = default;

    /*
    * \brief Метод вычисления периметра
    */
    double calcPerimetr() {
        return (_side1 + _side2 + _side3);
    };

    /*
    * \brief Метод вычисления площади
    */
    double calcArea() override {
        return _a * _h;
    };

};

/*
* \brief Дочерний класс параллелепипед
*/
class Parallelepiped : public Triangles {
private:

    /*
    * \brief Сторона
    */
    double _a;

    /*
    * \brief Сторона
    */
    double _b;

    /*
    * \brief Сторона
    */
    double _c;

public:

    /*
    * \brief Конструктор по умолчанию
    */
    Parallelepiped(double a, double b, double c) : _a(a), _b(b), _c(c)
    {}

    /*
    * \brief Конструктор копирования по умолчанию
    */
    Parallelepiped(const Parallelepiped& parped) = default;

    /*
    * \brief Деструктор
    */
    ~Parallelepiped() = default;

    /*
    * \brief Метод вычисления площади
    */
    double calcArea() override {
        return 2 * _a * _b + 2 * _a * _c + 2 * _b * _c;
    };

    /*
    * \brief Метод вычисления объема
    */
    double calcVolume() {
        return _a * _b * _c;
    };

};

/*
* \brief Дочерний класс эллипс
*/
class Ellipse : public Triangles {
private:

    /*
    * \brief Сторона
    */
    double _a;

    /*
    * \brief Сторона
    */
    double _b;

    /*
    * \brief Константа пи
    */
    const double pi = 3.14159;

public:

    /*
    * \brief Конструктор по умолчанию
    */
    Ellipse(double a, double b) : _a(a), _b(b)
    {}

    /*
    * \brief Конструктор копирования по умолчанию
    */
    Ellipse(const Ellipse &el) = default;

    /*
    * \brief Деструктор
    */
    ~Ellipse() = 0;

    /*
    * \brief Метод вычисления периметра
    */
    double calcPerimetr() {
        return 4 * (pi * _a * _b + pow(_a - _b, 2)) / (_a + _b);
    };

    /*
    * \brief Метод вычисления площади
    */
    double calcArea() override {
        return _a * _b * pi;
    };

};