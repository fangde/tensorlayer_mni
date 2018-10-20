graphContext={

'vertex':{},


'edges':{}
    

}


class BasicLayer(object):

    
    def __init__(self,name):
        self.name=name


        graphContext['vertex'][self.name]=self

        print "basic"

    def get_all_layers(self):

        for k in graphContext['vertex'].iterkeys():
            print k



class SimpleLayer(BasicLayer):

    def __init__(self,name):
        self.weight=100
        super(SimpleLayer,self).__init__(name)

    def addInput(self,input):
        graphContext['edges'].update({input.name:self.name})



if  __name__=='__main__':
    

    l1=SimpleLayer('what')
    l2=SimpleLayer('disk')

    l2.addInput(l1)






    l2.get_all_layers()
    l1.get_all_layers()






    