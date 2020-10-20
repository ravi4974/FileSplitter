import os,math,sys

def split(filepath,chunksize):
    if not os.path.exists(filepath):
        print("FileNotFoundError: {} does not exists!".format(filepath))
        sys.exit(2)

    filesize=os.stat(filepath).st_size

    with open(filepath,'rb') as f:
        for i in range(math.ceil(filesize/chunksize)):
            partfile=filepath+'.part'+str(i)
            if os.path.exists(partfile):
                if os.stat(partfile).st_size==min(chunksize,filesize-i*chunksize):
                    print("Skipping : Part file {} already exists".format(partfile))
                    continue
                else:
                    os.remove(partfile)
            
            f.seek(i*chunksize)
            print("Creating part file {}...".format(partfile))
            with open(partfile,'wb+') as pf:
                pf.write(f.read(chunksize))

def main():
    if len(sys.argv)<2:
        print("")
        print("Usage: {0} <filepath> [<chunksize>]".format(__file__))
        sys.exit(1)

    chunksize=500*1024*1024
    if len(sys.argv)>2:
        size=sys.argv[2]
        if size.endswith('k'):
            chunksize=int(size[:-1])*1024
        elif size.endswith('m'):
            chunksize=int(size[:-1])*1024*1024
        elif size.endswith('g'):
            chunksize=int(size[:-1])*1024*1024*1024

    filepath=sys.argv[1]
    split(filepath,chunksize)

if __name__ == "__main__":
    main()