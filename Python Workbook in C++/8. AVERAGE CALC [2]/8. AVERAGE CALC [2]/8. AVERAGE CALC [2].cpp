// 8. AVERAGE CALC [2].cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>

using namespace std;

int main()
{
	string userRepeat;
	

	bool repeating = true;
	while (repeating){
		bool numberValid = false;
		int numbers[5] = { 0, 0, 0, 0, 0 };
		int counter = 0;
		int total = 0;
		float average = 0; 
		float weirdNumber = 0;

		while (counter < 5){
			bool numberValid = false;
			do
			{
				cout << "Please enter an integer: ";
				cin >> numbers[counter];

				if (cin.good()) {
					numberValid = true;
					counter += 1;
				}
				else {
					cout << "Enter a numerical value. " << endl;
					//something went wrong, we reset the buffer's state to good
					cin.clear();
					//and empty it
					cin.ignore(numeric_limits<streamsize>::max(), '\n');
				}
			} while (!numberValid);
		}

		for (int i = 0; i < 5; i++){
			total += numbers[i];
		}

		average = total / 5.0;
		cout << "The average is " << average << endl;

		weirdNumber = numbers[0] * numbers[1] - numbers[3];
		cout << "The sum of the first two numbers minus the third is " << weirdNumber << endl; 

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

