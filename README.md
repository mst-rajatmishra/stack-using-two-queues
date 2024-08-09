# stack-using-two-queues

### Find the First Non-Repeating Character in a String
 
**Problem Description**:
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.
 
**Objective**:
- Traverse the string to find the first character that does not repeat.
- Return the index of this character.
 
**Technique**:
- Use a hash map to store the frequency of each character.
- Traverse the string a second time to find the first character with a frequency of one.
