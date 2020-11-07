#!/usr/bin/env python
#-*- coding:utf-8 -*- 
#@Time: 2020-11-06 15:35:38
#@Author: 张柯尧
#@File: E:\myE\数学\bernollimotinomial.py
#@Software:sublime Text 3

'''
本库支持伯努利多项式及伯努利数的相关运算
需要先下载sympy库
'''

from fractions import Fraction
import math
import sympy

#获得组合数(n, k)___O(n)
def combination(n, k):
	return Fraction(math.factorial(n), math.factorial(k) * math.factorial(n - k))

#获得phi(n)列表___O(n**3)	
def findphi(n = -1):
	if n == -1:
		n = int(input("输入所需phi(i)项数:"))
	phi = []
	phi.append(Fraction(1, 1))
	phi.append(Fraction(-2, 4))
	for i in range(2, n + 1):
		x = 0
		for j in range(0, i):
			x += phi[j] *  combination(i + 1, j)
		x = Fraction(-1, i + 1) * x
		phi.append(x)
	return phi

#获得B(n)列表___O(n**3)
def findB(n = -1):
	if n == -1:
		n = int(input("输入所需B(i)项数:"))
	phi = findphi(2 * n)
	B = []
	flag = 1
	for i in range(1, n + 1):
		flag = -flag
		B.append(phi[2 * i] * flag)
	return B	

#获得贝努利多项式phin(x)___O(n**3)
def bernolli(n = -1, x = sympy.symbols('x')):
	if n == -1:
		n = int(input("输入所需benolli(x)对应的n:"))
	phin = 0
	phi = findphi(n)
	for k in range(0, n + 1):
		phin += x**(n - k) * phi[k] * combination(n, k)
	return phin	

#获得从1到n的贝努利多项式的列表___O(n**3)
def bernollilist(n = -1, x = sympy.symbols('x')):
	if n == -1:
		n = int(input("输入所需bernolli(x)项数："))
	phinl = [1];
	phi = findphi(n)
	for k in range(1, n + 1):
		phinl.append(sympy.integrate(phinl[k - 1], x) * k + phi[k])
	return phinl

#获得1**n+2**n+3**n+...+m**n的值___O(n**3)
def powersum(m, n):
	x = sympy.symbols('x')
	ber = bernollilist(n + 1, x)
	prehalf = ber[n + 1].evalf(subs = {x : m + 1})
	lsthalf = ber[n + 1].evalf(subs = {x : 0})
	sum = (1 / (n + 1)) * (prehalf - lsthalf)
	return sum

#以下为正式程序
# print(findB(20))