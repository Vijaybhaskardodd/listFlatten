### Problem Description:

Given a nested list of integers, implement a function to flatten it. Each element is either an integer, or a list -- whose elements may also be integers or other lists. Provide a github gist link to your code and tests,. You may use whatever language you are comfortable with but do not use any built-in flattening functions that provide this functionality like Ruby’s Array.flatten.

### Summary

The src folder consist ListFlatten.py file contain flatten function which takes one input parameter. flatten function converts the hierarchical to one dimension list.  
Unit tests for this flatten function were written in ListFlattenTest.py.

### Usage
* To run ListFlatten.py file

        
        python ListFlatten.py		
        

* To run ListFlattenTest.py file

        
        python ListFlattenTest.py
        
### Technologies

* In Python 2, reduce() was a built-in function. However, in Python 3, it is moved to functools  module. Therefore to use it, you have to first import it as follows:

	from functools import reduce # only in Python 3