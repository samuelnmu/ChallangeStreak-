import 'dart:io';

void main() {
  print("Enter first Number: ");
  String? input1 = stdin.readLineSync();

  // Error handling for invalid input
  double num1;
  while (true) {
    try {
      num1 = double.parse(input1!);
      break;
    } catch (e) {
      print("Invalid input. Please enter a number.");
      input1 = stdin.readLineSync();
    }
  }

  print("Enter second Number: ");
  String? input2 = stdin.readLineSync();

  // Error handling for invalid input
  double num2;
  while (true) {
    try {
      num2 = double.parse(input2!);
      break;
    } catch (e) {
      print("Invalid input. Please enter a number.");
      input2 = stdin.readLineSync();
    }
  }

  print(num1 - num2);
}