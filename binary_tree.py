from mininet.log import setLogLevel
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import irange,dumpNodeConnections
class MyTopo( Topo ):
    "Binary topology example."

    def __init__( self ):
        "Create binary topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
    h1 = self.addHost( 'h1' )
    h2 = self.addHost( 'h2' )
    h3 = self.addHost( 'h3' )
    h4 = self.addHost( 'h4' )
	h5 = self.addHost( 'h5' )
	h6 = self.addHost( 'h6' )
	h7 = self.addHost( 'h7' )
	h8 = self.addHost( 'h8' )
	
	#Add switches
	s1=self.addSwitch( 's1' )
	s2=self.addSwitch( 's2' )
	s3=self.addSwitch( 's3' )
	s4=self.addSwitch( 's4' )
	s5=self.addSwitch( 's5' )
	s6=self.addSwitch( 's6' )
	s7=self.addSwitch( 's7' )
       
	 # Add links
    self.addLink( s7, s5 )
    self.addLink( s7, s6 )
    self.addLink( s5, s1 )
	self.addLink( s5, s2 )
	self.addLink( s6, s3 )
	self.addLink( s6, s4 )
	self.addLink( s1, h1 )
	self.addLink( s1, h2 )
	self.addLink( s2, h3 )
	self.addLink( s2, h4 )
	self.addLink( s3, h5 )
	self.addLink( s3, h6 )
	self.addLink( s4, h7 )
	self.addLink( s4, h8 )


topos = { 'mytopo': ( lambda: MyTopo() ) }
