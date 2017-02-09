if __name__ == '__main__':
    import sys
    keyword = "LoveTanling"
    try:
        keyword = sys.argv[1]
    except:
        pass

    print('\n'.join([''.join([(keyword[(x-y)%len(keyword)]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)]))
