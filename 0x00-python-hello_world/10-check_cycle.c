#include "lists.h"
/**
*check_cycle - checks for cycle in linked list
*@list: list of  or head of the list
*Return: 0 if no cycle otherwise 1
*/
int check_cycle(listint_t *list)
{
listint_t *p1, *p2;
if (list == NULL || list->next == NULL)
return (0);
p1 = list->next;
p2 = list->next->next;
while (p1 && p2 && p2->next)
{
if (p1 == p2)
return (1);
p1 = p1->next;
p2 = p2->next->next;
}
return (0);
}
