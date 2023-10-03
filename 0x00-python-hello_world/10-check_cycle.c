#include "lists.h"

/**
 * check_cycle - gustavo
 * @list: gustavo
 *
 * Return: gustavo
 */
int check_cycle(listint_t *list)
{
	listint_t *s = list;
	listint_t *f = list;

	if (list == NULL)
		return (0);
	while (s != NULL && f != NULL && f->next != NULL)
	{
		s = s->next;
		f = f->next->next;

		if (s == f)
			return (1);
	}
	return (0);
}
