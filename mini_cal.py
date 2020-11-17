print("Enter current date")
cd = int(input())
print("Enter current month")
cm = int(input())
print("Enter current year")
cy = int(input())
print("Enter Birth date")
bd = int(input())
print("Enter Birth month")
bm = int(input())
print("Enter Birth year")
by = int(input())
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if bd > cd:
    cm = cm - 1
    cd = cd + month[bm - 1]
if bm > cm:
    cy = cy - 1
    cm = cm + 12

calyear = cy - by
calmon = cm - bm
caldays = int(cd) - bd

print("\nYour age is:", caldays, end='')
print(" Days", calmon, end='')
print(" Month", calyear, end='')
print(" Year")
