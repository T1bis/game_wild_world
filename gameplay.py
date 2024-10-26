import pygame
import math
from food import Food
from lion import Lion

from random import *

def in_one_place(animal,arr):
    for i in range(len(arr)):
        if animal.x == arr[i].x:
            if animal.y == arr[i].y:
                arr[i].locate_food()
                return 1

def in_joke(animal,arr):
    for i in range(len(arr)):
        if animal.x == arr[i].x:
            if animal.y == arr[i].y:
                animal.locate_food()
                return 1




def make_arr(arr,window,type,size,lion):
    while len(arr) < size:
        obj = type(randint(0, 5) * 70 + 5, randint(1, 5) * 70 + 5)
        if(lion.x != obj.x and lion.y != obj.y ):
            arr.append(obj)
    for i in arr:
        window.blit(i.image, (i.x, i.y))




