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

int main(void)
{
    node *tail = malloc(sizeof(struct node));
    tail->x = 1;
    tail->prev = NULL;
    tail->next = malloc(sizeof(struct node));
    tail->next->x = 2;
    tail->next->prev = tail;
    tail->next->next = malloc(sizeof(struct node));
    tail->next->next->x = 3;
    tail->next->next->next = NULL;
    tail->next->next->prev = tail->next;
    node *head = tail->next->next;
    node *curr = head;
    while (curr != NULL)
    {
        printf("the number is: %d\n", curr->x);
        curr = curr->prev;
    }
    dalloc(&tail, &head);
}
