#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int x;
    struct node *next;
    struct node *prev;
}node;

void dalloc(node **tail, node **head)
{
    if(tail == NULL)
    {
        return;
    }
    node *curr = *tail;
    while (curr->next != NULL)
    {
        curr = curr->next;
        free(curr->prev);
    }
    free(curr);
    tail = NULL;
    head = NULL;
}

void add_at_the_beginning(node **tail, int value)
{
    node *newnode = malloc(sizeof(node));

    newnode->x = value;
    newnode->prev = NULL;
    newnode->next = *tail;
    if(*tail != NULL)
    {
        (*tail)->prev = newnode;
    }
    *tail = newnode;
}
void add_at_the_end(node **head, int value)
{

}

int main(void)
{
    node *tail = NULL;
    node *head = NULL;

    add_at_the_beginning(&tail, 9);
    add_at_the_beginning(&tail, 8);
    add_at_the_beginning(&tail, 7);
    add_at_the_beginning(&tail, 6);
    add_at_the_beginning(&tail, 5);
    node *curr = head;
    while (curr != NULL)
    {
        printf("the number is: %d\n", curr->x);
        curr = curr->prev;
    }
    dalloc(&tail, &head);
}
