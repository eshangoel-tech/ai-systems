from fastapi import FastAPI
import json
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

def load_data():
    with open("data.json", "r") as f:
        return json.load(f)

@app.get("/data")
def get_data():
    return load_data()

@app.get("/mergesort")
def mergesort():
    arr = [2,3,1,4,5,7,6,9,2]
    return split(arr)
    

def split(arr):
    mid = len(arr) // 2
    if len(arr) <= 1:
        return arr
    else:
        left = arr[:mid]
        right = arr[mid:]
        
    left = split(left)
    right = split(right)
    return merge(left, right)

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left)
    result.extend(right)
    return result   


def recurr(i,arr):
    if i==0:
        return 1
    elif i<1:
        return -9999
    
    left=recurr(i-1,arr)+arr[i]
    right=recurr(i-2,arr)+arr[i]

    return max(left,right)

@app.get("/recurr")
def recurrent():
    arr = [1,2,3,4,5,6,7,8,9,10]
    return recurr(len(arr)-1,arr)
