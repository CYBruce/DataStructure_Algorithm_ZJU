#include <stdio.h>
#include <stdlib.h>
#define MAXSIZE 10
#define NotFound 0
typedef int ElementType;

typedef int Position;
typedef struct LNode *List;
struct LNode {
    ElementType Data[MAXSIZE];
    Position Last; /* 保存线性表中最后一个元素的位置 */
};

List ReadInput(); /* 裁判实现，细节不表。元素从下标1开始存储 */
Position BinarySearch( List L, ElementType X );

List ReadInput(){//List is a point;
    int N;
    scanf("%d",&N);
    List L = (struct LNode*)malloc(sizeof(struct LNode)); /* Strange!! Why LNode is non-declared? Use struct LNode instead of LNode!!!*/
    L->Last = N;
    for(ElementType i=1;i<=N;i++){
        scanf("%d",&L->Data[i]);
    }
    return L;
}

int main()
{
    List L;
    ElementType X;
    Position P;

    L = ReadInput();
    scanf("%d", &X);
    P = BinarySearch( L, X );
    printf("%d\n", P);

    return 0;
}

/* 你的代码将被嵌在这里 */
Position BinarySearch( List L, ElementType X ){
    Position position;
    Position left = 0;
    Position right = L->Last;
    ElementType flag = 0;
    while(left <= right){
        Position mid = left + (right -left)/2;
        /* I know that there should notice sth,
        but i cannot remember that exactly*/
        if(L->Data[mid] == X){
            position = mid;
            flag = 1;
            break;
        }
        else if(L->Data[mid] > X){
            right = mid-1;
        }else{
            left = mid+1;
        }
    }
    if(flag == 0)
        position = NotFound;
    return position;  /*Only one return.*/
}
