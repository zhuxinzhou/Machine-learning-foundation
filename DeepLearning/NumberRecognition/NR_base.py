class NeuralNetWork:
    def __init__(self,inputnodes,hiddennodes,outputnodes,learninggrate):
        #初始化网络，设置输入层，中间层，和输出层节点数
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes
        #设置学习率
        self.lr =learninggrate


        pass

    def train(self):
        #根据输入的训练数据更新节点的链路权重
    def query(self):
        #根据输入数据计算并输出答案
        pass

input_nodes = 3
hidden_nodes = 3
output_nodes = 3
learning_rate = 0.3
n = NeuralNetWork(input_nodes,hidden_nodes,output_nodes,learning_rate)