// 6. IN THE YEAR 2050[2].cpp : Defines the entry point for the console application.
//



#include "stdafx.h"
#include <string>
#include <iostream>
#include <ctime>

using namespace std;

int main()
{
	bool repeating = true;
	string firstName, surname, userRepeat;
	int age;

	time_t now = time(0);
	#pragma warning(disable: 4996)
	tm *ltm = localtime(&now);

	while (repeating) {
		bool gettingData = true;
		//Gets the user's name and age
		while (gettingData) {
			cout << "Please enter your first name: ";
			cin >> firstName;

			cout << "Please enter your surname: ";
			cin >> surname;
			bool valid = false;
			do
			{
				cout << "Please enter your age: ";
				cin >> age;
				if (cin.good()) {
					valid = true;
				}
				else {
					cout << "Enter a numerical value. " << endl;
					//something went wrong, we reset the buffer's state to good
					cin.clear();
					//and empty it
					cin.ignore(numeric_limits<streamsize>::max(), '\n');
				}
			} while (!valid);

			while (true) {
				string informationCheck;
				cout << endl << "Your name is " << firstName << " " << surname << " and your age is " << age << "." << endl << "Is this information correct?" << endl << "Enter Y/N: ";
				cin >> informationCheck;
				if (informationCheck == "y" || informationCheck == "Y") {
					gettingData = false;
					break;
				}
				else if (informationCheck == "n" || informationCheck == "N") {
					break;
				}
			}
		}

		// Works out the age 
		int currentYear = ltm->tm_year + 1900;
		int ageIn2050 = 2050 - currentYear + age;

		// Prints age
		cout << "You are in 2050 will be : " << ageIn2050 << "." << endl;

		// Allows the user to quit
		while (true) {
			cout << "Do you want to repeat." << endl << "Enter Y/N: ";
			cin >> userRepeat;

			if ((userRepeat == "y") || (userRepeat == "Y")) {
				break;
			}
			else if ((userRepeat == "n") || (userRepeat == "y")) {
				repeating = false;
				break;
			}
			else {
				cout << "Enter a valid input." << endl << endl;
			}
		}
	}
	return 0;
}

