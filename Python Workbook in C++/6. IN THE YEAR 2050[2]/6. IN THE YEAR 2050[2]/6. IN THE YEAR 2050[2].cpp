// 6. IN THE YEAR 2050[2].cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <iostream>

using namespace std;

int main()
{
	bool repeating = true;
	string firstName, surname;
	int age;

	while (repeating) {
		bool gettingData = true;
		while (gettingData) {
			cout << "Please enter your first name: ";
			cin >> firstName;

			cout << "Please enter your surname: ";
			cin >> surname;
			while (true) {
				try {
					cout << "Please enter your age: ";
					cin >> age;
					break;
				}
				catch (...) {
					cout << "Enter a numerical value. " << endl;
				}
			}
		}
	}
    return 0;
}

