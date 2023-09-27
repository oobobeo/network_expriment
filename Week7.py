from mininet.topo import Topo
class Week7( Topo ):

    def build(self,Switch_num,lossy=True):

        Switch=[]
        Left_host=self.addHost('h1',ip='10.1.1.1')
        Right_host=self.addHost('h{}'.format(Switch_num),ip='10.{}.1.1'.format(Switch_num))
        for i in range(Switch_num):
            Switch.append(self.addSwitch('s{}'.format(i+1)))
        self.addLink(Switch[0],Left_host,bw=1000,delay='1ms')
        self.addLink(Switch[Switch_num-1],Right_host,bw=1000,delay='1ms')    
        for i in range(Switch_num//4+1):
            self.addLink(Switch[4*i],Switch[4*i+1],bw=1000,delay='1ms')

        for i in range(Switch_num-2):
            if i%2==0:
                self.addLink(Switch[i],Switch[i+2],bw=1000,delay='1ms')
                self.addLink(Switch[i],Switch[i+3],bw=1000,delay='1ms')
            else:
                self.addLink(Switch[i],Switch[i+2],bw=1000,delay='1ms')

topos = { 'mytopo': ( lambda num: Week7(Switch_num=num) ) }