The user will specify Test Suites:


An abstract test consists of 
- Test Name
- Constraint 
- Property
- (List of InputIDs)

A concrete test consists
- Test Name
- Abstract Test
- Input ID


--------------------------------
The program should verify an input satisfies the constraint when adding the input to the test suite


If an input is invalid, an error should be generated
->
[FE] If an error is generated, it should be displayed to the user


The program should read in a Test Suite:



The program should allow modifying a Test Suite
- Add an Abstract Test
- Add an InputID to an Abstract Test
- Add a set of InputID to an ABstractTest
- Add an InputID to a set of Abstract Tests


The program should return the current Test Suite


The user wants to display the loaded Test Suite

The user wants to modify the existing Test Suite

The user wants to validate the existing Test Suite