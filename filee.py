class savefile():
    def __init__(self):
        self.name = ''

        self.point = [] #x,y,rgba,thickness,texture
        self.line = [] #list of points
        self.lines = [] #list of lines
        self.pattern = [] #lines,name,width,height
        self.patterns = [] #list of patterns

        self.node = [] #type,x,y,connections
        self.nodeconfig = [] #list of nodes

        self.generation = [] #nodeconfig,width,height,seed       #seamless and other config types in future
        self.projdetails = (self.name,self.patterns,self.nodeconfig,self.generation) #name,patterns,nodeconfig,generation
    def create(self,name):
        self.name = str(name)
        self.projdetails = (self.name,self.patterns,self.nodeconfig,self.generation)
    def save(self,projdetails):
        self.patterns,self.nodeconfig,self.generation = projdetails
        self.projdetails = (self.name,self.patterns,self.nodeconfig,self.generation)

