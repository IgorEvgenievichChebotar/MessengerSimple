#include <iostream>
using namespace std;


void selection_sort(int data[], const int len)
{
    int j = 0;
    int tmp = 0;
    for (int i = 0; i < len; i++) {
        j = i;
        for (int k = i; k < len; k++) {
            if (data[j] > data[k]) {
                j = k;
            }
        }
        tmp = data[i];
        data[i] = data[j];
        data[j] = tmp;
    }
}

void bubble_sort(int data[], const int len)
{
    int tmp = 0;
    for (int i = 0; i < len; i++) {
        for (int j = (len - 1); j >= (i + 1); j--) {
            if (data[j] < data[j - 1]) {
                tmp = data[j];
                data[j] = data[j - 1];
                data[j - 1] = tmp;
            }
        }
    }
}

void insertion_sort(int data[], const int len)
{
    int key = 0;
    int i = 0;
    for (int j = 1; j < len; j++) {
        key = data[j];
        i = j - 1;
        while (i >= 0 && data[i] > key) {
            data[i + 1] = data[i];
            i = i - 1;
            data[i + 1] = key;
        }
    }

}

void print(int data[], const int len) {
    for (int i = 0; i < len; i++)
    {
        cout << data[i] << " ";
    }
}

int main()
{
    setlocale(0, "ru");
    cout << "Введите длину массива (списка):" << endl;
    int len;
    cin >> len;
    cout << "Введите массив (список):" << endl;
    int data[100]{};
    for (int i = 0; i < len; i++)
    {
        cin >> data[i];
    }
    cout << "Как отсортировать массив (список)?" << endl;
    cout << "Введите: 1 - selection, 2 - bubble, 3 - insertion" << endl;
    int sel;
    cin >> sel;
    switch (sel) {
    case (1):
        selection_sort(data, len);
        cout << "Результат: ";
        print(data, len);
        break;
    case (2):
        bubble_sort(data, len);
        cout << "Результат: ";
        print(data, len);
        break;
    case (3):
        insertion_sort(data, len);
        cout << "Результат: ";
        print(data, len);
        break;
    default:
        cout << "error" << endl;
    }

}