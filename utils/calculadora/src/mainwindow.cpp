#include "mainwindow.hpp"
#include <cstdint>
#include <iostream>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent),
    ui(new Ui::Calculadora)
{
    ui->setupUi(this);
    setFixedSize(293, 294);

    //Area Botones
    connect(ui->uno,   &QPushButton::clicked, this, [this](){
        ui->display->insert("1");
    });
    connect(ui->dos,   &QPushButton::clicked, this, [this](){
        ui->display->insert("2");
    });
    connect(ui->tres,  &QPushButton::clicked, this, [this](){
        ui->display->insert("3");
    });
    connect(ui->cuatro,&QPushButton::clicked, this, [this](){
        ui->display->insert("4");
    });
    connect(ui->cinco, &QPushButton::clicked, this, [this](){
        ui->display->insert("5");
    });
    connect(ui->seis,  &QPushButton::clicked, this, [this](){
        ui->display->insert("6");
    });
    connect(ui->siete, &QPushButton::clicked, this, [this](){
        ui->display->insert("7");
    });
    connect(ui->ocho,  &QPushButton::clicked, this, [this](){
        ui->display->insert("8");
    });
    connect(ui->nueve, &QPushButton::clicked, this, [this](){
        ui->display->insert("9");
    });
    connect(ui->cero,  &QPushButton::clicked, this, [this](){
        ui->display->insert("0");
    });
    connect(ui->sum,   &QPushButton::clicked, this, [this](){
        onOperacion('+');
    });
    connect(ui->rest,  &QPushButton::clicked, this, [this](){
        onOperacion('-');
    });
    connect(ui->mult,  &QPushButton::clicked, this, [this](){
        onOperacion('*');
    });
    connect(ui->div,   &QPushButton::clicked, this, [this](){
        onOperacion('/');
    });
    connect(ui->del,   &QPushButton::clicked, this, [this](){
        ui->display->clear();
        this->valor_actual = 0;
        this->valor_previo = 0;
        this->operacion_pendiente = 0;
        this->esperando_segundo = false;
    });
    connect(ui->igual, &QPushButton::clicked, this, [this](){
        onIgual();
    });
    connect(ui->punto, &QPushButton::clicked, this, [this](){
        QString contenido = ui->display->text();
        
        if(!contenido.isEmpty() && !contenido.contains(".")){
            ui->display->insert(".");
        }
    });
}

MainWindow::~MainWindow(){delete ui;} // clear all ptrs

void MainWindow::onOperacion(char op) {
    bool ok = false;
    double num = ui->display->text().toDouble(&ok);
    if (!ok) {
        std::cerr << "Entrada inválida: no es un número\n";
        return;
    }

    if (esperando_segundo && operacion_pendiente != 0) {
        valor_actual = num;
        onIgual();
        num = ui->display->text().toDouble(&ok);
        if (!ok) {
            return;
        }
    }

    valor_previo = num;
    operacion_pendiente = op;
    esperando_segundo = true;
    ui->display->clear();
}

void MainWindow::onIgual() {
    if (!esperando_segundo || operacion_pendiente == 0) {
        return;
    }

    bool ok = false;
    double num = ui->display->text().toDouble(&ok);
    if (!ok) {
        std::cerr << "Entrada inválida: no es un número\n";
        return;
    }

    double res = 0;
    switch (operacion_pendiente) {
        case '+': res = valor_previo + num; break;
        case '-': res = valor_previo - num; break;
        case '*': res = valor_previo * num; break;
        case '/':
            if (num == 0) {
                std::cerr << "Error: División por cero.\n";
                res = 0;
            } else {
                res = valor_previo / num;
            }
            break;
        default:
            return;
    }

    ui->display->setText(QString::number(res));
    esperando_segundo = false;
    operacion_pendiente = 0;
}
