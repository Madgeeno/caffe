import sys
import fileinput

fName = 'caffe.pb.h'
addline = '#undef STRICT // conflict with winmindef.h included by Application module'
print 'Modifying', fName, 'for BM project'
print 'Inserting line: ', addline

fileName = str(sys.argv[1])+'/' + fName

for line in fileinput.input(fileName, inplace=1):
 print line,
 if line.startswith('#define PROTOBUF_caffe_2eproto__INCLUDED'):
     print addline,