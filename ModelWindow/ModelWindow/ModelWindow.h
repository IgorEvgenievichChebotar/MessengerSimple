using namespace std;
#include <iostream>
/*
* \brief Класс для работы с моделями экранных окон
*/
class ModelWindow {
private:

	/*
	* \brief Заголовок окна
	*/
	string m_title;

	/*
	* \brief Цвет окна
	*/
	struct color {
		unsigned int m_red;
		unsigned int m_green;
		unsigned int m_blue;
	}; color color;
	color.m_red = 1;



	/*
	* \brief Координаты левого верхнего угла
	*/
	struct coords {
		unsigned int m_x;
		unsigned int m_y;
	}; coords coords;

	/*
	* \brief Размер окна
	*/
	struct size {
		unsigned int m_horizontalSize;
		unsigned int m_verticalSize;
	}; size size;

	/*
	* \brief Видимость окна
	*/
	bool m_visibility;

	/*
	* \brief Наличие рамки у окна
	*/
	bool m_hasFrame;

public:

	/*
	* \brief Параметризированный конструктор
	* \ param title Заголовок окна
	* \ param coords Координаты левого верхнего угла
	* \ param size Размер окна
	* \ param color Цвет окна
	* \ param visibility Видимость окна
	* \ param hasFrame Наличие рамки у окна
	*/
	ModelWindow(
		const string title,
		const unsigned int red,
		const unsigned int green,
		const unsigned int blue,
		const unsigned int x,
		const unsigned int y,
		const unsigned int horizontalSize,
		const unsigned int verticalSize,
		const bool visibility,
		const bool hasFrame
	) : m_title(title),
		color.m_red(red),
		color.m_green(green),
		color.m_blue(blue),
		coords.m_x(x),
		coords.m_y(y),
		size.m_horizontalSize(horizontalSize),
		size.m_verticalSize(verticalSize),
		m_visibility(visibility),
		m_hasFrame(hasFrame) 
	{}

	/*
	* \brief Конструктор копирования
	* \other Копируемые данные
	*/
	ModelWindow(const ModelWindow& other);

	/*
	* \brief Деструктор
	*/
	~ModelWindow() = default;

	/*
	* \brief Метод установки заголовка окна
	*/
	void setTitle(const string &title);
	string getTitle() const;

	/*
	* \brief Метод изменения цвета окна
	*/
	void setColor(const unsigned int r, const unsigned int g, const unsigned int b);
	string getColor() const;

	/*
	* \brief Метод перемещения окна
	*/
	void setCoords(const struct coords);
	string getCoords() const;

	/*
	* \brief Метод изменения размера окна
	*/
	void setSize(const struct size);
	string getSize() const;

	/*
	* \brief Метод для установки состояния окна (видимое/невидимое)
	*/
	void setVisibility(const bool visibility);
	string getVisibility() const;

	/*
	* \brief Метод для установки состояния окна (есть рамка/нет рамки)
	*/
	void setFrame(const bool hasFrame);
	string getFrame() const;

};