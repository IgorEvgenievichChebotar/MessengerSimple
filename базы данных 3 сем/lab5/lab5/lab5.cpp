#include <iostream>
#include <clocale>
#include <vector>
using namespace std;

/**
 * \brief максимальное кол-во связей К ЭТОМУ элементу
 */
constexpr int max_connected_in = 6;
/**
 * \brief максимальное кол-во связей ОТ ЭТОГО элемента
 */
constexpr int max_connected_to = 1;

class node {
private:

	int value_ = 0;
	string name_ = "node";
	vector <string> connected_to_;
	vector <string> connected_in_;

public:
	explicit node(string name) : name_(std::move(name))
	{
	}

	node(const int value, string name) : value_(value), name_(std::move(name))
	{
	}

	node(string name, const int value) : value_(value), name_(std::move(name))
	{
	}

	void connect(node* target_node);
	void disconnect(node* target_node);
	void which_connected() const;
	void to_which_connected() const;
	void set_value(const int &value);
	void get_value() const;
	void node_info() const;

};


void node::connect(node* target_node) {
	if (this->connected_to_.size() >= max_connected_to) {
		cerr << "Превышено кол-во связей self node" << endl;
	}
	else if (target_node->connected_in_.size() >= max_connected_in) {
		cerr << "Превышено кол-во связей target node" << endl;
	}
	else {
		this->connected_to_.push_back(target_node->name_);
		target_node->connected_in_.push_back(name_);
	}
}

void node::disconnect(node* target_node) {

	const auto it1 = remove(
		this->connected_to_.begin(), this->connected_to_.end(), target_node->name_
	);
	this->connected_to_.erase(it1, this->connected_to_.end());

	const auto it2 = remove(
		target_node->connected_in_.begin(), target_node->connected_in_.end(), this->name_
	);
	target_node->connected_in_.erase(it2, target_node->connected_in_.end());

}

void node::which_connected() const
{
	for (const auto& r : this->connected_in_)
	{
		cout << r << ", ";
	}
}

void node::to_which_connected() const
{
	for (const auto& r : this->connected_to_)
	{
		cout << r << ", ";
	}
}

void node::set_value(const int& value)
{
	this->value_ = value;
}

void node::get_value() const
{
	cout << this->value_ << endl;
}

void node::node_info() const
{
	cout << "Узел: " << this->name_ << endl;
	cout << "Значение: " << this->value_ << endl;
	cout << "К кому подключен: "; to_which_connected(); cout << endl;
	cout << "Кто подключен: "; which_connected(); cout << endl;
}

int main() {
	setlocale(0, "Rus");

	node node1(10, "node1");
	node node2("node2");
	node node3("node3");
	node node4("node4", 20);
	node node5("node5", 25);

	node2.connect(&node1);
	node3.connect(&node2);

	node2.set_value(50);

	node2.node_info();

}

