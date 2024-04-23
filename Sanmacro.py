with open("macro.txt", "r") as file:
    lines = file.readlines()

mnt = []
mdt = []
ala = []
labelIndex = 0

i = 0

while i < len(lines):

    if lines[i].strip().upper() == "MACRO":
        counter = 0
        i += 1

        while lines[i].strip().upper() != "MEND":
            if counter == 0:

                mac = lines[i].strip().split(' ')
                mdt.append(mac)
                mdtIndex = len(mdt)

                mnt.append([mac[1], str(mdtIndex)])

                for itr in mac[2].split(','):
                    if itr not in ala:
                        ala.append(itr)

                counter += 1
                i += 1

            else:
                mac = lines[i].strip().split(' ')

                if len(mac) == 2:
                    ala_temp = mac[1].split(',')
                    index = ""
                    if len(ala_temp) > 1:
                        index = str(ala.index(ala_temp[1]) + 1)
                    mdt.append(['', mac[0], f"{ala_temp[0]}," + "#" + index])

                elif len(mac) == 3:
                    ala_temp = mac[2].split(',')
                    index = ""
                    if len(ala_temp) > 1:
                        index = str(ala.index(ala_temp[1]) + 1)

                    mdt.append([f'#{labelIndex}', mac[1], f"{ala_temp[0]},"  "#" + index])
                    labelIndex += 1

                i += 1
    else:
        i += 1

print("\nMNT")
print("Index\tName\tMDT index")
for count, itr in enumerate(mnt):
    print(f"{count + 1}\t{itr[0]}\t{itr[1]}")

print("\nMDT")
print("Index\t\tName")
for count, itr in enumerate(mdt):
    print(f"{count + 1}\t{itr[0]}\t{itr[1]}\t{itr[2]}")

print("\nDummy ALA in Pass 1")
print("Index\tArguements")
for count, itr in enumerate(ala):
    print(f"{count + 1}\t{itr}")