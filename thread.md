# Потоки в c++

Поток — это по сути последовательность инструкций, которые выполняются параллельно с другими потоками. Каждая программа создает по меньшей мере один поток: основной, который запускает функцию main(). Программа, использующая только главный поток, является однопоточной; если добавить один или более потоков, она станет многопоточной.
Потоки — это способ сделать несколько вещей одновременно. Это может быть полезно, например, для отображения анимации и обработки пользовательского ввода данных во время загрузки изображений или звуков. Потоки также широко используется в сетевом программировании, во время ожидания получения данные будет продолжаться обновление и рисование приложения.

Пример создания потока:
```c++
#include <thread>
 
void threadFunction()
{
     // do smth
}
 
int main()
{
     std::thread thr(threadFunction); // Поток запустится сразу после создания
     thr.join(); // Блокируем основной поток, пока thr не завершит свою работу
     return 0;
}
```

Если не ожидать завершения потоков, то они могут быть завершены раньше времени автоматически в момент, когда завершится основной поток программы.

## Передача параметров в поток.

Пример:
```c++
void threadFunction(int i, double d, const std::string &s)
{
     std::cout << i << ", " << d << ", " << s << std::endl;
}

int main()
{
     std::thread thr(threadFunction, 1, 2.34, "example"); // Все пераметры передаются по значению, даже если функция принимает ссылку
     thr.join(); // Блокируем основной поток, пока thr не завершит свою работу
     return 0;
}
```


## Передача параметров в поток по ссылке.

Если в функцию необходимо передать параметры по ссылке, они должны быть обернуты в `std::ref` или `std::cref`.

Пример:
```c++
void threadFunction(int &a)
{
     a++;
}
 
int main()
{
     int a = 1;
     std::thread thr(threadFunction, std::ref(a)); // Передаём параметр по ссылке
     thr.join(); // Блокируем основной поток, пока thr не завершит свою работу
     std::cout << a << std::endl; 
     return 0;
}
```

## Получение данных из потока
```c++
int threadFunction(int a, int b)
{
     return a + b;
}
 
int main()
{
     int a = 1;
     int b = 5;
     
     std::future<int> result;  // объект для хранения результатов асинхронных вычислений
     result = std::async(threadFunction, a, b);  // запуск функции в отдельном потоке
     
     result.wait();  // Блокируем основной поток
     std::cout << result.get() << std::endl; 
     return 0;
}
```

## Блокировки

Блокировки нужны, чтобы два и более потока не могли работать с одними и теми же общими данными

Мьютекс — базовый элемент синхронизации и в С++11 представлен в 4 формах в заголовочном файле <mutex>:
- mutex: обеспечивает базовые функции lock() и unlock() и не блокируемый метод try_lock()
- recursive_mutex: может войти «сам в себя»
- timed_mutex: в отличие от обычного мьютекса, имеет еще два метода: try_lock_for() и try_lock_until()
- recursive_timed_mutex: это комбинация timed_mutex и recursive_mutex

Пример
```c++
#include <iostream>
#include <chrono>
#include <thread>
#include <mutex>
 
std::mutex g_lock;
 
void threadFunction()
{
     g_lock.lock(); // Поток блокирует (отмечает) мьютекс
 
     std::cout << "entered thread " << std::this_thread::get_id() << std::endl;
     std::this_thread::sleep_for(std::chrono::seconds(rand()%10));
     std::cout << "leaving thread " << std::this_thread::get_id() << std::endl;
 
     g_lock.unlock(); // Работа завершена, освободим
}
 
int main()
{
     srand((unsigned int)time(0));
     std::thread t1(threadFunction);
     std::thread t2(threadFunction);
     std::thread t3(threadFunction);
     t1.join();
     t2.join();
     t3.join();
     return 0;
}
```

Программа должна выводить примерно следующее
```
entered thread 10144
leaving thread 10144
entered thread 4188
leaving thread 4188
entered thread 3424
leaving thread 3424
```

# Источники
- https://habr.com/ru/post/182610/
