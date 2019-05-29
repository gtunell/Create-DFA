# Create-DFA
This program takes command line arguments as input and uses them to demonstrate behavior of a DFA classifier.

**Inputs**

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

**Outputs** 

1. On one line this program prints the initial segment of the sequence 
of weights, and the next line is the repeated segment of weights. These 
weights will classify the states of the DFA classifier.

2. Next we output a table representing the DFA classifier that, 
given a number y in base b, read right to left, is in a state k 
where y ≡ k (mod m). Each state of the DFA classifier is be represented 
by a pair (j, k), where j is the weight index of the state (0 ≤ j < w) 
and k is the classifier value at the state (0 ≤ k < m). Additionally, 
for a given state, the transition function at that state is represented
as a list of length b, where the α-th element of the list (0 ≤ α < b) 
identifies the new state that is reached upon transitioning on digit α.

3. Next the program outputs the sequence of states that
would be encountered, from first to last, upon inputting the sequence
of base-b digits x into the DFA classifier above. This sequence of states
is displayed on a single line in list form, following the formatting
rules used in the previous two parts. By convention, the initial state
(0, 0) is included the list.
On a new line, it outputs “accept” if and only if x ≡ i (mod m), 
otherwise it output “reject”. (Here, x denotes the number given by the
sequence of base-b digits supplied as arguments to x. Keep in mind that
the digits of x will be given in right to left order.)

**Example**

$>program 6 8 0 4 5 2
[1, 6, 4]
[0]
(0, 0) [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5)]
(0, 1) [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6)]
(0, 2) [(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7)]
(0, 3) [(1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 0)]
(0, 4) [(1, 4), (1, 5), (1, 6), (1, 7), (1, 0), (1, 1)]
(0, 5) [(1, 5), (1, 6), (1, 7), (1, 0), (1, 1), (1, 2)]
(0, 6) [(1, 6), (1, 7), (1, 0), (1, 1), (1, 2), (1, 3)]
(0, 7) [(1, 7), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4)]
(1, 0) [(2, 0), (2, 6), (2, 4), (2, 2), (2, 0), (2, 6)]
(1, 1) [(2, 1), (2, 7), (2, 5), (2, 3), (2, 1), (2, 7)]
(1, 2) [(2, 2), (2, 0), (2, 6), (2, 4), (2, 2), (2, 0)]
(1, 3) [(2, 3), (2, 1), (2, 7), (2, 5), (2, 3), (2, 1)]
(1, 4) [(2, 4), (2, 2), (2, 0), (2, 6), (2, 4), (2, 2)]
(1, 5) [(2, 5), (2, 3), (2, 1), (2, 7), (2, 5), (2, 3)]
(1, 6) [(2, 6), (2, 4), (2, 2), (2, 0), (2, 6), (2, 4)]
(1, 7) [(2, 7), (2, 5), (2, 3), (2, 1), (2, 7), (2, 5)]
(2, 0) [(3, 0), (3, 4), (3, 0), (3, 4), (3, 0), (3, 4)]
(2, 1) [(3, 1), (3, 5), (3, 1), (3, 5), (3, 1), (3, 5)]
(2, 2) [(3, 2), (3, 6), (3, 2), (3, 6), (3, 2), (3, 6)]
(2, 3) [(3, 3), (3, 7), (3, 3), (3, 7), (3, 3), (3, 7)]
(2, 4) [(3, 4), (3, 0), (3, 4), (3, 0), (3, 4), (3, 0)]
(2, 5) [(3, 5), (3, 1), (3, 5), (3, 1), (3, 5), (3, 1)]
(2, 6) [(3, 6), (3, 2), (3, 6), (3, 2), (3, 6), (3, 2)]
(2, 7) [(3, 7), (3, 3), (3, 7), (3, 3), (3, 7), (3, 3)]
(3, 0) [(3, 0), (3, 0), (3, 0), (3, 0), (3, 0), (3, 0)]
(3, 1) [(3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1)]
(3, 2) [(3, 2), (3, 2), (3, 2), (3, 2), (3, 2), (3, 2)]
(3, 3) [(3, 3), (3, 3), (3, 3), (3, 3), (3, 3), (3, 3)]
(3, 4) [(3, 4), (3, 4), (3, 4), (3, 4), (3, 4), (3, 4)]
(3, 5) [(3, 5), (3, 5), (3, 5), (3, 5), (3, 5), (3, 5)]
(3, 6) [(3, 6), (3, 6), (3, 6), (3, 6), (3, 6), (3, 6)]
(3, 7) [(3, 7), (3, 7), (3, 7), (3, 7), (3, 7), (3, 7)]
32
4
[(0, 0), (1, 4), (2, 2), (3, 2)]
reject
