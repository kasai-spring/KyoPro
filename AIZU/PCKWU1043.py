import sys

while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break
    teamList = [[int(x) for x in sys.stdin.readline().split()] for y in range(N)]
    teamList.sort(key=lambda x: x[3])
    teamList.sort(key=lambda x: x[2], reverse=True)
    selectedTeamNumber = 0
    selectedTeam = []
    teamID = {}
    while True:
        for i in teamList:
            if selectedTeamNumber < 10:
                if i[1] in teamID:
                    if teamID[i[1]] > 2:
                        continue
                    else:
                        teamID[i[1]] += 1
                        selectedTeamNumber += 1
                        selectedTeam.append(i[0])
                        teamList.remove(i)
                        break
                else:
                    teamID[i[1]] = 1
                    selectedTeamNumber += 1
                    selectedTeam.append(i[0])
                    teamList.remove(i)
                    break
            elif selectedTeamNumber < 20:
                if i[1] in teamID:
                    if teamID[i[1]] > 1:
                        continue
                    else:
                        teamID[i[1]] += 1
                        selectedTeamNumber += 1
                        selectedTeam.append(i[0])
                        teamList.remove(i)
                        break
                else:
                    teamID[i[1]] = 1
                    selectedTeamNumber += 1
                    selectedTeam.append(i[0])
                    teamList.remove(i)
                    break
            elif selectedTeamNumber < 26:
                if i[1] in teamID:
                    continue
                else:
                    teamID[i[1]] = 1
                    selectedTeamNumber += 1
                    selectedTeam.append(i[0])
                    teamList.remove(i)
                    break

        else:
            break
    for i in selectedTeam:
        print(i)
