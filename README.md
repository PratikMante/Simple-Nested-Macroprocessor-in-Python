# Simple-Nested-Macroprocessor-in-Python
This is a code for simple nested macroprocessor written in Python

## Algorithm

1. Open input file in read and create mnt, fppt and mdt
2. Declare lists
3. if MACRO in words > count ‘&’ in words > write(words1[0]+count+line no.) in mnt
4. write(words[1]+words[-count]+x) > name=words[1] > append(words[-count]),words[1],x > count- - > x++
5. count != 0 > goto 4
6. line ++
7. if words[-1] in fp > y= fp.index(words[-1]) > write(mname[y]+words[0]+pp[y]) 
8. else > write(name+words[0]+words[-1])
9. line++ > y=0
10. if MEND ! in words > goto 7
11. write(words[0])
12. x=1 > close all files
13. open all files in read > create papt
14. i in range(lines)
15. if words[0] == words1[0] > x=words1[-2] > y=1
16. write(words[0]+y+words[-x]) > y++ > x - -
17. if x!=0 > goto 16
18. if j != lines1 > goto 15
19. if i != lines > goto 14
20. close all files
21. Open all files in read > create expanded code 
22. if MACRO in words 
23. for (line in f) > if MEND in words : break > else : continue
24. else > if words[0] in operation : write(line)
25. else:
26. j++ > if words1[0]==words[0]
27. line2=lines2[k]
28. if words[0]==words2[0] & words1[-1]==words2[-2]: write(words[1]+words2[-1]) ,flag=0, break
29. else flag=1
30. k++ > if k!= lines2 : goto 27
31. if flag==1: write(words1[1]+words1[-1]), flag=0
32. if j!= lines1 : goto 26
33. if ! EOF : goto 22
34. Close all files
