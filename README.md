# Create-DFA
This program takes command line arguments as input and uses them to demonstrate behavior of a DFA classifier.

The parameters corresponding to these arguments are specified below.

1. b - a base-10 number given by the 1st argument. This represents the
base of the numerical input that your DFA classifier will receive.

2. m - a base-10 number given by the 2nd argument. This represents the
modulo value corresponding to your DFA classifier.

3. i - a base-10 number given by the 3rd argument. See part 3 of the
output for details.

4. x - a sequence of base-10 numbers given by the remaining supplied
arguments. Each number k in this sequence represents a base-b digit
(so 0 ≤ k < b). x will represent the sequence of base-b digits that will
be supplied in right to left order to your DFA classifier. NOTE: There
may be multiple arguments corresponding to this parameter.

There are three outputs associated with a given input. 

Part 1 - On one line this program prints the initial segment of the sequence 
of weights, and the next line is the repeated segment of weights. These 
weights will classify the states of the DFA classifier.

Part 2 - For this we output a table representing the DFA classifier that, 
given a number y in base b, read right to left, is in a state k 
where y ≡ k (mod m). Each state of the DFA classifier is be represented 
by a pair (j, k), where j is the weight index of the state (0 ≤ j < w) 
and k is the classifier value at the state (0 ≤ k < m). Additionally, 
for a given state, the transition function at that state is represented
as a list of length b, where the α-th element of the list (0 ≤ α < b) 
identifies the new state that is reached upon transitioning on digit α.

Part 3 - Next the program outputs the sequence of states that
would be encountered, from first to last, upon inputting the sequence
of base-b digits x into the DFA classifier above. This sequence of states
is displayed on a single line in list form, following the formatting
rules used in the previous two parts. By convention, the initial state
(0, 0) is included the list.
