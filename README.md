# Easy test file creation for QiangdaoU's OnlineJudge

Creates a zip archive with the .in .out tests files for [this judge](https://github.com/QingdaoU/OnlineJudge).

# Usage:

`python makeFiles.py [-h] [-o <outputFile>] [-s] <inputFile>`

 | Optional arguments: | Description:           |
 |---------------------|-----------------------:|
 | -h, --help          | show this help message |
 | -o, --fileout       | output file            |
 | -s, --show          | show test cases        |


Input file should be in `.txt` format and be formatted as following: 

```
test1
::
result1

test2
::
result2
```

# Example output

Command:

`python makeFiles.py --show -o testsarchive inputfile.txt`

Output: 

```
Test 0: 0 2      2 0      0 0      ::       2        
Test 1: 1 3      -3 5     3 1      ::       2        
Test 2: 3 3      -3 3     3 3      ::       0        
Test 3: -2 3     -3 -1    3 -2     ::       12.5     
Test 4: 6 8      7 9      5 8      ::       0.5      
Test 5: -6 -8    -7 -9    -5 -8    ::       0.5      
Test 6: 65 52    34 12    95 34    ::       879      
Test 7: 15 84    15 -84   0 0      ::       1260     
Test 8: 99 99    99 -99   -99 -99  ::       19602    
Test 9: 0 0      0 0      0 0      ::       0                 
Total number of tests: 10
Finished building testsarchive.zip
```

