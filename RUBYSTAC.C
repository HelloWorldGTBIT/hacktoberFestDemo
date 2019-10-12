//stack
#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
struct stack
{ int bno;
  char bnm[25];
  struct stack *next;
};
struct stack *top,*newptr,*ptr;
void display()
{ if(top==NULL)
  printf("\n Stack is empty ");
  else
  { printf("\n Stack is ");
    ptr=top;
    printf("\n -> ");
    while(ptr)
    { printf("%d",ptr->bno);
      printf("%s  ",ptr->bnm);
      printf("\n   ");
      ptr=ptr->next;
    }
  }
}
void push()
{ newptr = (struct stack*)malloc(sizeof(struct stack));
  if(newptr==NULL)
  { printf("\n Memory overflow ");
  }
  else
  { printf("\n Enter book number = ");
    scanf("%d",&newptr->bno);
    printf("\n Enter book name = ");
    scanf("%s",&newptr->bnm);
    newptr->next=NULL;
    if(top==NULL)
    top=newptr;
    else
    { newptr->next=top;
      top=newptr;
    }
    printf("\n Stack after push : \n ");
    display();
  }
}
void pop()
{ if(top==NULL)
  printf("\n Memory underflow stack is empty ");
  else
  { ptr=top;
    top=top->next;
    free(ptr);
    printf("\n Stack after pop : \n ");
    display();
  }
}
void main()
{  int ch;
   top=NULL;

   do
   { clrscr();
     printf("\n              MENU            ");
     printf("\n 1.Push in linked list stack ");
     printf("\n 2.Pop in linked list stack  ");
     printf("\n 3. Traverse the stack       ");
     printf("\n 4. Exit           	    ");
     printf("\n Enter choice (1-4) =        ");
     scanf("%d",&ch);
     switch(ch)
     { case 1 : push();
		 break;
       case 2 : pop();
		break;
       case 3 : display();
		break;
       case 4 : printf("\n Terminating ");
		break;
       default:printf("\n Wrong Choice ");
		break;
     }
     getch();
   }while(ch!=4);
}
