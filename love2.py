def drawLove(keyword):
    arr=[]
    for y in range(15,-15,-1):
        line_arr = []
        for x in range(-30,30):
            if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0:
                line_arr.append(keyword[(x-y)%8])
            else:
                line_arr.append(' ')
        arr.append(''.join(line_arr))
    print('\n'.join(arr))

if __name__ == '__main__':
    drawLove("LoveTanling")
