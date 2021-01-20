/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        
        ListNode *x=new  ListNode(0);
        ListNode *res=x;
        int car=0;
        while(1)
        {
            if(l1!=NULL&&l2!=NULL)
            {
                int ans=(l1->val+l2->val+car);
                x->val=ans%10;
                car=ans/10;
                l1=l1->next;
                l2=l2->next;
                   
            }
            else if(l1!=NULL)
            {
                 int ans=(l1->val+car);
                x->val=ans%10;
                car=ans/10;
                l1=l1->next;
        
            }
            else if(l2!=NULL)
            {
                int ans=(l2->val+car);
                x->val=ans%10;
                car=ans/10;
                l2=l2->next;
        
            }
            else if(car>0)
            {
                x->val=car;
                car=0;
                break;
            }
            
            
            if(l1==NULL&&l2==NULL&&car==0)break;
            
            
            x->next=new ListNode(0);
            x=x->next;
        }
        return  res; 
        
    }
};
