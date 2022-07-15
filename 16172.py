import sys
input = sys.stdin.readline
a = input().rstrip()
st=[]
b = input().rstrip()
for i in a:
    if not i.isdigit():
        st.append(i)
st = "".join(st)
if b in st:
    print(1)
else:
    print(0)
#
# s = input().rstrip()
# k = input().rstrip()
# "".isdigit()