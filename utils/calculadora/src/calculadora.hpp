#pragma once

class Calculadora{
private:
    int valor_actual;
    int valor_previo;
    /*
    * Guardara el caracter de la operacion
    * e.g(+,-,*,/)
    */
    char operacion;

public:
    int sum(int& num, int& num2);
    int rest(int& num, int& num2);
    int mult(int& num, int& num2);
    float div(int& num, int& num2);

    float resultado();
    void limpiar(); // setea los valores a 0
};