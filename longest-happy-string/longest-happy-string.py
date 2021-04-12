class Solution(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        r = ''
        d = {'a':a, 'b':b, 'c':c}
        sign = [-1, 1]
        for i in range(a+b+c):
           
		    # exclude the last character 
            cmp_key = lambda x: d[x]* sign[x!=r[i-1]]
               
            # if r is good
            if i<2 or r[i-1]!=r[i-2]:
                cmp_key = d.get
              
            c = max(d, key=cmp_key)
            if d[c] == 0:
                break
            r += c
            d[c] -=1
                
            
        return r