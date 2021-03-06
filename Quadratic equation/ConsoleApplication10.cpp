#include "pch.h"
#include <iostream>
#include <string>

int test(double a, double b, double c)
{
	if ((b*b - 4 * a*c) >= 0)
	{
		return 1;
	}
}

int diskr(double a, double b, double c)
{
	double D = sqrt(b*b - 4 * a*c);
	return D;
}

double solution(double a, double b, double c, double D)
{
	if (a != 0)
	{
		double x1 = (-1 * b + D) / (2 * a);
		return x1;
	}
	else
	{
		if (b != 0)
		{
			double x1 = -c / b;
			return x1;
		}
		else
		{
			return 0;
		}
	}
}

void print(double a, double b, double c, double D)
{
	if (a != 0) 
	{
		std::cout << solution(a, b, c, D) << std::endl;
		std::cout << solution(a, b, c, -D) << std::endl;
	}
	else if (b != 0)
	{
		std::cout << solution(a, b, c, D) << std::endl;
	}
}

int main()
{
	double a;
	std::cin >> a;

	double b;
	std::cin >> b;

	double c;
	std::cin >> c;

	if (test(a, b, c))
	{
		print(a,b,c, diskr(a,b,c));
	}

	return 0;
}
