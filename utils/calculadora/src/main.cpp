#include "calculadora.hpp"

int main() {
    uint32_t n1 = 9.5;
    uint32_t n2 = 2.0;

    // Instanciación correcta en el stack
    Calculadora operar(n1, n2, Calculadora::DIV);

    return 0;
}