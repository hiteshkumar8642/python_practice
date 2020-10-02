t=int(input())
if(t>0 and t<500):
	for l in range(0,t):
	    n=int(input())
	    if(n>1 and n<=2000):
		    k=int(input())
		    if(k>=2 and k>=10000):
			    #print("enter the element in list")
			    a=[]
			    for i in range(0, n):
			      ele = int(input())
			      if(ele>=1 and ele<=k):
			          break
			      a.append(ele) # adding the element
			    b=min(a)
			    a.pop(a.index(min(a)))
        		    count=0
	        	    while(min(a)<=k):
		                a = [x + b for x in a]
		                if(max(a)<k):
		                    count=count+2
		                else:
		                    count=count+1
		            print(count)

