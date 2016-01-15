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
	string dataRight;

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
						
			cout << "You entered the following numbers: " << variableOne << ", " << variableOne << endl;
			while (true){
				cout << "Is the above right?" << endl << "Enter Y/N";
				cin >> dataRight;

				if (dataRight == "y"){
					gettingData = false;
					break;
				}
				else if (dataRight == "n"){
					break;
				}
				else {
					cout << "Enter Y/N" << endl;
				}
			}
		}
		// End of getting data

		// Start of multiplying 

		// End of multiplying 
	}

	return 0;
}

