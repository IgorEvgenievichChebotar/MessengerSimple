#include <iostream>
#include <clocale>
#include <vector>
using namespace std;

constexpr int MAX_CONNECTED_IN = 6; // максимальное кол-во связей К ЭТОМУ элементу
constexpr int MAX_CONNECTED_TO = 1; // максимальное кол-во связей ОТ ЭТОГО элемента

class Node {
private:

	int m_value = 0;
	string m_name = "node";
	vector <string> m_connected_to;
	vector <string> m_connected_in;

public:

	Node(string name) {
		m_name = name;
	}

	Node(int value, string name) {
		m_value = value;
		m_name = name;
	}

	Node(string name, int value) {
		m_value = value;
		m_name = name;
	}

	void connect(Node* target_node) {
		if (m_connected_to.size() >= MAX_CONNECTED_TO) {
			cerr << "Превышено кол-во связей self node" << endl;
		}
		else if (target_node->m_connected_in.size() >= MAX_CONNECTED_IN) {
			cerr << "Превышено кол-во связей target node" << endl;
		}
		else {
			//cout << "Подключено" << endl;
			m_connected_to.push_back(target_node->m_name);
			target_node->m_connected_in.push_back(m_name);
		}
	}

	void disconnect(Node* target_node) {
		//cout << "Отключено" << endl;

		auto it1 = remove(
			m_connected_to.begin(), m_connected_to.end(), target_node->m_name
		);
		m_connected_to.erase(it1, m_connected_to.end());

		auto it2 = remove(
			target_node->m_connected_in.begin(), target_node->m_connected_in.end(), m_name
		);
		target_node->m_connected_in.erase(it2, target_node->m_connected_in.end());

	}

	void which_connected() {
		for (int r = 0; r < m_connected_in.size(); r++) {
			cout << m_connected_in[r] << ", ";
		}
	}

	void to_which_connected() {
		for (int r = 0; r < m_connected_to.size(); r++) {
			cout << m_connected_to[r] << ", ";
		}
	}

	void set_value(int value) {
		m_value = value;
	}

	void get_value() {
		cout << m_value << endl;
	}

	void node_info() {
		cout << "Узел: " << m_name << endl;
		cout << "Значение: " << m_value << endl;
		cout << "К кому подключен: "; to_which_connected(); cout << endl;
		cout << "Кто подключен: "; which_connected(); cout << endl;
	}
};

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