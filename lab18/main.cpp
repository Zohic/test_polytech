// Напишите программу, используя технику TDD. Реализуйте калькулятор,
// поддерживающий операции: +, -, *, /. Проверьте тестами свойства операций
// и законы элементарной алгебры.

#include <cassert>

enum Command
{
    Add,Sub,Mul,Div
};

double calc(Command operation, double x, double y) {
    switch (operation)
    {
        case Command::Add:
            return x+y;
            break;
        case Command::Sub:
            return x-y;
            break;
        case Command::Mul:
            return x*y;
            break;
        case Command::Div:
            return x/y;
            break;
        default:
            return 0;
            break;

    }
}

int main() {
    assert(calc(Command::Add, 1.2, 4.1) == 5.3);
    assert(calc(Command::Sub, 2.2, 6.2) == -4.0);
    assert(calc(Command::Mul, 1.5, 2.0) == 3.0);
    assert(calc(Command::Div, 10.25, 2.0) == 5.125);

    double a=2, b=3, c=11;

    // Коммутативность сложения
    assert(calc(Command::Add, a, b) == calc(Command::Add, b, a));
    // Коммутативность умножения
    assert(calc(Command::Mul, a, b) == calc(Command::Mul, b, a));

    // Ассоциативность сложения
    assert(calc(Command::Add, calc(Command::Add, a, b), c) == calc(Command::Add, calc(Command::Add, a, c), b));
    // Ассоциативность умножения
    assert(calc(Command::Mul, calc(Command::Mul, a, b), c) == calc(Command::Mul, calc(Command::Mul, a, c), b));

    // закон распределения
    assert(calc(Command::Mul, a, calc(Command::Add, b, c))
                                ==
           calc(Command::Add, calc(Command::Mul, a, b), calc(Command::Mul, a, c)));

    return 0;
}
