/*http://practice.geeksforgeeks.org/problems/sort-a-linked-list/1*/


/* Structure of the linked list node is as
struct node
{
    int data;
    struct node* next;
};
*/
/* split the nodes of the given list into front and back halves,
     and return the two lists using the reference parameters.*/
void splitList(struct node* source, struct node** frontRef, struct node** backRef)
{
    
    source = source->next;
    
    node* current = source;
    node* halfway = source;
    bool half = false;

    while(current->next){

        if(half){
            halfway = halfway->next;
        }
        current = current->next;
        half = half;
    }
    
    node* nextBoy = halfway->next;
    halfway->next = NULL;
    backRef = &nextBoy;
    frontRef = &source;
    return;

}
// merges two sorted list into one big list
struct node* mergeList(struct node* a, struct node* b)
{
    node* comboList = new node();
    node* curr = comboList;
    if(a && b){
        if(a->data > b->data){
            curr->next = a;
            a = a->next;
        }else{
            curr->next = b;
            b = b->next;
        }
        curr = curr->next;
    }else if(a){
        curr->next = a;
    }else if(b){
        curr->next = b;
    }
    return comboList->next;

}