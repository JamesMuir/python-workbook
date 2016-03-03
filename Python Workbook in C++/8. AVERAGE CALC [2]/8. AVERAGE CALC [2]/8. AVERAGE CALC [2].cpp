// 8. AVERAGE CALC [2].cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>

using namespace std;

int main()
{
	bool repeating = true;
	while (repeating){
		bool numberValid = false;
		int numbers[5] = { 0, 0, 0, 0, 0 };
		int counter = 0;
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
			cout << numbers[i] << endl;
		}
	}

	return 0;
}

