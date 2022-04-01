#include <iostream>
#include <string>
using namespace std;

template<typename T>
class List {
public:
    List();
    ~List();
    void push_back(T data);//Добавление элемента с конца
    void push_front(T data);//Добавление элемента в начало
    void pop_back();//Удалить последний элемент
    void pop_front();//Удалить первый элемент
    int get_size() {
        return size;
    }//Количество элементов в списке
    T& operator[](const int index);//Определение индекса элемента
    void clear_line();//Удалить строку полностью
    void insert(T value, int index);//Добавление элемента на указанную позицию
    void removeAt(int index);//Удаление элемента с указанной позиции
    

private:
    template<typename T>
    class Node {
    public:
        Node* pNext;
        T data;
        Node(T data = T(), Node* pNext = nullptr)/*pNext=nullptr*/ {
            this->data = data;
            this->pNext = pNext;
        }
    };
    int size;
    Node<T>* head;
};

template<typename T>
List<T>::List() {
    size = 0;
    head = nullptr;
}

template <typename T>
void List <T> ::push_back(T data) {
    if (head == nullptr) {
        head = new Node<T>(data);
    }
    else {
        Node<T>* current = this->head;
        while (current->pNext != nullptr) {
            current = current->pNext;
        }
        current->pNext = new Node<T>(data);
    }
    size++;
}
template <typename T>
T& List<T>::operator[](const int index) {
    int counter = 0;
    Node<T>* current = this->head;
    while (current != nullptr) {
        if (counter == index) {
            return current->data;
        }
        current = current->pNext;
        counter++;
    }
}
template<typename T>
void List<T>::pop_front() {
    Node<T>* temp = head;
    head = head->pNext;
    delete[] temp;
    size--;
}

template<typename T>
void List<T>::clear_line() {
    while (size > 0) {
        pop_front();
    }
}
template<typename T>
void List<T>::push_front(T data) {
    head = new Node<T>(data, head);
    size++;
}

template<typename T>
void List<T>::insert(T value, int index) {
    if (index == 0) {
        push_front(value);
    }
    else {
        Node<T>* previous = this->head;
        for (int i = 0; i < index - 1; i++) {
            previous = previous->pNext;
        }
        Node<T>* newNode = new Node<T>(value, previous->pNext);
        previous->pNext = newNode;
        size++;
    }
}

template<typename T>
void List<T>::removeAt(int index) {
    if (index == 0) {
        pop_front();
    }
    else {
        Node<T>* previous = this->head;
        for (int i = 0; i < index - 1; i++) {
            previous = previous->pNext;
        }
        Node<T>* toDelete = previous->pNext;
        previous->pNext = toDelete->pNext;
        delete toDelete;
        size--;
    }
}

template<typename T>
void List<T>::pop_back() {
    removeAt(size - 1);
}

template<typename T>
List<T>::~List() {
    clear_line();
}

int main()
{
    setlocale(LC_ALL, "Russian");
    cout << "Введите количество строк" << endl;
    int raws;
    cin >> raws;
    List<int>* arr = new List<int>[raws];
    for (int i = 0; i < raws; i++) {
        List<int> lst;
        arr[i] = lst;
    }
    string choice1;
    string choice2;
    choice2 = "y";
    choice1 = "y";
    while (choice1 == "y") {
        cout << "Выберите строку" << endl;
        for (int i = 1; i <= raws; i++) {
            cout << i << " ";
        }
        cout << endl;
        int raw;
        cin >> raw;
        for (int i = 0; i < arr[raw - 1].get_size(); i++) {
            cout << arr[raw - 1][i] << " ";
        }
        while (choice2 == "y") {
            cout << "Что будете делать?" << endl << endl;
            cout << "1. Добавить элемент в список с конца" << endl;
            cout << "2. Добавить элемент в список с начала" << endl;
            cout << "3. Удалить первый элемент списка" << endl;
            cout << "4. Удалить последний элемент списка" << endl;
            cout << "5. Добавить элемнт на выбранную позицию" << endl;
            cout << "6. Удалить элемент из выбранной позиции" << endl;
            cout << "7. Вывести количество элементов списка" << endl;
            int chase;
            int n;
            cin >> chase;
            int index;
            switch (chase) {
            case 1:
                cout << "Введите число для вставки" << endl;
                cin >> n;
                arr[raw - 1].push_back(n);
                for (int i = 0; i < arr[raw - 1].get_size(); i++) {
                    cout << arr[raw - 1][i] << " ";
                }
                break;
            case 2:
                cout << "Введите число для вставки" << endl;
                cin >> n;
                arr[raw - 1].push_front(n);
                for (int i = 0; i < arr[raw - 1].get_size(); i++) {
                    cout << arr[raw - 1][i] << " ";

                }
                break;
            case 3:
                arr[raw - 1].pop_front();
                for (int i = 0; i < arr[raw - 1].get_size(); i++) {
                    cout << arr[raw - 1][i] << " ";
                }
                break;
            case 4:
                arr[raw - 1].pop_back();
                for (int i = 0; i < arr[raw - 1].get_size(); i++) {
                    cout << arr[raw - 1][i] << " ";
                }
                break;
            case 5:
                cout << "Введите позицию для вставки" << endl;
                cin >> index;
                cout << "Введите число для вставки" << endl;
                cin >> n;
                arr[raw - 1].insert(n, index);
                for (int i = 0; i < arr[raw - 1].get_size(); i++) {
                    cout << arr[raw - 1][i] << " ";
                }
                break;
            case 6:
                cout << "Введите позицию для удаления" << endl;
                cin >> index;

                arr[raw - 1].removeAt(index);
                for (int i = 0; i < arr[raw - 1].get_size(); i++) {
                    cout << arr[raw - 1][i] << " ";
                }
                break;
            default:
                arr[raw - 1].get_size();
                cout << endl;
                for (int i = 0; i < arr[raw - 1].get_size(); i++) {
                    cout << arr[raw - 1][i] << " ";
                }
                break;
            }
            cout << "Желаете продолжить с этой строкой?" << endl;
            cin >> choice2;
            if (choice2 != "y") {
                break;
            }
        }
        choice2 = "y";
        cout << "Желаете продолжить?" << endl;
        cin >> choice1;
        if (choice1 != "y") {
            break;
        }
    }

    for (int i = 0; i < raws; i++) {
        for (int j = 0; j < arr[i].get_size(); j++) {
            cout << arr[i][j] << " ";
        }
        cout << endl;
    }

    return 0;

}
