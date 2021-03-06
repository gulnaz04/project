#include "pch.h"
#include <iostream>
#include <string>
#include <fstream>
#include <windows.h>
#include "DataBase.h"

void AddPatient()
{
	Patient* patient = new Patient;
	patient->Id = PatientCount++;
	std::cout << "Name" << std::endl;
	std::cin >> patient->name;
	std::cout << "Surname" << std::endl;
	std::cin >> patient->surname;
	std::cout << "Age" << std::endl;
	std::cin >> patient->age;
	std::cout << "Sex" << std::endl;
	std::cin >> patient->sex;
	std::cout << "City" << std::endl;
	std::cin >> patient->city;
	std::cout << "VisitAmount" << std::endl;
	std::cin >> patient->VisitAmount;
	std::cout << Id;
	patients.push_back(patient);
}


void GetInfo(int Id)
{
	Patient* patient;
	if (Id > PatientCount)
	{
		std::cout << "Patient not found" << std::endl;
	}
	else
	{
		patients.operator[];
		std::cout << "Name: ";
		std::cout << patient->name << std::endl;
		std::cout << "Surname: ";
		std::cout << patient->surname << std::endl;
		std::cout << "Age: ";
		std::cout << patient->age << std::endl;
		std::cout << "Sex: ";
		if (patient->sex)
		{
			std::cout << "female" << std::endl;
		}
		else
		{
			std::cout << "male" << std::endl;
		}
		std::cout << "City: ";
		std::cout << patient->city << std::endl;
		std::cout << "Visit Amount: ";
		std::cout << patient->VisitAmount << std::endl;
	}
}


void LoadFrom(std::string filePath)
{
	DataBase db;
	Patient* patient;
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

			fin >> patient->name;
			fin >> patient->surname;
			fin >> patient->age;
			fin >> patient->sex;
			fin >> patient->city;
			fin >> patient->VisitAmount;

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
	Patient* patient = new Patient;
	patient->Id = PatientCount++;
	std::ofstream fout;
	fout.open(filePath, std::ofstream::app);
	if (fout.is_open())
	{
		SetConsoleCP(1251);
		std::cout << "Name" << std::endl;
		std::cin >> patient->name;
		fout << std::endl << patient->name << " ";
		std::cout << "Surame" << std::endl;
		std::cin >> patient->surname;
		fout << patient->surname << " ";
		std::cout << "Age" << std::endl;
		std::cin >> patient->age;
		fout << patient->age << " ";
		std::cout << "Sex" << std::endl;
		std::cin >> patient->sex;
		fout << patient->sex << " ";
		std::cout << "City" << std::endl;
		std::cin >> patient->city;
		fout << patient->city << " ";
		std::cout << "VisitAmount" << std::endl;
		std::cin >> patient->VisitAmount;
		fout << patient->VisitAmount;
		patients.push_back(patient);

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
};
