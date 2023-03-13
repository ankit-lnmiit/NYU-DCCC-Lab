"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def build( self ):
        "Create custom topo."

        # Add hosts and switches
        h1 = self.addHost( 'h1' )
        h2 = self.addHost( 'h2' )
        a_switch = self.addSwitch( 's1' )
        b_switch = self.addSwitch( 's2' )
        c_switch = self.addSwitch( 's3' )
        d_switch = self.addSwitch( 's4' )
        e_switch = self.addSwitch( 's5' )
        

        # Add links
        self.addLink( h1, a_switch )
        self.addLink( a_switch, b_switch , 2, 1)
        self.addLink( a_switch, c_switch , 3, 1)
        self.addLink( b_switch, e_switch , 2, 1)
        self.addLink( b_switch, d_switch , 3, 1)
        self.addLink( c_switch, d_switch , 3, 2)
        self.addLink( c_switch, e_switch , 2, 2)
        self.addLink( e_switch, d_switch , 3, 3)
        self.addLink( d_switch, h2 )



topos = { 'mytopo': ( lambda: MyTopo() ) }
