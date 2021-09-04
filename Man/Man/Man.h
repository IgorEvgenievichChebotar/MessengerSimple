#pragma once
using namespace std;

/*
* \brief Класс Man
*/
class Man {
private:

	/*
	* \brief Символьная константа для проверки корректности ввода
	*/
	const unsigned int maxWeight{ 100 };

	/*
	* \brief Символьная константа для проверки корректности ввода
	*/
	const unsigned int maxAge{ 100 };

protected:

	/*
	* \brief Имя
	*/
	string m_name;

	/*
	* \brief Возраст
	*/
	unsigned short int m_age;

	/*
	* \brief Пол
	*/
	string m_gender;

	/*
	* \brief Вес
	*/
	unsigned short int m_weight;

	/*
	* \brief Конструктор копирования по умолчанию
	*/
	Man(const Man& man) = default;

public:

	/*
	* \brief Конструктор с параметрами по умолчанию
	* \param name Имя
	* \param age Возраст
	* \param gender Пол
	* \param weight Вес
	*/
	Man(string name = "Vasya",
		unsigned short int age = 20,
		string gender = "getero",
		unsigned short int weight = 80)
		: m_name(name), m_age(age), m_gender(gender), m_weight(weight) 
	{
		/*
		* \brief Обработка исключений
		*/
		try { 
			if (age > maxAge) { throw "Incorrect age"; } 
			if (weight > maxWeight) { throw "Incorrect weight"; }
		}
		catch (const char* msg) { cerr << msg << endl; }
	}

	/*
	* \brief Деструктор
	*/
	~Man() = default;

	/*
	* \brief Сеттер для имени
	*/
	void setName(const string& name);

	/*
	* \brief Геттер для имени
	*/
	string getName() const;

	/*
	* \brief Сеттер для возраста
	*/
	void setAge(unsigned short int age);

	/*
	* \brief Геттер для возраста
	*/
	unsigned short int getAge() const;

	/*
	* \brief Сеттер для пола
	*/
	void setGender(const string& gender);

	/*
	* \brief Геттер для пола
	*/
	string getGender() const;

	/*
	* \brief Сеттер для веса
	*/
	void setWeight(unsigned short int weight);

	/*
	* \brief Геттер для веса
	*/
	unsigned short int getWeight() const;

	/*
	* \brief Оператор присваивания
	*/
	Man operator=(const Man& man) {
		m_name = man.m_name;
		m_age = man.m_age;
		m_gender = man.m_gender;
		m_weight = man.m_weight;
		return man;
	};

	/*
	* \brief Оператор вывода
	*/
	friend ostream& operator<< (ostream& out, const Man& man);

	/*
	* \brief Оператор ввода
	*/
	friend istream& operator>> (istream& in, Man& man);

};

/*
* \brief Класс Student
*/
class Student : public Man {
private:

	/*
	* \brief Символьная константа для проверки корректности ввода
	*/
	const unsigned int maxStudyYears{ 10 };

	/*
	* \brief Года обучения
	*/
	short unsigned int m_studyYears;

	/*
	* \brief Конструктор копирования по умолчанию
	*/
	Student(const Student &student) = default;

public:

	/*
	* \brief Конструктор с параметрами по умолчанию
	*/
	Student(short unsigned int studyYears = 0) : m_studyYears(studyYears) 
	{
		/*
		* \brief Обработка исключений
		*/
		try {
			if (studyYears > maxStudyYears) { "Incorrect study years"; }
		}
		catch (const char* msg) { cerr << msg << endl; }
	}

	/*
	* \brief Деструктор
	*/
	~Student() = default;

	/*
	* \brief Сеттер для годов обучения
	*/
	void setStudyYears(const short unsigned int studyYears);

	/*
	* \brief Геттер для годов обучения
	*/
	short unsigned int getStudyYears() const;

	/*
	* \brief Метод для увеличения лет обучения
	*/
	void addStudyYears(short int num);

	/*
	* \brief Оператор присваивания
	*/
	Student operator=(const Student& student) {
		m_name = student.m_name;
		m_age = student.m_age;
		m_gender = student.m_gender;
		m_weight = student.m_weight;
		m_studyYears = student.m_studyYears;
		return student;
	};

	/*
	* \brief Оператор вывода
	*/
	friend ostream& operator<< (ostream& out, const Student& student);

	/*
	* \brief Оператор вывода
	*/
	friend istream& operator>> (istream& in, Student& student);

};