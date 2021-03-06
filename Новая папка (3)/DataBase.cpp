#include "pch.h"
#include <iostream>
#include <string>
#include <fstream>
#include <windows.h>
#include "DataBase.h"


class DataBase
{
private:
	int Id = 0;
	Patient patients[100];
	int PatientCount = 0;
	int Number = 0;


public:
	void AddPatient()
	{
		int Id = PatientCount;
		PatientCount++;

		std::cout << "Name" << std::endl;
		std::cin >> patients[Id].name;
		std::cout << "Surname" << std::endl;
		std::cin >> patients[Id].surname;
		std::cout << "Age" << std::endl;
		std::cin >> patients[Id].age;
		std::cout << "Sex" << std::endl;
		std::cin >> patients[Id].sex;
		std::cout << "City" << std::endl;
		std::cin >> patients[Id].city;
		std::cout << "VisitAmount" << std::endl;
		std::cin >> patients[Id].VisitAmount;
		std::cout << Id;
	}

	void GetInfo(int Id)
	{
		if (Id > PatientCount)
		{
			std::cout << "Patient not found" << std::endl;
		}
		else
		{
			std::cout << "Name: ";
			std::cout << patients[Id].name << std::endl;
			std::cout << "Surname: ";
			std::cout << patients[Id].surname << std::endl;
			std::cout << "Age: ";
			std::cout << patients[Id].age << std::endl;
			std::cout << "Sex: ";
			if (patients[Id].sex)
			{
				std::cout << "female" << std::endl;
			}
			else
			{
				std::cout << "male" << std::endl;
			}
			std::cout << "City: ";
			std::cout << patients[Id].city << std::endl;
			std::cout << "Visit Amount: ";
			std::cout << patients[Id].VisitAmount << std::endl;
		}
	}


	void LoadFrom(std::string filePath)
	{
		DataBase db;
		std::ifstream fin;
		fin.open(filePath);
		if (fin.is_open())
		{
			int amount = 0;
			fin >> amount;
			Number = amount;

			while (amount != 0)
			{
				int Id = PatientCount;
				PatientCount++;

				fin >> patients[Id].name;
				fin >> patients[Id].surname;
				fin >> patients[Id].age;
				fin >> patients[Id].sex;
				fin >> patients[Id].city;
				fin >> patients[Id].VisitAmount;

				amount -= 1;
			}

			fin.close();

		}
		else
		{
			std::cout << "File not found" << std::endl;
		}

	}

	void SaveTo(std::string filePath)
	{
		DataBase db;
		std::ofstream fout;
		fout.open(filePath, std::ofstream::app);
		if (fout.is_open())
		{
			int Id = PatientCount;
			PatientCount++;

			SetConsoleCP(1251);

			std::cout << "Name" << std::endl;
			std::cin >> patients[Id].name;
			fout << std::endl << patients[Id].name << " ";
			std::cout << "Surame" << std::endl;
			std::cin >> patients[Id].surname;
			fout << patients[Id].surname << " ";
			std::cout << "Age" << std::endl;
			std::cin >> patients[Id].age;
			fout << patients[Id].age << " ";
			std::cout << "Sex" << std::endl;
			std::cin >> patients[Id].sex;
			fout << patients[Id].sex << " ";
			std::cout << "City" << std::endl;
			std::cin >> patients[Id].city;
			fout << patients[Id].city << " ";
			std::cout << "VisitAmount" << std::endl;
			std::cin >> patients[Id].VisitAmount;
			fout << patients[Id].VisitAmount;

			Number++;
			SetConsoleCP(866);
			fout.close();
		}
		else
		{
			std::cout << "File not found" << std::endl;
		}

	}

	void CloseDoc(std::string filePath)
	{
		std::ofstream fout;
		fout.open(filePath, std::ofstream::app);
		if (fout.is_open())
		{
			fout << std::endl;
			fout << Number << " ";
			fout.close();
		}
		else
		{
			std::cout << "File not found" << std::endl;
		}
	}

};