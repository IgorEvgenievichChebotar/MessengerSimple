#include <iostream>
#include <clocale>
#include <vector>
using namespace std;

constexpr int MAX_CONNECTED_IN = 6; // максимальное кол-во связей К ЭТОМУ элементу
constexpr int MAX_CONNECTED_TO = 1; // максимальное кол-во связей ОТ ЭТОГО элемента

class Node {
private:

	int value = 0;
	string name = "node";
	vector <string> connected_to;
	vector <string> connected_in;

public:

	Node(string name) {
		this->name = name;
	}

	Node(int value, string name) {
		this->value = value;
		this->name = name;
	}

	Node(string name, int value) {
		this->value = value;
		this->name = name;
	}

	void connect(Node* target_node);
	void disconnect(Node* target_node);
	void which_connected();
	void to_which_connected();
	void set_value(const int &value);
	void get_value();
	void node_info();
};


void Node::connect(Node* target_node) {
	if (this->connected_to.size() >= MAX_CONNECTED_TO) {
		cerr << "Превышено кол-во связей self node" << endl;
	}
	else if (target_node->connected_in.size() >= MAX_CONNECTED_IN) {
		cerr << "Превышено кол-во связей target node" << endl;
	}
	else {
		//cout << "Подключено" << endl;
		this->connected_to.push_back(target_node->name);
		target_node->connected_in.push_back(name);
	}
}

void Node::disconnect(Node* target_node) {
	//cout << "Отключено" << endl;

	auto it1 = remove(
		this->connected_to.begin(), this->connected_to.end(), target_node->name
	);
	this->connected_to.erase(it1, this->connected_to.end());

	auto it2 = remove(
		target_node->connected_in.begin(), target_node->connected_in.end(), this->name
	);
	target_node->connected_in.erase(it2, target_node->connected_in.end());

}

void Node::which_connected() {
	for (int r = 0; r < this->connected_in.size(); r++) {
		cout << this->connected_in[r] << ", ";
	}
}

void Node::to_which_connected() {
	for (int r = 0; r < this->connected_to.size(); r++) {
		cout << this->connected_to[r] << ", ";
	}
}

void Node::set_value(const int &value) {
	this->value = value;
}

void Node::get_value() {
	cout << this->value << endl;
}

void Node::node_info() {
	cout << "Узел: " << this->name << endl;
	cout << "Значение: " << this->value << endl;
	cout << "К кому подключен: "; to_which_connected(); cout << endl;
	cout << "Кто подключен: "; which_connected(); cout << endl;
}


int main() {
	setlocale(0, "Rus");

	Node node1(10, "node1");
	Node node2("node2");
	Node node3("node3");
	Node node4("node4", 20);

	node2.connect(&node1);
	node3.connect(&node2);

	node2.set_value(50);

	node2.node_info();
}