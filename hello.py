import sys
  
if len(sys.argv) < 2:
	print('hello world')
else:
	input = sys.argv[1]
	print("hello " + input)
