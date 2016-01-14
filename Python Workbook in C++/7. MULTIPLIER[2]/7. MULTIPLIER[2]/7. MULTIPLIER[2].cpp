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
		bool gettingData = true;
		while (gettingData){
			try {
				cout << "Please enter an integer: ";
				cin >> variableOne;

				cout << "Please enter an integer: ";
				cin >> variableTwo;
			}
			catch (...){
				cout << "Enter a numerical value." << endl;
			}
			cout << "You entered the following numbers: " << variableOne << ", " << variableOne << endl;
			while (true){
				cout << "Is the above right?" << endl << "Enter Y/N";
				cin >> dataRight;

				dataRight = 

				if (dataRight == "y"){
					gettingData = false;
				}
				else if (dataRight == "n"){
					
				}
				else {
					cout << "Enter Y/N" << endl;
				}
			}
		}

	}

	return 0;
}

