#include "pch.h"
#include <iostream>
#include <string>
#include <fstream>
#include <windows.h>
#include "DataBase.cpp"


int main()
{
	setlocale(LC_ALL, "rus");
	int PatientCount = 0;
	DataBase db;
	db.LoadFrom("C:\\Users\\DNS\\source\\repos\\Data base.cpp\\Base.txt");

	for (;;)
	{
		int choice = 0;
		std::cout << "To add a patient to the database enter: 1" << std::endl;
		std::cout << "For information about the patient enter: 2" << std::endl;
		std::cout << "To close the program enter: 3" << std::endl;

		std::cin >> choice;
		int k = 0;

		switch (choice)
		{
		case 1:
			db.SaveTo("C:\\Users\\DNS\\source\\repos\\Data base.cpp\\Base.txt");
			break;

		case 2:
			std::cout << "Enter the patient Id about which you want to get information" << std::endl;
			std::cin >> k;
			db.GetInfo(k);
			break;

		case 3:
			db.CloseDoc("C:\\Users\\DNS\\source\\repos\\Data base.cpp\\Base.txt");
			return 0;

		default:
			std::cout << "This operation is not possible" << std::endl;
			break;

		}

	}

	return 0;
}