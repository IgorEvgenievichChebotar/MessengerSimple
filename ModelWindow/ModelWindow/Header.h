#pragma execution_character_set("utf-8")
class ModelWindow {
private:

	string title;
	unsigned int topleftCorner; //coordinates
	unsigned int horizontalSize;
	unsigned int verticalSize;
	unsigned int color;
	bool visibility;
	bool hasFrame;

public:

	/*
	* \brief Параметризированный конструктор
	* \ param title Название окна
	* \ param topleftcorner Координаты левого верхнего угла
	* \ param horizontalsize Размер окна по горизонтали
	* \ param verticalsyze Размер окна по вертикали
	* \ param color Цвет окна
	* \ param visibility Видимость окна
	* \ param frame Наличие рамки у окна
	*/
	ModelWindow(const string title,
		const unsigned int topleftCorner,
		const unsigned int horizontalSize,
		const unsigned int verticalSize,
		const unsigned int color,
		const bool visibility,
		const bool hasFrame
	);
	/*
	* \brief Конструктор копирования
	* \other Копируемые данные
	*/
	ModelWindow(const ModelWindow& other);
	/*
	* \brief Деструктор
	*/
	~ModelWindow();

	/*
	* \brief Функция вывода параметров объекта
	*/
	string get() const;
	/*
	* \brief Функция ввода параметров объекта
	*/
	ModelWindow set() const;

	/*
	* \brief Метод перемещения окна
	*/
	unsigned int moving(const unsigned int topleftCorner) const;
	/*
	* \brief Метод изменения размера окна
	*/
	unsigned int sizing(const unsigned int horizontalSize, const unsigned int verticalSize) const;
	/*
	* \brief Метод изменения цвета окна
	*/
	unsigned int coloring(const unsigned int color) const;
	/*
	* \brief Метод, получающий или изменяющий статус
	*/
	ModelWindow& status(const ModelWindow& other) const;

};