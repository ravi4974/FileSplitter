import os,re,sys

def join(filepath):
    if not re.search('\.part\d+',filepath):
        print("Invalid file : {}".format(filepath))
        sys.exit(1)
    
    actual_file,ext=os.path.splitext(filepath)

    if os.path.exists(actual_file):
        os.remove(actual_file)
    
    partdir=os.path.dirname(actual_file)
    _,_,dirfiles=next(os.walk(partdir))
    dirfiles.sort()

    for idx,dirfile in enumerate(dirfiles):
        if not dirfile.endswith(str(idx)):
            print("MissingPartFile: {}.part{} is missing...".format(actual_file,idx))
            sys.exit(3)

    with open(actual_file,'wb+') as f:
        for dirfile in dirfiles:
            dirfile=os.path.join(partdir,dirfile)
            if dirfile.startswith(actual_file+'.part'):
                print("Processing part file {}...".format(dirfile))
                with open(dirfile,'rb') as pf:
                    f.write(pf.read())

def main():
    if len(sys.argv)<2:
        print("")
        print("Usage: {0} <part-filepath>".format(__file__))
        sys.exit(1)

    filepath=sys.argv[1]
    join(filepath)

if __name__ == "__main__":
    main()