#include <iostream> 
constexpr auto nmax = 10;
using namespace std;

struct Stack {
    int arr[nmax]{};
    int head = -1;   //Индекс крайнего элемента.

    void push(const int x) {
        head++;
        arr[head] = x;
        cout << "Добавлен элемент: " << x << endl;
    }

    int pop() {
        if (head != -1) {
            cout << "Удален элемент " << arr[head] << endl;
            arr[head] = 0;
            head--;
            return arr[head + 1];
        }
        else {
            cout << "Ошибка, попытка извлечь элемент из пустого стека" << endl;
        }
        return 0;
    }

    bool is_empty() const
    {
        return head == -1;
    }

    void display()
    {
        cout << "Стек: ";
        for (int n : arr)
            cout << n << "  ";
        cout << endl;
    }

};

struct Deque {
    int arr[nmax]{};

    //Используя такие начальные значения индексов, у нас
    //будет свободная память как слева, так и справа.
    int head = nmax / 2;    //Индекс первого элемента.
    int tail = nmax / 2;    //Индекс элемента, следующего за последним.

    void push_front(const int x) {
        head--;
        arr[head] = x;
        cout << "Добавлен элемент " << x << endl;
    }

    void push_back(int x) {
        arr[tail] = x;
        tail++;
        cout << "Добавлен элемент " << x << endl;
    }

    int pop_front() {
        if (head != tail) {
            cout << "Удален элемент " << arr[head] << endl;
            arr[head] = 0;
            head++;
            return arr[head - 1];
        }
        else {
            cout << "На месте " << tail << " элемента нет" << endl;
            tail--;
        }
        return 0;
    }

    int pop_back() {
        if (head != tail) {
            cout << "Удален элемент " << arr[head] << endl;
            arr[head] = 0;
            tail--;
            return arr[tail];
        }
        else {
            cout << "На месте " << tail << " элемента нет" << endl;
            tail--;
        }
        return 0;
    }

    bool is_empty() const
    {
        return head == tail;
    }

    void display()
    {
        cout << "Дек: ";
        for (const int &n : arr)
            cout << n << "  ";
        cout << endl;

    }

    Deque operator=(Stack& stk);

};

Deque Deque::operator=(Stack& stk) {
    cout << "Стек преобразован в дек" << endl;
    int i = 0;
    for (const int &stk_elem : stk.arr) {
        arr[i++] = stk_elem;
    }
    return *this;
}

int main() {
    setlocale(0, "Rus");

    Stack stack1;
    stack1.push(1);
    stack1.push(2);
    stack1.push(3);
    stack1.push(4);
    stack1.pop();
    stack1.display();

    Deque deque1;
    deque1.push_front(5);
    deque1.push_back(4);
    deque1.display();

    Deque deque2;
    deque2 = stack1;

    deque2.display();

    deque2.push_back(7);
    deque2.push_back(8);
    deque2.push_back(9);
    deque2.push_front(6);

    deque2.display();

    deque2.pop_front();
    deque2.pop_back();

    deque2.display();

}