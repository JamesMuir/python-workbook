// 4. CANNIBAL PROGRAM[1].cpp : Defines the entry point for the console application.
//

#include <iostream> 
#include <stdlib.h> 
#include <string>



using namespace std;

int main()
{
	bool repeating = true;
	string userName, hairColour, eyeColour, userReapeat;
	string responses[3];
	int randomNumber;

	responses[0] = " eyes are very tasty in the cooking pot!";
	responses[1] = " eyes are very tasty over the fire!";
	responses[2] = " eyes smell horrible when set on fire!";

	while (repeating) {
		cout << "Please enter your name: ";
		cin >> userName;

		cout << "Please enter your hair colour: ";
		cin >> hairColour;

		cout << "Please enter your eye colour: ";
		cin >> eyeColour;

		randomNumber = rand() % 3;

		cout << "Hello, " << userName << " people with " << hairColour << " hair and " << eyeColour << responses[randomNumber] << endl;
		cout << endl;

		while (true) {
			cout << "Do you want to repeat? Enter Y/N: ";
			cin >> userReapeat;
			//Convers input to lowercase
			for (int i = 0; userReapeat[i]; i++) userReapeat[i] = tolower(userReapeat[i]);;

			if (userReapeat == "y") {
				break;
			}
			else if (userReapeat == "n") {
				repeating = false;
				break;
			}
			else {
				cout << "Enter valid input." << endl;
			}
		}
	}
    return 0;
}

