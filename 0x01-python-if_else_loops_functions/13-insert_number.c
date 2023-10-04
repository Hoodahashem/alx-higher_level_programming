#include "lists.h"
/**
 * insert_node - gustavo
 * @head: gustavo
 * @number:gustavo
 * Return:gustavo
*/
listint_t *insert_node(listint_t **head, int number)
{
		listint_t *n, *c;

		n = malloc(sizeof(listint_t));
		if (!n)
			return (NULL);
		n->n = number;
		if (!*head)
		{
			n->next = *head;
			*head = n;
			return (n);
		}
		c = *head;
		if (number < c->n)
		{
			n->next = c;
			*head = n;
			return (n);
		}
		while (c->next && c->next->n < number)
			c = c->next;
		n->next = c->next;
		c->next = n;
		return (n);
}
