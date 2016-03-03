// 7. MULTIPLIER[2].cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <stdlib.h> 
#include <string>
#include <algorithm>

using namespace std;

int main()
{
	bool repeating = true;
	int variableOne, variableTwo;
	string dataRight, addOrMultiply, userRepeat;

	while (repeating){
		// Start of getting data
		bool gettingData = true;
		while (gettingData){
			bool oneValid = false;
			do
			{
				cout << "Please enter an integer: ";
				cin >> variableOne;

				if (cin.good()) {
					oneValid = true;
				}
				else {
					cout << "Enter a numerical value. " << endl;
					//something went wrong, we reset the buffer's state to good
					cin.clear();
					//and empty it
					cin.ignore(numeric_limits<streamsize>::max(), '\n');
				}
			} while (!oneValid);

			bool twoValid = false;
			do
			{
				cout << "Please enter an integer: ";
				cin >> variableTwo;

				if (cin.good()) {
					twoValid = true;
				}
				else {
					cout << "Enter a numerical value. " << endl;
					//something went wrong, we reset the buffer's state to good
					cin.clear();
					//and empty it
					cin.ignore(numeric_limits<streamsize>::max(), '\n');
				}
			} while (!twoValid);
						
			bool threeValid = false;
			do
			{
				cout << "Do you want to add or multiply?" << endl << "Enter A/M: ";
				cin >> addOrMultiply;

				if (addOrMultiply == "a" || addOrMultiply == "A"){
					addOrMultiply = "add";
					threeValid = true;
				}
				else if (addOrMultiply == "m" || addOrMultiply == "M"){
					addOrMultiply = "multiply";
					threeValid = true;
				}

			} while (!threeValid);

			cout << "You entered the following numbers: " << variableOne << ", " << variableOne << endl;
			cout << "You selected to " << addOrMultiply << endl;
			while (true){
				cout << "Is the above right?" << endl << "Enter Y/N: ";
				cin >> dataRight;

				if (dataRight == "y"){
					gettingData = false;
					break;
				}
				else if (dataRight == "n"){
					break;
				}
			}
		}
		// End of getting data

		// Start of adding or multiplying 
		if (addOrMultiply == "add"){
			cout << variableOne << " + " << variableTwo << " = " << variableOne + variableTwo << endl;
		}
		else if (addOrMultiply == "multiply"){
			cout << variableOne << " * " << variableTwo << " = " << variableOne * variableTwo << endl;
		}
		// End of adding or multiplying 

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

