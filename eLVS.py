
import networkx as nx
import matplotlib.pyplot as plt


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(773, 695)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(450, 10, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(530, 10, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(610, 120, 151, 91))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(450, 110, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(450, 50, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(440, 570, 141, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(590, 590, 151, 17))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(590, 610, 151, 17))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(590, 630, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(590, 570, 171, 17))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName("checkBox_4")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 411, 671))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(450, 160, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.checkBox_6 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_6.setGeometry(QtCore.QRect(620, 90, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_6.setFont(font)
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_7 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_7.setGeometry(QtCore.QRect(620, 60, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.checkBox_7.setFont(font)
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_8.setGeometry(QtCore.QRect(620, 40, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.checkBox_8.setFont(font)
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_9 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_9.setGeometry(QtCore.QRect(620, 20, 91, 17))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_9.setFont(font)
        self.checkBox_9.setObjectName("checkBox_9")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(450, 210, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(450, 500, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(23)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(490, 500, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(580, 500, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(530, 500, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(450, 300, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(530, 300, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(450, 330, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(450, 260, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(610, 500, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_18.setGeometry(QtCore.QRect(610, 210, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_19.setGeometry(QtCore.QRect(610, 460, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_20.setGeometry(QtCore.QRect(690, 460, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_21.setGeometry(QtCore.QRect(730, 460, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_22 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_22.setGeometry(QtCore.QRect(510, 330, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_22.setFont(font)
        self.pushButton_22.setObjectName("pushButton_22")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "<<"))
        self.pushButton_2.setText(_translate("MainWindow", ">>"))
        self.pushButton_3.setText(_translate("MainWindow", "Search"))
        self.pushButton_4.setText(_translate("MainWindow", "Devices  -> Net"))
        self.pushButton_5.setText(_translate("MainWindow", "Net  -> Devices"))
        self.pushButton_6.setText(_translate("MainWindow", "Plot"))
        self.checkBox.setText(_translate("MainWindow", "no RCM wires"))
        self.checkBox_2.setText(_translate("MainWindow", "stop after PU"))
        self.checkBox_3.setText(_translate("MainWindow", "no Cap, WPAD"))
        self.checkBox_4.setText(_translate("MainWindow", "stop at UXX-XX"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_7.setText(_translate("MainWindow", "MCN <-> Descrip"))
        self.checkBox_6.setText(_translate("MainWindow", "MCNs"))
        self.checkBox_7.setText(_translate("MainWindow", "partNames"))
        self.checkBox_8.setText(_translate("MainWindow", "nets"))
        self.checkBox_9.setText(_translate("MainWindow", "Devices"))
        self.pushButton_8.setText(_translate("MainWindow", "Device -> MCN"))
        self.pushButton_9.setText(_translate("MainWindow", "↑"))
        self.pushButton_10.setText(_translate("MainWindow", "↓"))
        self.pushButton_11.setText(_translate("MainWindow", "?"))
        self.pushButton_12.setText(_translate("MainWindow", "↓↓↓"))
        self.pushButton_13.setText(_translate("MainWindow", "Caps"))
        self.pushButton_14.setText(_translate("MainWindow", "RES"))
        self.pushButton_15.setText(_translate("MainWindow", "Nets"))
        self.pushButton_16.setText(_translate("MainWindow", "Cap Count"))
        self.pushButton_17.setText(_translate("MainWindow", "Export Cap Count"))
        self.pushButton_18.setText(_translate("MainWindow", "sel BOM"))
        self.pushButton_19.setText(_translate("MainWindow", "Add net"))
        self.pushButton_20.setText(_translate("MainWindow", "?"))
        self.pushButton_21.setText(_translate("MainWindow", "X"))
        self.pushButton_22.setText(_translate("MainWindow", "end ICs"))


import os

print('Programm starting...')

def qpp(qpp_file, refDeslist,debug):     #using qcae_parts_properties file
    
    f=open(qpp_file,'r')    
    descrList=[None]*len(refDeslist)
    mcn=list(descrList)
    for line in f:
        a = line.split('\t\t')
        word= a[0].split('\t')
        if word[0] in refDeslist:
            b=refDeslist.index(word[0])
            descrList[b]=a[1].split('\t')[0]
            mcn[b]=word[1]
        elif debug:
            print ('RefDes in qpp is note present in bom.txt-   ' + word [0])
    return (descrList)
def bom_init(filename):
    list1=[]
    list2=[]
    PartsList=[]
    BomName=[]
    RefDesList=[]
    f=open(filename,'r')
    for line in f:
        if line[0] =='-':
            BomName.append(line.split()[1])
           #'new BOM, new List'
            PartsList.append(list1)
            RefDesList.append(list2)
            list1=[]
            list2=[]
        words=line.rstrip().split(';')
        if words[0].isdigit():
            count=0;
            for word in words:
               if count==1:
                   list1.append(word)
               elif count==2:
                   list2.append(word)
               count=count+1
    PartsList.append(list1)               
    RefDesList.append(list2)
    return(RefDesList,PartsList,BomName)
def Read_netlist_QCV(qcv_path):
    f=open(qcv_path,'r')
    # import re
    netList =[]
    CCMPL =[]  #corrsponding componet list
    CPML =[]  #corrsponding pin map list 
    temp_component_ = ''
    Comp_2_net_pinName_map = {}
    temp_dict = {}
    for i,line in enumerate(f):
        words=line.split()
        if words[0] == 'FlatNet:':
            #if words[1] == "'AGND'" or words[1] == "'DGND'":
            #    continue
            temp = words[1].replace("'", "")
            netList.append(temp)
            component_list =[]
            pin_list=[]
        
            for component_pin in words[2:]:
                CPS= component_pin.split('-')
                if (len(CPS) <1):
                    return ('syntax error in net list')
                component_list.append(CPS[0])
                pin_list.append( CPS[1])
            #print (pin_list,component_list)
            CCMPL.append(component_list)
            CPML.append(pin_list)
            continue
        if words[0] == 'COMP:':
            if temp_component_ in Comp_2_net_pinName_map:
                temp_dict.update (   Comp_2_net_pinName_map [temp_component_ ]  )
                Comp_2_net_pinName_map [temp_component_ ]  =  temp_dict
            else:
                Comp_2_net_pinName_map [temp_component_ ] =  temp_dict
            temp_dict = {}
            temp_component_ = words[2][1:-1]
            continue
        if words [0] == 'Explicit':
            net_temp = words [4][1:-1]
            pinnum_name = words[2][1:-1]  + '  ' + words[3][1:-1]
            if net_temp in temp_dict:
                temp_dict [ net_temp ] = pinnum_name + '\n'+ temp_dict [ net_temp ]
            else:
                temp_dict [ net_temp ] = pinnum_name
            continue
    f.close()
    corr_Conn_count =list(netList)
    for i in range(len(netList)) :
        corr_Conn_count[i] = len(CPML[i])
        #print (netList [i] ,'==', CPTs[i])
    #===============================
    #       netlist centric
    # netList, CCMPL, CPML, corr_Conn_count
    #===============================
    CompL=  []
    CnetList = []  # corresponding netlist
    CPinList = []  # Corresponding pin list
    
    for x in range(len(CCMPL)):
        for i,U in enumerate(CCMPL[x]):
            if U not in CompL:
                CompL.append(U)
                CnetList.append([netList[x]])
                CPinList.append([CPML[x][i]])
    
                
            else:
                indx = CompL.index(U)
                CnetList[indx].append(netList[x])
                CPinList[indx].append(CPML[x][i])
    PC =list(CompL)         # pin count
    for i in range(len(CompL)) :
        PC[i] = len(CPinList[i])
        #print (CompL [i] ,'==', PC[i])
    #===============================
    #       device centric
    # CompL, CnetList, CPinList , PC
    #===============================      
    CNGnetList, CNGPinList = [],[]
    for x in range(len(CnetList)):
        tempList1, tempList2  =[], []
        for i,U in enumerate(CnetList[x]):
            if "GND" not in U:
                tempList1 .append (U)
                tempList2 .append(CPinList[x][i])
        
        CNGnetList.append(tempList1)
        CNGPinList.append(tempList2)

    #===============================
    #       device centric  but ground excluded  : NG = No ground
    # CNGnetList, CNGPinList
    #===============================  
    
    return ( netList, CCMPL, CPML, corr_Conn_count, CompL, CnetList, CPinList, PC, CNGnetList, CNGPinList, Comp_2_net_pinName_map)
def list2string(a):
    c= set(a)
    b= ''
    for i in c:
        b=b+i+'\n'
    return b

class Net_container :
    def __init__(self):
        self.G=nx.Graph()
        self.DisconnectedDevices= []
        self.RefDesList_global, self.PartsList_global =[], []
        self.Buffer_length = 40
        self.PastStrings = ['' ]*self.Buffer_length
        self.pointer =self.Buffer_length - 1 
        self.Cap_list_Buffer =[]
        self.get_cap_flag = False
        self.get_Res_flag = False
        self.get_net_flag = False
        self.BOM_choose_FSM = 0
        self.NET_storage = []
        self.capacitance_flag=False
        self.Device_Buffer = []
        self.device_pin_flag = False
        
        
        self.main_window =QtWidgets.QMainWindow()
        self.winObj = Ui_MainWindow()
        self.winObj.setupUi(self.main_window)
        
        self.winObj.pushButton.clicked.connect(self.goBack)
        self.winObj.pushButton_2.clicked.connect(self.goForward)
        self.winObj.pushButton_3.clicked.connect(self.search_Universal) 
        self.winObj.pushButton_4.clicked.connect(self.Device2Nets)  
        self.winObj.pushButton_5.clicked.connect(self.Net2Devices)  
        self.winObj.pushButton_6.clicked.connect(self.process_graph) 
        self.winObj.pushButton_7.clicked.connect(self.MCN_Descr_convert)
        self.winObj.pushButton_8.clicked.connect(self.get_part_details)
        self.winObj.pushButton_9.clicked.connect(self.DNI_refdes)
        self.winObj.pushButton_10.clicked.connect(self.Mount_refdes)
        self.winObj.pushButton_12.clicked.connect(self.Free_all_DNIed)
        self.winObj.pushButton_11.clicked.connect(self.show_DNied)
        self.winObj.pushButton_13.clicked.connect(self.Get_Caps)
        self.winObj.pushButton_14.clicked.connect(self.Get_Rs)
        self.winObj.pushButton_15.clicked.connect(self.Get_NET)
        self.winObj.pushButton_16.clicked.connect(self.Capacitance_count)
        self.winObj.pushButton_17.clicked.connect(self.Capacitance_count_export  )
        self.winObj.pushButton_18.clicked.connect(self.Choose_BOM)
        self.winObj.pushButton_19.clicked.connect(self.Add_net)
        self.winObj.pushButton_20.clicked.connect(self.Show_net_storage)
        self.winObj.pushButton_21.clicked.connect(self.free_all_nets)
        self.winObj.pushButton_22.clicked.connect(self.get_components)
        
        self.winObj.checkBox_8.setChecked(True)
        
        
        
        
 
        fname =  'qcae'
            
        self.bom_combined_path = fname+ '/bom/bom_combined.txt'
        self.Board1_qcv_path = fname+'/nets/Board1.qcv'
        self.qpp = fname+'/bom/qcae_part_properties.txt'
        
        if os.path.exists (self.bom_combined_path )    and os.path.exists (self.Board1_qcv_path )  and os.path.exists ( self.qpp):
            print ('found the files !  ')
            self.main_window.show()
        else:
            print ('bom_combined , qcae_parts_properties or Board1.qcv doesn\'t exist inside folder' )
            return
        self.acquire_data ()           
    def acquire_data (self):
        self.RFDS_List,self.RFDS2_MCN_List,self.BomName = bom_init(self.bom_combined_path)
        a= Read_netlist_QCV(self.Board1_qcv_path)
        # netList, CCMPL, CPML, corr_Conn_count, CompL, CnetList, CPinList, PC, CNGnetList, CNGPinList = a
        self.NL, self.N2C, self.N2P_C, self.N2Cn, self.CL, self.C2N, self.C2P_N, self.C2Pc, self.C2N_NG, self.C2P_N_NG , self.Comp_2_net_pinName_map_global     = a 
        
        
        self.RFDS_List_0 = self.RFDS_List [1]
        self.RFDS2_MCN_List_0 = self.RFDS2_MCN_List [1]
        self.descr =  qpp ( self.qpp, self.RFDS_List_0 , False)
        self.MCN_Descr_LUT ()
        print ('Got the data !')
        
    
    def print_B (self, textt):
        self.winObj.textEdit.clear()
        self.winObj.textEdit.append (textt)
    def Device2Nets(self):
        DeviceName = self.get_text()
        if DeviceName in self.CL:
            indx = self.CL.index(DeviceName)
            a= list2string(self.C2N_NG[indx] )
            self.print_B(a)
            self.push (a)
        else:
            a= "device Not Found" 
            self.print_B(a)   
            self.push (a)            
    def Net2Devices(self):
        netName =  self.get_text()
        if netName in self.NL:
            indx = self.NL.index(netName)
            a= list2string(self.N2C[indx] )
            self.print_B(  a )
            self.push (a)
        else:
            a= "net Not Found"
            self.print_B( a )
            self.push (a)
    def Net2DevicesInternal(self,netName):
        if netName in self.NL:
            indx3 = self.NL.index(netName)
            return (self.N2C[indx3])
        else:
            return [False]  
    def Device2NetsInternal(self,DeviceName):
        if DeviceName in self.CL:
            indx2 = self.CL.index(DeviceName)
            return ( self.C2N_NG[indx2] )  
    def search_Universal(self):
        Name = self.get_text()
        searchResults=[]
        dictionary_list = []
        if self.winObj.checkBox_9.isChecked ():
            dictionary_list= dictionary_list + self.CL
        if self.winObj.checkBox_8.isChecked ():
            dictionary_list= dictionary_list +self.NL
        if self.winObj.checkBox_7.isChecked ():
            dictionary_list= dictionary_list + self.descr
        if self.winObj.checkBox_6.isChecked ():
            dictionary_list= dictionary_list + self.RFDS2_MCN_List_0
            
        for i in  dictionary_list :
            if Name in i:
                searchResults.append (i)
        if searchResults == []:
            a= "-not found any trace in database"
            self.print_B( a )
            self.push ( a  )		    
            return 
        a= list2string(searchResults)  
        self.print_B(a)  
        self.push   (a)		
        
    def get_part_details (self):
        DeviceName =  self.get_text()
        if DeviceName in self.CL  and DeviceName in self.RFDS_List_0:
            indx = self.RFDS_List_0.index(DeviceName)
            a= self.RFDS2_MCN_List_0[indx] + '  '+ self.descr[indx]
            self.print_B(a)
            self.push (a)
        else:
            a= "device Not Found" 
            self.print_B(a)   
            self.push (a)          
 
        
    def MCN_Descr_LUT (self):
        self.descr_map =[]
        self.MCN_map = []
        for index , i in enumerate(self.RFDS2_MCN_List_0):
            if i not in self.MCN_map:
                self.MCN_map.append (i)
                self.descr_map.append (  self.descr[index]  )
        
        
    def MCN_Descr_convert(self):
        Name = self.get_text()
        searchResults=[]
        if Name.count ('-')==2:
            dictionary_list = self.MCN_map
            LUT =  self.descr_map
        elif ',' in Name:
            dictionary_list = self.descr_map
            LUT = self.MCN_map
        else:
            print ('not a valid MCN or part description')
            return
          
        for index,i in  enumerate(dictionary_list) :
            if Name in i:
                searchResults.append ( LUT[i] )
                
                
        if searchResults == []:
            a= "-not found keyword in database"
            self.print_B( a )
            self.push ( a  )		    
            return 
        a= list2string(searchResults)  
        self.print_B(a)  
        self.push   (a)	        
    def bridge(self,a,b,path):
        self.G.add_node(a)
        self.G.add_node(b)
        self.G.add_edge(a,b, edge_labels =path)
    def show_graph(self)  :
        #print (len(G))
        if len(self.G) > 100:
            print ('Too Large network; ',len(self.G) ,'  disconnect some connections')
            return 0
            
        pos = nx.spring_layout(self.G)
        plt.figure()
        nx.draw(self.G,pos,edge_color='black',width=1,linewidths=1,\
        node_size=100,node_color='pink',alpha=0.9,\
        labels={node:node for node in self.G.nodes()})
        #nx.draw(self.G,with_labels=True)
        EDGELAbel= nx.get_edge_attributes(self.G,'edge_labels')
        nx.draw_networkx_edge_labels(self.G,pos,edge_labels = EDGELAbel, font_color='red')#,edge_labels={('A','B'):'AB',\
        #('B','C'):'BC',('B','D'):'BD'})
        plt.savefig("simple_path.png")
        plt.axis('off')
        plt.show()
    def process_graph (self):
        inp= self.get_text()
        self.G.clear()
        a= self.winObj.checkBox.isChecked ()
        b= self.winObj.checkBox_2.isChecked ()
        c= self.winObj.checkBox_3.isChecked ()
        d= self.winObj.checkBox_4.isChecked ()
                
        #o :    terminate(inp, True, False, False)
        #L: terminate(inp, False, False, False)
        #K: terminate(inp, False, False, True)
        #J : terminate(inp, True, True, False)
        #U : terminate(inp, False, True, False)
        self.terminate(inp, d, a, b, c)
        self.show_graph()
    def push( self, x   ):
        self.resetPointer()
        for i in range(self.Buffer_length -1 ):
            self.PastStrings[i] = self.PastStrings [i+1]
        self.PastStrings[self.Buffer_length-1 ] = x
        #print (PastStrings)  
    def goBack(self):
        if self.pointer ==0:
            self.print_B( "UnderFlow, Cant go back \n "  )
            return 
        self.pointer = self.pointer-1
        self.print_B(    self.PastStrings[ self.pointer]    )    
    def goForward(self):
        if self.pointer ==self.Buffer_length-1:
            self.print_B( "Overflow , Cant go forward \n " )
            return
        self.pointer = self.pointer+1
        self.print_B(    self.PastStrings[ self.pointer]  )
    def resetPointer(self):
        if self.pointer == self.Buffer_length-1:
             return 0
        delta = self.Buffer_length-1 - self.pointer
        # #print (PastStrings ,len (PastStrings))
        a= list (range (self.Buffer_length)  )
        a.reverse()
        for i in a:
            if i > delta:
                self.PastStrings [i] = self. PastStrings [i -   delta] 
            else:
                self.PastStrings [i] = "blank"
        self.pointer = self.Buffer_length -1

    def other_net(self,d,n, debug, Bounce_flag, Remove_RCM_path, remove_cap):
        
        '''
        0 if invalid- > cap disabled but cap encountered
        1  Teset point or CRXX   or VXXX  or something else IC
        2 if GND terminated, pull down 
        5  if net goes to a IC or connector 
        net n2 if for normal res, cap
        list n2 of len 4 if RCM resistor
        
        '''
    
        n2 = list(self.Device2NetsInternal(d))
        indx4=n2.index(n)
        del n2[indx4]
        length=len(n2)
        
        if Remove_RCM_path == True and d[0] == 'W' :
            return [0]
        if remove_cap == True and( d[0] == 'C' or d[0:2] == 'TP'):
            return [0]
        if ( d[0] == 'R' or d[0] == 'C' or d[0] == 'L' or  d[0] == 'W' ) and  not (d[0:2] == 'CR'):
            if length == 0: # for GND terminated devices #for 2 terminal RLC
                # if self.get_cap_flag == True:
                #     indx = self.RFDS_List_0.index (d)
                #     a= self.RFDS2_MCN_List_0 [indx]
                #     b= self.descr [indx]
                #     self.Cap_list_Buffer. append (d+ ';' + b+';'+a)
                return [2]
            elif length == 1:
                return n2
            elif length == 3:  # 4 terminal resistors: RCM res
                n2.insert(0, 3)
                return n2
        elif d[0:2] == 'CR' or d[0:2] == 'TP':
        #    print ('CR / TP detected')
            return [1]
        elif n[0] == 'V':
            return  [1]
        else:
         #   print ('default detection')
            if Bounce_flag == True:
                return [5]
            else:
                return  [1]        
    def check_value(self,ref_des):
        
        if not (ref_des [0] == 'R'):
            return 0
        if ref_des in self.RFDS_List_0:
            indx = self.RFDS_List_0.index(ref_des)
            temp =  self.RFDS2_MCN_List_0[indx].split ('-')[-1]
            if 'R'  in temp  or  temp =='0000' :
                return 0    # 0 means 0 ohm resisotr or low 
            else:
                return 1   # 1 means high value
        else:
            return -1 #     means res doesn't exist/ cant be decoded
    def  DNI_refdes(self):
        Name= self.get_text()
        self.DisconnectedDevices.append (Name)
    def Mount_refdes(self):
        Name= self.get_text()
        if Name in self.DisconnectedDevices :
            self.DisconnectedDevices.remove (Name)
        else:
            print ('Component Not rpesent in DNI list')
    def Get_Caps (self):
        inp= self.get_text()
        self.Get_Caps_internal(inp)
        a= list2string( self.Cap_list_Buffer  )  
        self.print_B(a)  
        self.push   (a)	   
    def Get_Caps_internal(self, textt)    :
        self.Cap_list_Buffer =[]
        self.get_cap_flag = True
        self.terminate(textt, False, False , True, False)   
        self.Cap_list_Buffer = list (set (self.Cap_list_Buffer))
        self.get_cap_flag = False
    def Capacitance_count (self):
        self.capacitance_flag=True
        inp= self.get_text()
        self.Get_Caps_internal(inp)  
        cap_value= 0
        i4= 0
        for item in self.Cap_list_Buffer :
            i3= item.split(';') [1]    
            if 'UF'in i3:
                i4= float ( i3.replace ('UF', ''))
            elif 'PF'in i3:
                i4= float ( i3.replace ('PF', '')) * 1e-12
            else:
                i4 = 1000
            cap_value = cap_value +i4
        self.capacitance_flag=False
        a= inp+ ' capacitance =  '+str (cap_value) + ' uF'
        self.print_B(a)  
        self.push   (a)	          
    def get_text(self):
        inp = self.winObj.textEdit.textCursor().selectedText() 
        return inp.upper()
    def Get_Rs(self):
        inp= self.get_text()
        self.Cap_list_Buffer =[]
        self.get_Res_flag = True
        self.terminate(inp, False, False , True, False)   
        self.Cap_list_Buffer = list (set (self.Cap_list_Buffer))
        a= list2string( self.Cap_list_Buffer  )  
        self.print_B(a)  
        self.push   (a)	          
        self.get_Res_flag = False
    def Get_NET (self):
        inp = self.get_text() 
        self.Cap_list_Buffer =[]
        self.get_net_flag =  True
        self.terminate(inp, False, False , True, False)   
        self.Cap_list_Buffer = list (set (self.Cap_list_Buffer))
        a= list2string( self.Cap_list_Buffer  )  
        self.print_B(a)  
        self.push   (a)	               
        self.get_net_flag = False           
    def Free_all_DNIed (self):
        self.DisconnectedDevices =[]
    def show_DNied (self):
        a= list2string( self.DisconnectedDevices  )  
        self.print_B(a)  
        self.push   (a)	         

    def terminate (self, net, Bounce_flag, Remove_RCM_path, Pull_up_flag, remove_cap):
        status = True
        netMain= [net]
        DoneNet=[]
        DoneDeviceListEnd=[]
        DoneDeviceListBridge=[]
        while status:
            nextNets= []
            for n in netMain:
                dev= self.Net2DevicesInternal(n)
                if dev[0] == False:         # device doesn't exist in database
                    return 0
                dev = list(set(dev))        #avoids repetition of same IC

                dev= sorted(dev,reverse=True)   #sorting is unnecessary-- recheck

                othNL=[]
                for d in dev:
                    othNL.append(self.other_net(d,n, False, Bounce_flag, Remove_RCM_path, remove_cap))
                    
                    
                    
                # this routine checks if futrthur checks need to be done- if 'bounce back feature at IC ' is enabled
                exitFlag = True
                k2= None
                for k,i in enumerate(othNL):
                    for j in i:
                        if j == 5 and exitFlag :
                            k2=k
                            exitFlag = False
                            
                if exitFlag == False:
                    #print ('U1 detected')
                    for i in range (len(othNL)):
                        if i == k2:
                            othNL[i] = [5]
                        else:
                            if not (othNL[i] == [2]):
                                othNL[i] =[1]
                for d_index in range(len(dev)):
                    d= dev[d_index]
                    if d in DoneDeviceListEnd:
                        if self.device_pin_flag == True: self.Device_Buffer.append ([ d , n ])
                        self.bridge(d, n, 'O')
                        continue
                    if d in DoneDeviceListBridge :
                        continue
                    elif d in self.DisconnectedDevices:
                        continue
                    elif d not in self.RFDS_List_0:
                        if d[0]=='C' or d[0] =='R' or d[0] == 'L':
                            continue
                    else:     
                        DoneDeviceListBridge.append (d)
                        
                    if self.get_cap_flag == True:
                        if d[0] == 'C' and d[1] != 'R' :
                            #not CR
                            indx = self.RFDS_List_0.index (d)
                            a= self.RFDS2_MCN_List_0 [indx]
                            b= self.descr [indx]
                            if self.capacitance_flag == True:
                                c= ''
                                for ii in b.split ():
                                    if 'UF' in ii or 'PF' in ii:
                                        c= ii
                                        break
                                self.Cap_list_Buffer. append (d+ ';' + c +';' + a+ ';'+ b)
                            else:
                                self.Cap_list_Buffer. append (d+ ';' + b+';'+a)                            
                        
                    elif self.get_Res_flag == True:
                        if d[0] == 'R' : #or d[0] == 'W' :
                            indx = self.RFDS_List_0.index (d)
                            a= self.RFDS2_MCN_List_0 [indx]
                            b= self.descr [indx]
                            self.Cap_list_Buffer. append (d+ ';' + b+';'+a)   
                        elif d [0] =='W':
                            self.Cap_list_Buffer. append (d)
                            
                    othN=  othNL [d_index]
                    if othN[0]== 0:    #if the net needn't be considered at all
                        continue
                    if othN[0]== 1:    #if non resistor /cap/ inductor element comes
                        self.bridge(d, n, 'O')
                        DoneDeviceListEnd.append(d)
                        if self.device_pin_flag == True: self.Device_Buffer.append ([ d , n ])
                    elif othN[0] == 2:      #2 means Grounded in the other end
                        self.bridge(d, n, 'GND')
                    elif othN[0] == 5:      # 5 means IC detected, stop searching option used
                        self.bridge(d, n, 'U')
                        DoneDeviceListEnd.append(d)
                        if self.device_pin_flag == True: self.Device_Buffer.append ([ d , n ])
                    elif othN[0] == 3:  #for 4 teminal resistors
                        self.bridge(d, n, "RCM")
                        for i in range (3):
                            self.bridge(d, othN[i+1], "RCM")
                            nextNets.append(othN[i+1])
                    else:
                        temp1 = othN[0] not in DoneNet
                        if Pull_up_flag == True:
                            temp2 = self.check_value(d)
                            if temp1:
                                if temp2 == 1 :
                                    self.bridge(othN[0], n, d+'PU')
                                elif temp2 == 0:
                                    nextNets.append(othN[0])
                                    self.bridge(othN[0], n, d)    # in case it wasn't a pull up, but net was already in the done list
                            else:
                                self.bridge(othN[0], n, d)    # in case net wasn't already in done net list
                        else:
                            self.bridge(othN[0], n, d)    #incase PU flag is absent 
                            if temp1:
                                nextNets.append(othN[0])
                DoneNet.append(n)
            if len(nextNets)== 0:
                status = False

            if Remove_RCM_path == True:
                netMain2= list(set(nextNets))
                netMain = []                
                for n in netMain2:
                    if 'RCM' not in n:
                        netMain.append (n)
            else:
                netMain = list(set(nextNets))
        if self.get_net_flag ==  True:
            self.Cap_list_Buffer  = DoneNet


		
    def Choose_BOM(self):
        if self.BOM_choose_FSM == 0:
            a= 'Select the text of BOM you need\nand then press the button again\n\n'+ list2string(self.BomName) 
            
            self.BOM_choose_FSM = 1
        else: 
            self.BOM_choose_FSM = 0
            b= self.winObj.textEdit.textCursor().selectedText() 
            if b in self.BomName:
                x= self.BomName.index (b) +1
        
                self.RFDS_List_0 = self.RFDS_List [x]
                self.RFDS2_MCN_List_0 = self.RFDS2_MCN_List [x]
                self.descr =  qpp ( self.qpp, self.RFDS_List_0 , False)
                self.MCN_Descr_LUT ()                
                a= 'BOM selected-  '+ b
            else:
                a= 'invalid BOM selected'

        self.print_B(a)  
        self.push   (a)	    
        
        a= list2string( self.DisconnectedDevices  )  
    def Capacitance_count_export (self):
        Cap_summary_list= []
        Format_1 = ''
        Format_2 = ''
        Format_3 = ''
        Format_4 = ''        
        self.capacitance_flag= True      
        for net in self.NET_storage :
            self.Get_Caps_internal(net)  
            cap_list= []
            cap_mcnL = []
            cap_descr = []
            cap_valL = []
            cap_total_value= 0
            for combo in self.Cap_list_Buffer:
                i1 = combo.split (';')
                cap_list.append (i1[0])
                cap_descr.append (i1[3])
                cap_mcnL.append (i1[2])
                i2= i1[1]
                if 'UF'in i2:
                    i3= float ( i2.replace ('UF', ''))
                elif 'PF' in i2:
                    i3= float( i2.replace ('PF', '')) * 1e-12
                else:
                    i3= 1000  
                cap_valL.append (i3)
                cap_total_value = cap_total_value + i3
            Format_1 = Format_1 + ',,'+  net  +','+ str( cap_total_value ) +'\n'
            Cap_summary_list.append ( [net,  cap_list, cap_mcnL  ,cap_descr, cap_valL   ])

        for i in Cap_summary_list:
            Format_2 = Format_2 + i [ 0 ] + '\n'
            Format_3 = Format_3 + i [ 0 ] + '\n'
            mcnset_i =list ( set (i [ 2 ]))
            for item in mcnset_i:
                indx= i [ 2 ].index ( item)
                Format_2 = Format_2 + ',,'+item + ','+ str (i [ 4 ] [indx ] )+ ',' + str (i[2].count (item))+ ','+ i [3] [indx]+ '\n'                
            for indx in range (len( i [ 1] )):
                Format_3 = Format_3 + ',,'+ i[1][indx]+ ',' + i [2][indx] + ',' + str (i[4][indx]) + ',' +i[3] [indx] +'\n'
                
        file_0 = open ('Cap_count_eLVS.csv', 'w')
        file_0.write('Summary: all values are in microfarad\n===============================================\n')
        file_0.write(Format_1)
        file_0.write('\n\n\n\Distribution Count\nNET,,MCN,Value,Occurence,Description,,,===================\n')
        file_0.write(Format_2)
        file_0.write('\n\n\n\nDetailed description\n===================================================\n')
        file_0.write(Format_3)
        file_0.write('\n\n\n')
        file_0.write(Format_4)        
        file_0.close()

        a= 'Cap values exported to Cap_count_eLVS.csv'
        self.print_B(a)  
        self.push   (a)	         

    def Add_net (self):
        Name= self.get_text()
        self.NET_storage.append(Name)
    def Show_net_storage(self):
        a= list2string( self.NET_storage  )  
        self.print_B(a)  
        self.push   (a)	   
    def free_all_nets(self):
        self.NET_storage = []
    def get_components (self):
        inp = self.get_text() 
        if inp not in self.NL:
            self.print_B( 'Net doesn\'t exist')
        self.device_pin_flag = True
        self.Device_Buffer = []
        self.terminate(inp, False, False , True, False)  
        temp_a = []
        for item in self.Device_Buffer :
            temp_a.append ( '\n'+ item [0 ]+ ' ' +item [1]  + '\n'+ self.Comp_2_net_pinName_map_global [item [0]] [ item [1] ]  )
        self.Device_Buffer = []
        self.device_pin_flag = False
        a= list2string( temp_a  )          
        self.print_B(a)  
        self.push   (a)	                    

        
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    C= Net_container()
    
    sys.exit(app.exec_())
    
'''
qpp hasn't been usede in extracting description

how cap and wwpad are excluded from plot

#sorting is unnecessary-- recheck

RCM sense resistors or other ultra low resistors 
must have 'R'010 or 0000 at last section of MCN

remove caps also removes CRXX and test points

choosing different BOM can only DNI some ersistors 
-it can't take different MCN --with different capacitance for example'

Capacitance Grid not prepared
remove manually replacing UF by nlank and remove all alphabets from string itself

'''

'''
0 if invalid- > cap disabled but cap encountered
1  Teset point or CRXX   or VXXX  or something else IC
2 if GND terminated, pull down 
5  if net goes to a IC or connector 
net n2 if for normal res, cap
(3) n2) of len 4 if RCM resistor

'''

