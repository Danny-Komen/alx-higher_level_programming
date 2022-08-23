#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for Holbertton project
 */

typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

size_t print_listint(const listint *h);
listint_t *add_nodeint(listint **head, const int n);
void free_listint(listint_t *h);
int check_cycle(listont_t *list);

#endif /* LISTS_H */
