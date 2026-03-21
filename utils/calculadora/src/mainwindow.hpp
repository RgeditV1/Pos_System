#pragma once
#include <QMainWindow>
#include <QString>
#include <cstdint>
#include "./gui/ui_mainwindow.hpp"


class MainWindow : public QMainWindow
{
    Q_OBJECT

private:
    Ui::Calculadora* ui;
    double valor_actual = 0;
    double valor_previo = 0;
    char operacion_pendiente = 0;
    bool esperando_segundo = false;

public:
    explicit MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

    void onOperacion(char op);
    void onIgual();
};
