#include "pch.h"
#include <iostream>
#include <string>
#include <fstream>
#include <windows.h>
#include "Patient.h"

class DataBase
{
private:
	int Id = 0;
	Patient patients[100];
	int PatientCount = 0;
	int Number = 0;


public:
	void AddPatient();
	void GetInfo(int Id);
	void LoadFrom(std::string filePath);
	void SaveTo(std::string filePath);
	void CloseDoc(std::string filePath);

};