//http://practice.geeksforgeeks.org/problems/insert-in-a-sorted-list/1
/*structure of the node of the list is as
struct node
{
    int data;
    struct node* next;
};
*/
void sortedInsert(struct node** head_ref, int data)
{
    //cout<<"hello";
    std::string output ("");
    std::string dataString (std::to_string(data));
    if(head_ref == NULL){
        cout<<dataString + '\n';
        return;
        }
    bool placed = false;
    
    node* temp = new node;
    temp = *head_ref;
    while(temp){
        if(temp->data > data && !placed){
            output += dataString;
            output += " ";
            placed = true;
        }
        output += std::to_string(temp->data);
        
        if(temp->next){
            output += " ";
            temp = temp->next;
        }
        else{
            break;
        }
    }
    cout<<output;
    return;
    
}
