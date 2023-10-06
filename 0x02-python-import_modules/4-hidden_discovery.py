#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    gus = dir(hidden_4)
    for i in range(len(gus)):
        for j in range(len(gus[i])):
            if (gus[i][j] == '_' and gus[i][j+1] == '_'):
                break
            else:
                print(gus[i])
                break
