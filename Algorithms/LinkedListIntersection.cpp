/*http://practice.geeksforgeeks.org/problems/intersection-of-two-linked-list/1*/


/*
structure of the node is as
struct node
{
    int data;
    struct node* next;
};
*/
struct node* findIntersection(struct node* head1, struct node* head2)
{
    std::multimap<int,bool> mymap;
    
    node* curr = head1;
    while(curr){
        mymap.insert(pair<int,bool>(curr->data,false));
        curr = curr->next;
    }
    curr = head2;
    while(curr){
        if(mymap.count(curr->data) > 0){
            pair<multimap<int,bool>::iterator,multimap<int,bool>::iterator> it;
            it = mymap.equal_range(curr->data);
            for (multimap<int, bool>::iterator it2 = it.first; it2 != it.second;++it2){
                if(!it2->second){
                    it2->second = true;
                    break;
                }
                
            }
        }
        curr = curr->next;
    }
    node* head3;
    multimap<int,bool>::iterator itr;
    bool headed = false;
    curr = head3;
    for(itr = mymap.begin(); itr != mymap.end(); itr++)
    {  
       if(itr->second == true){
            node* newNode = new node();
            newNode->data = itr->first;
            if(!headed){
                head3 = newNode;
                headed = true;
            }
            if(curr){
                curr->next = newNode;
            }
           
           curr = newNode;
            }
    }
    
    return head3;
    
}
