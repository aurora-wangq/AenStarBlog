id:5
title:第k个数
author:AenStarAX
date:2024-05-01 23:17:25
---
跟快速排序模板基本一样
```cpp
#include<iostream>
#include<time.h>
using namespace std;
const int N = 1e5 + 10;
int n, q[N], k;

void quick_sort(int q[], int l, int r)
{
    if (l >= r) return;
    int x = q[rand() % (r - l + 1) + l], i = l - 1, j = r + 1;
    while (i < j)
    {
        do i++; while(q[i] < x);
        do j--; while(q[j] > x);
        if (j > i) swap(q[i], q[j]);
    }
    quick_sort(q, l, j);
    quick_sort(q, j + 1, r);
}
int main()
{
    scanf("%d%d", &n, &k);
    for (int i = 0; i < n; i ++) scanf("%d", &q[i]);
    quick_sort(q, 0, n - 1);
    printf("%d", q[k - 1]);
    return 0;
}
```