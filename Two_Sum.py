class Solution:
    def TwoSum(array: list[int], target:int):
        hashmap={}
        for i in range(len(array)):
            component=target-array[i]
            if component in hashmap:
                return [hashmap[component], i]
            hashmap[array[i]]=i
            
        return []
    
    array=[1,2,3,4,5]
    target=3
    result=TwoSum(array,target)
    print(result)