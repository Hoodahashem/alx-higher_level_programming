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
    node *newnode = malloc(sizeof(node));
    newnode->x = value;
    newnode->next = NULL;
    newnode->prev = *head;

    if (*head != NULL)
    {
        (*head)->next = newnode;
    }
    *head = newnode;
}

void init(node **head, node **tail, int value)
{
    node *newnode = malloc(sizeof(node));
    newnode->next = NULL;
    newnode->prev = NULL;
    newnode->x = value;

    *tail = newnode;
    *head = newnode;
}

void add_after(node *btngan, int value)
{
    node *newnode = malloc(sizeof(node));
    newnode->x = value;
    newnode->next = btngan->next;
    newnode->prev = btngan;
    if (btngan->next != NULL)
    {
        btngan->next->prev = newnode;
    }
    btngan->next = newnode;
}

void remove_node(node *btngan)
{
    if (btngan->prev != NULL)
    {
        btngan->prev->next = btngan->next;
    }
    if (btngan->next != NULL)
    {
        btngan->next->prev = btngan->prev;
    }
    free(btngan);
}

node *find_node(node *btngan, int value)
{
    node *curr = btngan;
    while(btngan != NULL)
    {
        if (curr->x = value)
        {
            return curr;
        }
        curr = curr->next;
    }
    return NULL;
}

int main(void)
{
    node *tail = NULL;
    node *head = NULL;

    init(&head, &tail, 3);
    add_at_the_end(&head, 5);
    add_after(head->prev, 4);
    remove_node(head->prev);
    add_at_the_end(&head, 100);
    node *find = find_node(tail, 3);
    // node *curr = tail;
    // while (curr != NULL)
    // {
    //     printf("the number is: %d\n", curr->x);
    //     curr = curr->next;
    // }
    dalloc(&tail, &head);
}
