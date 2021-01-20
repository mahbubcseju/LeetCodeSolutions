        {   
            store[row]++;
            
            if(row==1)flag=0;
            else if(row==numRows)flag=1;
            if(flag==0)
            {
                row++;
            }
            else {
                row--;
                col++;
            }
       
        }
        for(int i=1;i<=numRows;i++)store[i]+=store[i-1];
        
      flag =0;
       row=1,col=1;
       int  store1[numRows+2];
        for(int i=0;i<=numRows;i++)store1[i]=0;
        string ans=s;
        for(int i=0;i<s.size();i++)
        {   
            int ind=store[row-1];
            store1[row]++;
            ind+=store1[row];
            ans[ind-1]=s[i];
            
            if(row==1)flag=0;
            else if(row==numRows)flag=1;
            if(flag==0)
            {
                row++;
            }
            else {
                row--;
                col++;
            }
       
        }
        return ans;
        
        
    }
};
