import os,sys

script="~/sire.app/bin/python ~/software/devel/BioSimSpace/nodes/playground/prepareFEP.py"

perts = ["1:9","9:1","1:15","15:1","15:3","3:15","15:5","5:15","3:5","5:3",
         "15:16","16:15","5:16","16:5","15:10","10:15","15:6","6:15","6:10",
         "10:6","15:17","17:15","1:17","17:1","17:13","13:17","17:12","12:17",
         "17:8","8:17","17:4","4:17","4:14","14:4","4:11","11:4","11:7","7:11",
         "7:14","14:7","14:2","2:14","2:7","7:2"]


print ("@@@@ FREE LEGS@@@")
for pert in perts:
    a,b = pert.split(":")
    aparm = "1-fesetup-noequil/_ligands/tyk_lig%s/solvated.parm7" % a
    arst = "2-openmmequil/rst7_files/tyk_lig%s_equilibrated.rst7" % a
    bparm = "1-fesetup-noequil/_ligands/tyk_lig%s/solvated.parm7" % b
    brst = "2-openmmequil/rst7_files/tyk_lig%s_equilibrated.rst7" % b
    cmd = "%s --input1 %s %s --input2 %s %s --output output/%sto%s_free" % (script,aparm,arst,bparm,brst,a,b)
    print (cmd)
    os.system(cmd)
    if not os.path.exists("output/%sto%s_free.prm7" % (a,b)):
        print ("ERROR ! Output not created")
    sys.stdout.flush()
    sys.stderr.flush()
    #sys.exit(-1)

print ("@@@@ BOUND LEGS@@@")
for pert in perts:
    a,b = pert.split(":")
    aparm = "1-fesetup-noequil/_complexes/TYK2-tyk_lig%s/solvated.parm7" % a
    arst = "2-openmmequil/rst7_files/TYK2_tyk_lig%s_equilibrated.rst7" % a
    bparm = "1-fesetup-noequil/_complexes/TYK2-tyk_lig%s/solvated.parm7" % b
    brst = "2-openmmequil/rst7_files/TYK2_tyk_lig%s_equilibrated.rst7" % b
    cmd = "%s --input1 %s %s --input2 %s %s --output output/%sto%s_bound" % (script,aparm,arst,bparm,brst,a,b)
    print (cmd)
    os.system(cmd)
    if not os.path.exists("output/%sto%s_bound.prm7" % (a,b)):
        print ("ERROR ! Output not created")
    sys.stdout.flush()
    sys.stderr.flush()
    #sys.exit(-1)
