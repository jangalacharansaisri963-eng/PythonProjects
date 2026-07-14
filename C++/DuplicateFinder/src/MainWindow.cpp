#include "MainWindow.h"

#include <QPushButton>
#include <QLineEdit>
#include <QListWidget>
#include <QLabel>
#include <QFileDialog>
#include <QVBoxLayout>
#include <QHBoxLayout>
#include <QWidget>


MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
{

    setWindowTitle("Duplicate Finder");

    resize(600, 400);


    QWidget *central = new QWidget(this);

    setCentralWidget(central);


    QVBoxLayout *mainLayout = new QVBoxLayout();


    QHBoxLayout *folderLayout = new QHBoxLayout();


    folderPath = new QLineEdit();

    browseButton = new QPushButton("Browse");


    folderLayout->addWidget(folderPath);

    folderLayout->addWidget(browseButton);



    scanButton = new QPushButton("Scan");


    results = new QListWidget();


    status = new QLabel("Ready.");



    mainLayout->addLayout(folderLayout);

    mainLayout->addWidget(scanButton);

    mainLayout->addWidget(results);

    mainLayout->addWidget(status);



    central->setLayout(mainLayout);



    connect(
        browseButton,
        &QPushButton::clicked,
        this,
        &MainWindow::selectFolder
    );


    connect(
        scanButton,
        &QPushButton::clicked,
        this,
        &MainWindow::scanFiles
    );

}



void MainWindow::selectFolder()
{

    QString folder = QFileDialog::getExistingDirectory(
        this,
        "Select Folder"
    );


    if(!folder.isEmpty())
    {
        folderPath->setText(folder);
    }

}



void MainWindow::scanFiles()
{

    results->clear();


    QString folder = folderPath->text();


    if(folder.isEmpty())
    {
        status->setText("Select a folder first.");

        return;
    }


    results->addItem(
        "Scanning: " + folder
    );


    status->setText(
        "Scanner will be added next."
    );

}
