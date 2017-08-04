//http://practice.geeksforgeeks.org/problems/insert-in-a-sorted-list/1


/*
structure of the node of the list is as
struct node
{
    int data;
    struct node* next;
};
*/
void sortedInsert(struct node** head_ref, int data)
{
    node* dataNode = new node();
    dataNode->data = data;
    if(head_ref == NULL){
        head_ref = &dataNode;
        return;
        }
    node* head = *head_ref;
    if(head->data > data){
        dataNode->next = head;
        *head_ref = dataNode;
        return;
    }
    
    node* temp = new node;
    temp = *head_ref;
    while(temp->next){
        if(temp->next->data > data){
            dataNode->next = temp->next;
            temp->next = dataNode;
            return;
        }
        temp = temp->next;
    }
    
    temp->next = dataNode;
    return;
    
}
