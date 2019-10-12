#include <stdio.h>
#include <stdlib.h>
#include<conio.h>
struct node {
    int num;
    struct node * nextptr;
}*stnode;

struct node *tail,*p,*q,*store,*cur;
void displayClList(int a);
 void AddFront( int data)
  { int d =1;
 struct node *temp = (struct node*)malloc(sizeof(struct node));
  temp->num = data;
  temp->nextptr = stnode;
  cur=stnode;
  while(cur->nextptr!=stnode)
 {
   cur=cur->nextptr;
 }   cur->nextptr=temp;
    stnode=temp;
  displayClList(d);
  }

void ClListcreation(int n);
void ClListDeleteLastNode();


int main()
{
    int n,num1,a,pos,c;
    stnode = NULL;
    clrscr();
	printf("\n\n Circular Linked List : Delete node at the end of a circular linked list :\n");
	printf("--------------------------------------------------------------------------------\n");

    printf(" Input the number of nodes : ");
    scanf("%d", &n);
    ClListcreation(n);
    a=1;
    displayClList(a);
    tail=stnode;
    //ClListDeleteLastNode();
    //a=2;
printf("\n Enter new data = ");
scanf("%d",&c);
  AddFront(c);
displayClList(a);
  getch();
    return 0;
}

void ClListcreation(int n)
{
    int i, num;
    struct node *preptr, *newnode;

    if(n >= 1)
    {   tail = (struct node *)malloc(sizeof(struct node));
	stnode = (struct node *)malloc(sizeof(struct node));
	tail=stnode;
	printf(" Input data for node 1 : ");
	scanf("%d", &num);
	stnode->num = num;
	stnode->nextptr = NULL;
	preptr = stnode;
	for(i=2; i<=n; i++)
	{
	    newnode = (struct node *)malloc(sizeof(struct node));
	    printf(" Input data for node %d : ", i);
	    scanf("%d", &num);
	    newnode->num = num;
	    newnode->nextptr = NULL;	// next address of new node set as NULL
	    preptr->nextptr = newnode;	// previous node is linking with new node
	    preptr = newnode;   		// previous node is advanced
	}
	preptr->nextptr = stnode; 		//last node is linking with first node
    }
}

void ClListDeleteLastNode()
{
		p=stnode;
		while(p->nextptr!=stnode)
		{
			q=p;
			p=p->nextptr;
		}
		q->nextptr=stnode;
		printf("\n The deleted node is : %d",p->num);
		free(p);
}

void displayClList(int m)
{
    struct node *tmp;
    int n = 1;

    if(stnode == NULL)
    {
	printf(" No data found in the List yet.");
    }
    else
    {
	tmp = stnode;
	if (m==1)
	{
	printf("\n Data entered in the list are :\n");
	}
	else
	{
	 printf("\n After deletion the new list are :\n");
	}
	do {
	    printf(" Data %d = %d\n", n, tmp->num);

	    tmp = tmp->nextptr;
	    n++;
	}while(tmp != stnode);
    }
}
