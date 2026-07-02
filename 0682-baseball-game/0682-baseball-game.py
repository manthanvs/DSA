class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for i in range(len(operations)):
            try:
                res.append(int(operations[i]))
            except ValueError:
                if operations[i] == "+":
                    res.append(res[-2] + res[-1])
                elif operations[i] == "D":
                    res.append(res[-1] * 2)
                elif operations[i] == "C":
                    res.pop()  # pop is way quicker here than del
        return sum(res)
        
        
# * For better understanding

# operations = ["5","-2","4","C","D","9","+","+"]
# res = []
# for i in range(len(operations)):
#     try:
#         res.append(int(operations[i]))
#         print(res)
#     except ValueError:
#         if operations[i] == "+":
#             print(res[-2])
#             res.append(res[-2] + res[-1])
#         elif operations[i] == "D":
#             res.append(res[-1] * 2)
#         elif operations[i] == "C":
#             res.pop()  # pop is way quicker here than del
#         print("Except", res)
# print(sum(res))
